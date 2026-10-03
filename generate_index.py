import os

files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

links = "\n".join([f'    <li><a href="{f}">{f.replace(".html", "").replace("-", " ").title()}</a></li>' for f in sorted(files)])

html_content = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Übersicht</title>
</head>
<body>
  <h1>Seitenübersicht</h1>
  <ul>
{links}
  </ul>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)