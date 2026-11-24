import webbrowser
import urllib.parse
from yt_dlp import YoutubeDL


def search_google(query):
    url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
    webbrowser.open(url)
    return f"Searching Google for {query}"


def search_youtube(query):
    url = (
        "https://www.youtube.com/results?search_query="
        + urllib.parse.quote(query)
    )
    webbrowser.open(url)
    return f"Searching YouTube for {query}"


def play_youtube_video(query):
    try:
        ydl_opts = {
            "quiet": True,
            "extract_flat": True
        }

        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(
                f"ytsearch1:{query}",
                download=False
            )

            entries = result.get("entries", [])

            if not entries:
                return "No video found"

            video_id = entries[0]["id"]

            video_url = (
                f"https://www.youtube.com/watch?v={video_id}"
            )

            webbrowser.open(video_url)

            return f"Playing {query}"

    except Exception as e:
        print("YOUTUBE ERROR:", e)
        return "Unable to play the video"