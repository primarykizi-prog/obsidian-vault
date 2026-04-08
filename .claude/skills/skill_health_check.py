#!/usr/bin/env python3
"""
skill_health_check.py
こういちカンパニー スキル自動検証・修復ループ

実行方法:
  python skill_health_check.py [--repair]

オプション:
  --repair   問題のあるスキルをバックアップから自動修復して .skill ファイルを生成する

出力:
  - コンソールに検証結果
  - Obsidian Vault/.claude/skill-backups/health_report_YYYY-MM-DD.md に検証レポート保存
  - 問題スキルは Obsidian Vault/.claude/skill-backups/<name>/SKILL.md のバックアップと照合
  - --repair 時は /tmp/<name>-repaired/ に修復版を作成、.skill ファイルを outputs/ に保存
"""

import os
import sys
import re
import shutil
import zipfile
import fnmatch
from pathlib import Path
from datetime import datetime

# ======== パス設定 ========
# セッションマウントを動的検出
def find_vault():
    for base in Path("/sessions").glob("*/mnt/Obsidian Vault"):
        if base.exists():
            return base
    raise FileNotFoundError("Obsidian Vault が見つかりません")

VAULT = find_vault()
SKILLS_DIR = VAULT.parent.parent.parent / "mnt" / ".claude" / "skills"
# Cowork スキルのマウントパスを動的検出
COWORK_SKILLS = None
for p in Path("/sessions").glob("*/mnt/.claude/skills"):
    if p.exists():
        COWORK_SKILLS = p
        break

BACKUP_DIR = VAULT / ".claude" / "skill-backups"
OUTPUTS_DIR = VAULT / ".claude" / "skill-backups" / "outputs"

BACKUP_DIR.mkdir(parents=True, exist_ok=True)
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

# ======== 途中切れ検出パターン ========
# 末尾がこれらのパターンにマッチしたら途中切れと判定
TRUNCATION_PATTERNS = [
    r"[^。\.\!\?！？`』」\n]$",   # 文が閉じていない
    r"[（(（【]$",                  # 開き括弧で終わる
    r"[a-z0-9ぁ-ん\u4e00-\u9fff]$",  # 普通の文字で終わる（記号なし）
]

# 末尾がこれなら正常（完結している）
COMPLETE_ENDINGS = [
    r"```\s*$",          # コードブロック終わり
    r"[。\.！？!?]\s*$", # 文末句読点
    r"[^\S\n]*[-\*]\s*$",  # リスト項目
    r"[）)）】』」]\s*$", # 閉じ括弧
    r"^\s*$",            # 空行
    r"luck!",            # 英語の文末
    r"[a-zA-Z]\.$",      # 英語文末
]

def is_truncated(content: str, skill_name: str) -> tuple[bool, str]:
    """スキルファイルが途中切れかどうかを判定する"""
    lines = content.strip().split('\n')
    if not lines:
        return True, "ファイルが空"

    last_line = lines[-1].strip()

    # 明らかな途中切れパターン
    obvious_cuts = [
        last_line.endswith("（実際の"),
        last_line.endswith("⚠️ "),
        last_line.endswith("生"),  # 「生...」
        last_line.endswith("なってい"),
        last_line.endswith(" #I"),
        last_line.endswith("てい"),
        last_line.endswith("おり"),
        len(last_line) > 0 and last_line[-1] in "（(【「『",
    ]

    if any(obvious_cuts):
        return True, f"末尾が途中切れ: '{last_line[-20:]}'"

    # frontmatter チェック
    if not content.startswith("---"):
        return True, "frontmatter がない"

    fm_end = content.find("---", 3)
    if fm_end == -1:
        return True, "frontmatter が閉じていない"

    # name フィールドチェック
    if "name:" not in content[:fm_end]:
        return True, "frontmatter に name がない"

    return False, "正常"


def check_all_skills() -> dict:
    """全スキルを検証して結果を返す"""
    if not COWORK_SKILLS:
        print("ERROR: Cowork スキルディレクトリが見つかりません")
        return {}

    results = {}

    for skill_dir in sorted(COWORK_SKILLS.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_name = skill_dir.name
        skill_md = skill_dir / "SKILL.md"

        if not skill_md.exists():
            results[skill_name] = {
                "status": "ERROR",
                "reason": "SKILL.md が存在しない",
                "lines": 0,
                "has_backup": False,
            }
            continue

        try:
            content = skill_md.read_text(encoding="utf-8")
        except Exception as e:
            results[skill_name] = {
                "status": "ERROR",
                "reason": f"読み取りエラー: {e}",
                "lines": 0,
                "has_backup": False,
            }
            continue

        lines = len(content.split('\n'))
        truncated, reason = is_truncated(content, skill_name)

        # バックアップの存在確認
        backup_path = BACKUP_DIR / skill_name / "SKILL.md"
        has_backup = backup_path.exists()

        results[skill_name] = {
            "status": "TRUNCATED" if truncated else "OK",
            "reason": reason,
            "lines": lines,
            "has_backup": has_backup,
            "content": content if not truncated else None,
        }

    return results


def save_backup(skill_name: str, content: str):
    """正常なスキルをバックアップとして保存"""
    backup_dir = BACKUP_DIR / skill_name
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup_path = backup_dir / "SKILL.md"
    backup_path.write_text(content, encoding="utf-8")

    # バックアップ日時を記録
    meta_path = backup_dir / "backup_meta.txt"
    meta_path.write_text(
        f"last_backup: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"lines: {len(content.split(chr(10)))}\n",
        encoding="utf-8"
    )


def package_skill(skill_dir: Path, output_dir: Path) -> Path:
    """スキルを .skill ファイルにパッケージ化"""
    skill_name = skill_dir.name
    output_path = output_dir / f"{skill_name}.skill"

    EXCLUDE_DIRS = {"__pycache__", "node_modules", "evals"}
    EXCLUDE_GLOBS = {"*.pyc"}
    EXCLUDE_FILES = {".DS_Store"}

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in skill_dir.rglob("*"):
            if file_path.is_file():
                rel_path = file_path.relative_to(skill_dir.parent)
                parts = rel_path.parts
                if any(part in EXCLUDE_DIRS for part in parts):
                    continue
                if file_path.name in EXCLUDE_FILES:
                    continue
                if any(fnmatch.fnmatch(file_path.name, pat) for pat in EXCLUDE_GLOBS):
                    continue
                zf.write(file_path, rel_path)

    return output_path


def repair_from_backup(skill_name: str) -> bool:
    """バックアップから修復して .skill ファイルを生成"""
    backup_path = BACKUP_DIR / skill_name / "SKILL.md"

    if not backup_path.exists():
        print(f"  ⚠️  {skill_name}: バックアップなし。手動修復が必要")
        return False

    # /tmp に修復版を作成
    repair_dir = Path(f"/tmp/{skill_name}-repaired")
    repair_dir.mkdir(exist_ok=True)
    repair_skill_md = repair_dir / "SKILL.md"

    shutil.copy2(backup_path, repair_skill_md)

    # パッケージ化
    output_path = package_skill(repair_dir, OUTPUTS_DIR)
    print(f"  ✅ {skill_name}: バックアップから修復 → {output_path}")
    return True


def generate_report(results: dict, repaired: list) -> str:
    """Obsidian用レポートを生成"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    ok_skills = [n for n, r in results.items() if r["status"] == "OK"]
    bad_skills = [n for n, r in results.items() if r["status"] != "OK"]

    report = f"""# スキル健全性レポート

更新日時: {now}
検査スキル数: {len(results)}
正常: {len(ok_skills)} / 問題あり: {len(bad_skills)}

---

## ✅ 正常スキル ({len(ok_skills)}件)

"""
    for name in ok_skills:
        r = results[name]
        backup_icon = "💾" if r["has_backup"] else "⚠️"
        report += f"- {backup_icon} **{name}** ({r['lines']}行)\n"

    if bad_skills:
        report += f"\n---\n\n## ❌ 問題あり ({len(bad_skills)}件)\n\n"
        for name in bad_skills:
            r = results[name]
            repaired_icon = "🔧 修復済み" if name in repaired else "🚨 要手動修復"
            report += f"- **{name}**: {r['reason']} ({r['lines']}行) → {repaired_icon}\n"

        if repaired:
            report += f"""
---

## 🔧 修復済みスキルのインストール方法

以下の .skill ファイルをダブルクリックしてインストールしてください：

"""
            for name in repaired:
                skill_file = OUTPUTS_DIR / f"{name}-repaired.skill"
                if skill_file.exists():
                    report += f"- `{skill_file}`\n"

    report += f"\n---\n\n> 次回自動チェック: スケジュールタスクで毎朝実行\n"

    return report


def main():
    repair_mode = "--repair" in sys.argv

    print("=" * 50)
    print("🔍 スキル健全性チェック開始")
    print(f"   スキルディレクトリ: {COWORK_SKILLS}")
    print(f"   バックアップ先: {BACKUP_DIR}")
    print(f"   修復モード: {'ON' if repair_mode else 'OFF'}")
    print("=" * 50)

    results = check_all_skills()
    repaired = []

    # 正常スキルはバックアップ保存
    print("\n📦 正常スキルをバックアップ中...")
    for name, result in results.items():
        if result["status"] == "OK" and result.get("content"):
            save_backup(name, result["content"])
            print(f"  💾 {name} ({result['lines']}行) → バックアップ保存")

    # 問題スキルの報告
    bad_skills = {n: r for n, r in results.items() if r["status"] != "OK"}

    if bad_skills:
        print(f"\n⚠️  問題のあるスキル: {len(bad_skills)}件")
        for name, result in bad_skills.items():
            print(f"  ❌ {name}: {result['reason']} ({result['lines']}行)")

            if repair_mode:
                if repair_from_backup(name):
                    repaired.append(name)
    else:
        print("\n✅ 全スキル正常！")

    # レポート生成・保存
    report = generate_report(results, repaired)
    report_path = BACKUP_DIR / f"health_report_{datetime.now().strftime('%Y-%m-%d')}.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"\n📝 レポート保存: {report_path}")

    if bad_skills and not repair_mode:
        print("\n💡 修復するには: python skill_health_check.py --repair")

    print("=" * 50)
    return len(bad_skills)


if __name__ == "__main__":
    sys.exit(main())
