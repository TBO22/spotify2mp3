# spotify2mp3

A lightweight Python tool that fetches any Spotify track, album, or playlist and downloads the audio in MP3 format via YouTube. Built using the Spotify Web API and `yt-dlp`, this tool offers a straightforward way to save your favorite music offline—no Spotify Premium required.

---

## 🎯 Features

- ✅ Convert Spotify links (track, album, or playlist) to MP3  
- 🔎 Smart YouTube audio search via track name and artist  
- 💽 Organizes downloads by folder for albums or playlists  
- 🧼 Automatically cleans file names to avoid OS conflicts  
- 🔧 FFMPEG post-processing for high-quality audio  

---

## ⚙️ Requirements

- Python 3.7+
- `ffmpeg` installed and added to your system path
- Spotify Developer credentials (client ID and secret)
- Required Python packages:
  - `spotipy`
  - `yt-dlp`

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/TBO22/spotify2mp3.git
cd spotify2mp3

# Install required Python packages
pip install -r requirements.txt
```

You also need to have `ffmpeg` installed:

- **macOS**: `brew install ffmpeg`
- **Windows/Linux**: [Download from https://ffmpeg.org](https://ffmpeg.org)

---

## 🔐 Spotify API Credentials

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new app and copy the **Client ID** and **Client Secret**
3. Replace the placeholders in the script:

```python
client_id = 'YOUR_SPOTIFY_CLIENT_ID'
client_secret = 'YOUR_SPOTIFY_CLIENT_SECRET'
```

---

## 🚀 Usage

Run the script and paste a Spotify track, album, or playlist URL when prompted:

```bash
python spotify2mp3.py
```

Example input:

```
Enter Spotify track, album or playlist URL: https://open.spotify.com/playlist/123abcXYZ
```

Downloads will be saved in a folder named after the album or playlist.

---

## 📁 Output Structure

```
Spotify_Downloads/
│
├── Track Name 1.mp3
├── Track Name 2.mp3
└── ...
```

For albums or playlists, a new folder will be created using the name from Spotify metadata.

---

## ❗ Disclaimer

This tool is intended for **educational and personal use only**. Redistribution of copyrighted content
may violate YouTube or Spotify's terms of service.

---
