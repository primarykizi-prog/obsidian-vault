"""
Google Docs → Obsidian 自動同期スクリプト
対象フォルダ: Googleドライブ内の「KeepメモSync」
出力先: Obsidian Vault の「日報/YYYY-MM-DD.md」
"""

import os
import json
from datetime import datetime, timezone, timedelta
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
    creds_json = os.environ["GOOGLE_CREDENTIALS"]
    creds_info = json.loads(creds_json)
    credentials = service_account.Credentials.from_service_account_info(
        creds_info, scopes=SCOPES
    )
    drive_service = build("drive", "v3", credentials=credentials)
    docs_service = build("docs", "v1", credentials=credentials)
    return drive_service, docs_service

def get_folder_id(drive_service, folder_name):
    results = drive_service.files().list(
        q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
        fields="files(id, name)",
    ).execute()
    files = results.get("files", [])
    if not files:
        raise Exception(f"フォルダ '{folder_name}' が見つかりません。")
    return files[0]["id"]

def get_new_docs(drive_service, folder_id, processed_ids):
    results = drive_service.files().list(
        q=f"'{folder_id}' in parents and mimeType='application/vnd.google-apps.document' and trashed=false",
        fields="files(id, name, createdTime)",
        orderBy="createdTime desc",
    ).execute()
    files = results.get("files", [])
    return [f for f in files if f["id"] not in processed_ids]

def extract_doc_text(docs_service, doc_id):
    doc = docs_service.documents().get(documentId=doc_id).execute()
    content = doc.get("body", {}).get("content", [])
    text_parts = []
    for element in content:
        if "paragraph" in element:
            for pe in element["paragraph"].get("elements", []):
                if "textRun" in pe:
                    text_parts.append(pe["textRun"].get("content", ""))
    return "".join(text_parts).strip()

def format_with_claude(text, date_str, client):
    prompt = f"""あなたはObsidian日報の整形アシスタントです。
以下はGoogle Keepの音声メモから保存されたテキストです。
これをObsidian用の日報（Markdown形式）に整形してください。

日付: {date_str}

【メモ内容】
{text}

【出力フォーマット】
---
title: 日報_{date_str}
date: {date_str}
tags:
  - 日報
  -
