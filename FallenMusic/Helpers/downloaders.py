# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from yt_dlp import YoutubeDL

# 📍 BU DOSYANIN BULUNDUĞU KLASÖR
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🍪 cookies.txt DOSYASININ TAM YOLU
COOKIES_PATH = os.path.join(BASE_DIR, "cookies.txt")

print("COOKIE PATH:", COOKIES_PATH)
print("COOKIE VAR MI:", os.path.exists(COOKIES_PATH))

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
    "prefer_ffmpeg": True,
    "noplaylist": True,

    # 🔐 BURASI ÇOK ÖNEMLİ
    "cookies": COOKIES_PATH,

    "extractor_args": {
        "youtube": {
            "player_client": ["android"],
            "skip": ["dash", "hls"]
        }
    },

    "http_headers": {
        "User-Agent": (
            "Mozilla/5.0 (Linux; Android 10; SM-G973F) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Mobile Safari/537.36"
        )
    },

    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }
    ],
}

ydl = YoutubeDL(ydl_opts)


def audio_dl(url: str) -> str:
    info = ydl.extract_info(url, download=False)
    file_path = os.path.join("downloads", f"{info['id']}.mp3")

    if os.path.exists(file_path):
        return file_path

    ydl.download([url])
    return file_path
