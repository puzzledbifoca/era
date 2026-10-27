# -*- coding: utf-8 -*-
"""Download two additional Rybakina gallery images."""
import os
import urllib.request

BASE = r"C:\Users\lenovo\Doubao\chats\2026-10-26\new-chat-1\rybakina-site\assets"

IMAGES = {
    "gallery-trophy.jpg": "https://aka.doubaocdn.com/s/lrgYOgc6Vl",
    "gallery-practice.jpg": "https://aka.doubaocdn.com/s/CKZM7fFTCJ",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Referer": "https://www.doubao.com/",
}

os.makedirs(BASE, exist_ok=True)

for name, url in IMAGES.items():
    dest = os.path.join(BASE, name)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        with open(dest, "wb") as f:
            f.write(data)
        print(f"OK  {name}  {len(data)} bytes")
    except Exception as e:
        print(f"FAIL {name}: {e}")
