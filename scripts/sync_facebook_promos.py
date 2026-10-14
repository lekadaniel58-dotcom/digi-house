"""Sincronizza solo i post della pagina Facebook contenenti #PromoDigiHouse."""
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

page_id = os.environ["FACEBOOK_PAGE_ID"]
token = os.environ["FACEBOOK_PAGE_ACCESS_TOKEN"]
params = urllib.parse.urlencode({
    "fields": "id,message,permalink_url,created_time,full_picture,attachments{media,subattachments}",
    "limit": "100",
    "access_token": token,
})
url = f"https://graph.facebook.com/v24.0/{urllib.parse.quote(page_id, safe='')}/posts?{params}"
items = []
for _ in range(5):
    with urllib.request.urlopen(url, timeout=30) as response:
        payload = json.load(response)
    if "error" in payload:
        raise RuntimeError(payload["error"].get("message", "Errore Meta"))
    for post in payload.get("data", []):
        message = post.get("message", "")
        if "#promodigihouse" not in message.lower().split() and "#promodigihouse" not in message.lower():
            continue
        items.append({
            "id": post["id"],
            "text": message[:3000],
            "url": post.get("permalink_url", ""),
            "image": post.get("full_picture", ""),
            "date": post.get("created_time", ""),
        })
    url = payload.get("paging", {}).get("next")
    if not url:
        break
Path("promozioni-facebook.json").write_text(
    json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(f"Sincronizzate {len(items)} promozioni")
