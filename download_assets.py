# -*- coding: utf-8 -*-
"""Download Rybakina site images from tool-returned CDN URLs into assets/."""
import os
import urllib.request

BASE = r"C:\Users\lenovo\Doubao\chats\2026-10-26\new-chat-1\rybakina-site\assets"

IMAGES = {
    "hero-wimbledon-final.jpg": "https://aka.doubaocdn.com/s/ldgtOuEeLU",
    "portrait-bw.jpg": "https://aka.doubaocdn.com/s/WpoiU4288f",
    "gallery-wimbledon-action.jpg": "https://aka.doubaocdn.com/s/uvWHj3hB2l",
    "gallery-black-outfit.jpg": "https://aka.doubaocdn.com/s/USS67UvfOl",
    "gallery-title-defense.jpg": "https://aka.doubaocdn.com/s/huiHdSyfzB",
    "gallery-wimbledon-scene.jpg": "https://aka.doubaocdn.com/s/DENQC4c76O",
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
