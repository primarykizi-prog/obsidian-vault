import os
import json
from datetime import datetime, timedelta
from pathlib import Path
from google.oauth2 import service_account
from googleapiclient.discovery import build
import anthropic

FOLDER_NAME = "KeepメモSync"
OBSIDIAN_DAILY_PATH = "日報"
PROCESSED_IDS_FILE = ".github/processed_doc_ids.json"
SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/documents.readonly",
]

def get_google_services():
    creds_info = json.loads(os.environ["GOOGLE_CREDENTIALS"])
    credentials = service_account.Credentials.from_service_account_info(creds_info, scopes=SCOPES)
    return build("drive", "v3", credentials=credentials), build("docs", "v1", credentials=credentials)

def get_folder_id(drive_service, folder_name):
    results = drive_service.files().list(
        q="name='" + folder_name + "' and mimeType='application/vnd.google-apps.folder' and trashed=false",
        fields="files(id, name)",
    ).execute()
    files = results.get("files", [])
    if not files:
        raise Exception("folder not found: " + folder_name)
    return files[0]["id"]

def get_new_docs(drive_service, folder_id, processed_ids):
    results = drive_service.files().list(
        q="'" + folder_id + "' in parents and mimeType='application/vnd.google-apps.document' and trashed=false",
        fields="files(id, name, createdTime)",
        orderBy="createdTime desc",
    ).execute()
    return [f for f in results.get("files", []) if f["id"] not in processed_ids]

def extract_doc_text(docs_service, doc_id):
    doc = docs_service.documents().get(documentId=doc_id).execute()
    parts = []
    for element in doc.get("body", {}).get("content", []):
        if "paragraph" in element:
            for pe in element["paragraph"].get("elements", []):
                if "textRun" in pe:
                    parts.append(pe["textRun"].get("content", ""))
    return "".join(parts).strip()

def format_with_claude(text, date_str, client):
    prompt = (
        "You are an Obsidian daily note formatter.\n"
        "Format the following voice memo into a structured Obsidian daily note in Japanese.\n\n"
        "Date: " + date_str + "\n\n"
        "Memo content:\n" + text + "\n\n"
        "Output in Japanese using this format:\n"
        "---\n"
        "title: " + "日報_" + date_str + "\n"
        "date: " + date_str + "\n"
        "tags:\n"
        "  - 日報\n"
        "  - 音声メモ\n"
        "---\n\n"
        "# 📋 " + date_str + " 日報\n\n"
        "## 🎤 音声メモ（要約）\n\n"
        "## ✅ アクション・タスク\n\n"
        "## 💡 気づき・アイデア\n\n"
        "## 📝 補足メモ\n\n"
        "---\n"
        "*自動同期: Google Keep → Google Docs → Obsidian*\n"
    )
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text

def save_to_obsidian(content, date_str, daily_path):
    path = Path(daily_path) / (date_str + ".md")
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        with open(path, "a", encoding="utf-8") as f:
            f.write("\n\n---\n\n## 追加メモ（" + datetime.now().strftime("%H:%M") + "）\n\n" + content)
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    return str(path)

def load_processed_ids():
    path = Path(PROCESSED_IDS_FILE)
    if path.exists():
        with open(path, "r") as f:
            return set(json.load(f))
    return set()

def save_processed_ids(ids):
    path = Path(PROCESSED_IDS_FILE)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(list(ids), f, indent=2)

def main():
    print("=== Sync Start ===")
    anthropic_client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    drive_service, docs_service = get_google_services()
    processed_ids = load_processed_ids()
    folder_id = get_folder_id(drive_service, FOLDER_NAME)
    new_docs = get_new_docs(drive_service, folder_id, processed_ids)
    if not new_docs:
        print("No new documents.")
        return
    print(str(len(new_docs)) + " docs found.")
    for doc in new_docs:
        try:
            text = extract_doc_text(docs_service, doc["id"])
            if not text:
                processed_ids.add(doc["id"])
                continue
            created_time = datetime.fromisoformat(doc["createdTime"].replace("Z", "+00:00"))
            date_str = (created_time + timedelta(hours=9)).strftime("%Y-%m-%d")
            formatted = format_with_claude(text, date_str, anthropic_client)
            saved = save_to_obsidian(formatted, date_str, OBSIDIAN_DAILY_PATH)
            processed_ids.add(doc["id"])
            print("Saved: " + saved)
        except Exception as e:
            print("Error: " + str(e))
    save_processed_ids(processed_ids)
    print("=== Sync Complete ===")

if __name__ == "__main__":
    main()
