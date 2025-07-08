import os
import re
import sys
import shutil
import spotipy
import yt_dlp
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")


def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("Error: 'ffmpeg' not found. Install it using Homebrew or download from ffmpeg.org.")
        sys.exit(1)


def get_spotify_type_and_id(url):
    match = re.match(r"https://open\.spotify\.com/(track|album|playlist)/([a-zA-Z0-9]+)", url)
    if not match:
        print("Invalid Spotify URL.")
        sys.exit(1)
    return match.group(1), match.group(2)


def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)


def get_queries_from_spotify(url):
    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    )
    url_type, spotify_id = get_spotify_type_and_id(url)
    queries = []
    folder = "Spotify_Downloads"

    if url_type == "track":
        track = sp.track(spotify_id)
        title = track["name"]
        artists = ", ".join(artist["name"] for artist in track["artists"])
        queries.append(f"{title} {artists} audio")
        folder = sanitize_filename(f"{title} - {artists}")

    elif url_type == "album":
        album = sp.album(spotify_id)
        folder = sanitize_filename(f"{album['name']} - {album['artists'][0]['name']}")
        for track in album["tracks"]["items"]:
            title = track["name"]
            artists = ", ".join(artist["name"] for artist in track["artists"])
            queries.append(f"{title} {artists} audio")

    elif url_type == "playlist":
        playlist = sp.playlist(spotify_id)
        folder = sanitize_filename(playlist["name"])
        for item in sp.playlist_tracks(spotify_id)["items"]:
            track = item.get("track")
            if not track:
                continue
            title = track["name"]
            artists = ", ".join(artist["name"] for artist in track["artists"])
            queries.append(f"{title} {artists} audio")

    return queries, folder


def download_from_youtube(query, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'default_search': 'ytsearch',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([query])


def main():
    check_ffmpeg()

    spotify_url = input("Enter Spotify track, album or playlist URL: ").strip()
    queries, folder = get_queries_from_spotify(spotify_url)

    print(f"\nSaving downloads to: {folder}\n")
    for idx, query in enumerate(queries, 1):
        print(f"[{idx}/{len(queries)}] Downloading: {query}")
        try:
            download_from_youtube(query, folder)
        except Exception as e:
            print(f"Failed to download '{query}': {e}")

    print("\nDone.")


if __name__ == "__main__":
    main()
