import os
from pathlib import Path

# --- 基本設定 ---
BASE_DIR = Path(__file__).parent
TXT_DIR = BASE_DIR / "news_texts"
NEWS_DIR = BASE_DIR / "news"
INDEX_PATH = BASE_DIR / "index.html"

def main(txt_filename):
    txt_path = TXT_DIR / txt_filename
    if not txt_path.exists():
        print(f"ファイルが見つかりません: {txt_path}")
        return

    # ファイル名から HTMLファイル名を作る
    stem = txt_path.stem  # news202510
    html_filename = f"{stem}.html"
    html_path = NEWS_DIR / html_filename

    # テキストを読み込む
    lines = txt_path.read_text(encoding="utf-8").splitlines()
    title, date, content = "", "", []
    for line in lines:
        if line.startswith("タイトル："):
            title = line.replace("タイトル：", "").strip()
        elif line.startswith("日付："):
            date = line.replace("日付：", "").strip()
        elif line.startswith("内容："):
            continue
        else:
            content.append(line.strip())

    body_html = "".join(f"<p>{line}</p>" for line in content if line)

    # HTML ページを作成
    html_template = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="../css/style_scroll_news.css" />
  <title>{title}</title>
</head>
<body>
  <header>
    <div class="logo"><a href="../index.html" style="color:white;text-decoration:none;">HaSe工業</a></div>
  </header>
  <main>
    <h1>{title}</h1>
    {body_html}
    <a href="../index.html">← ホームへ戻る</a>
  </main>
</body>
</html>
"""
    html_path.write_text(html_template, encoding="utf-8")
    print(f"[OK] {html_path} を作成しました")

    # index.html にリンクを追加
    index_html = INDEX_PATH.read_text(encoding="utf-8")
    new_line = f'  <li><a href="news/{html_filename}">{date} {title}</a></li>'
    updated_html = index_html.replace('<ul class="news-list">', f'<ul class="news-list">\n{new_line}')
    INDEX_PATH.write_text(updated_html, encoding="utf-8")
    print("[OK] index.html を更新しました")

if __name__ == "__main__":
    print("==== お知らせ追加ツール ====")
    txt_name = input("news_texts フォルダ内の .txt ファイル名を入力してください（例：news202510.txt）: ").strip()
    main(txt_name)