#!/usr/bin/env python3
"""
session_verify.py
セッション終了時の自動整合性チェック

やること：
1. 主要ファイルの最終更新日を確認（古いまま止まっていないか）
2. 重要キーワードが主要ファイルに入っているか確認
3. 「決定事項リスト」との差分をレポート
4. 問題があれば秘書メモにアラートを作成

実行方法:
  python session_verify.py

セッション終了スケジュールタスクから自動実行される
"""

import os
import sys
from pathlib import Path
from datetime import datetime, timedelta

# ===== パス設定 =====
def find_vault():
    for base in Path("/sessions").glob("*/mnt/Obsidian Vault"):
        if base.exists():
            return base
    raise FileNotFoundError("Vault未接続")

VAULT = find_vault()

# ===== 主要ファイルと「入っているべきキーワード」の定義 =====
# ここに「決まったこと」を追加していく。これがシステムの心臓部。
INTEGRITY_CHECKS = [
    {
        "file": "こういちカンパニー/MIGAKI事業戦略/MIGAKI_創業計画書_最終版.md",
        "must_contain": ["Zero Friction", "Active", "Quiet Luxury"],
        "label": "創業計画書（Geminiコンセプト反映）",
        "max_age_days": 7,  # 7日以上更新なければ警告
    },
    {
        "file": "こういちカンパニー/MIGAKI事業戦略/MIGAKIブランド設計.md",
        "must_contain": ["Zero Friction", "幸せを、磨く。"],
        "label": "ブランド設計（英語コンセプト・メインコピー）",
        "max_age_days": 7,
    },
    {
        "file": "こういちカンパニー/MIGAKI事業戦略/MIGAKI_コアコンセプト.md",
        "must_contain": ["一棟貸し", "高単価"],
        "label": "コアコンセプト（不動の原則）",
        "max_age_days": 14,
    },
    {
        "file": "こういちカンパニー/経営企画部/CLAUDE.md",
        "must_contain": ["糸魚川商工会議所", "今井"],
        "label": "経営企画部（補助金・許認可状況）",
        "max_age_days": 3,  # 3日以上更新なければ警告
    },
    {
        "file": "こういちカンパニー/MIGAKI事業戦略/_MASTER_INFO.md",
        "must_contain": ["最終更新"],
        "label": "マスター情報インデックス",
        "max_age_days": 7,
    },
]

# ===== 存在確認ファイルリスト（内容チェックなし・存在するだけでOK） =====
EXISTENCE_CHECKS = [
    "こういちカンパニー/MIGAKI事業戦略/MIGAKI_補助金完全攻略マップ_2026-04-05.md",
    "こういちカンパニー/MIGAKI事業戦略/MIGAKI_工事優先順位チェックリスト.md",
    "こういちカンパニー/役員会議/",
    "日報/",
]


def check_file(check: dict) -> dict:
    """ファイルの整合性チェック"""
    filepath = VAULT / check["file"]
    result = {
        "label": check["label"],
        "file": check["file"],
        "exists": False,
        "age_days": None,
        "missing_keywords": [],
        "status": "❌",
    }

    if not filepath.exists():
        result["status"] = "❌ ファイルなし"
        return result

    result["exists"] = True

    # 更新日チェック
    mtime = datetime.fromtimestamp(filepath.stat().st_mtime)
    age = (datetime.now() - mtime).days
    result["age_days"] = age

    if age > check.get("max_age_days", 999):
        result["status"] = f"⚠️ {age}日間未更新"
    else:
        result["status"] = "✅"

    # キーワードチェック
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        for kw in check.get("must_contain", []):
            if kw not in content:
                result["missing_keywords"].append(kw)
        if result["missing_keywords"]:
            result["status"] = f"❌ キーワード未反映: {', '.join(result['missing_keywords'])}"
    except Exception as e:
        result["status"] = f"⚠️ 読み取りエラー: {e}"

    return result


def run_checks() -> list:
    results = []
    for check in INTEGRITY_CHECKS:
        results.append(check_file(check))
    return results


def generate_report(results: list) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    ok = [r for r in results if r["status"] == "✅"]
    ng = [r for r in results if r["status"] != "✅"]

    report = f"""# セッション整合性チェックレポート

チェック日時: {now}
結果: ✅ 正常 {len(ok)}件 / ❌ 要対応 {len(ng)}件

---

## 要対応 ({len(ng)}件)
"""
    if ng:
        for r in ng:
            report += f"\n### {r['status']} — {r['label']}\n"
            report += f"- ファイル: `{r['file']}`\n"
            if r["age_days"] is not None:
                report += f"- 最終更新: {r['age_days']}日前\n"
            if r["missing_keywords"]:
                report += f"- 未反映キーワード: {', '.join(r['missing_keywords'])}\n"
    else:
        report += "\nなし\n"

    report += f"\n---\n\n## 正常 ({len(ok)}件)\n"
    for r in ok:
        report += f"- ✅ {r['label']} ({r['age_days']}日前に更新)\n"

    report += "\n---\n> 問題があれば次のセッション開始時に対応すること\n"
    return report


def save_alert(report: str, has_problems: bool):
    """問題があれば秘書メモにアラートを保存"""
    if not has_problems:
        return

    today = datetime.now().strftime("%Y-%m-%d")
    alert_dir = VAULT / "秘書メモ"
    alert_dir.mkdir(exist_ok=True)
    alert_path = alert_dir / f"整合性アラート_{today}.md"
    alert_path.write_text(report, encoding="utf-8")
    print(f"⚠️  アラートを保存しました: {alert_path}")


def main():
    print("=" * 50)
    print("🔍 セッション整合性チェック開始")
    print("=" * 50)

    results = run_checks()
    ng = [r for r in results if r["status"] != "✅"]

    for r in results:
        print(f"{r['status']}  {r['label']}")

    report = generate_report(results)

    # レポートをVaultに保存
    report_dir = VAULT / ".claude" / "skill-backups"
    report_dir.mkdir(exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    report_path = report_dir / f"integrity_report_{today}.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"\n📝 レポート: {report_path}")

    # 問題があれば秘書メモにアラート
    save_alert(report, bool(ng))

    print("=" * 50)
    return len(ng)


if __name__ == "__main__":
    sys.exit(main())
