# YouTube Downloader By Abdul Rahman :

## Feel free to give STAR ⭐

This repository contains two separate Python programs for downloading YouTube content:

1. **Download Playlist**: Downloads all videos from a YouTube playlist.
2. **Download Single Video**: Downloads a single YouTube video.

Both programs use the `yt-dlp` library to handle the downloading process.

## Prerequisites :

Ensure you have Python installed on your system. You also need to install the `yt-dlp` library. You can install it using pip:

```bash
pip install yt-dlp
```

## Download Playlist

This script downloads all videos from a specified YouTube playlist.

### Script: `download_playlist.py`

```python
import yt_dlp

def download_playlist(playlist_url, download_path):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',  # Use 'mkv' if you prefer that format
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'noplaylist': False,  # Set to True if you want to download only a single video
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

playlist_url = 'https://youtube.com/playlist?list=PLihCJJ6_IteEo46nNNA4ksZw7ITDQ7nkS'
download_path = 'D:/Yt_videos'
download_playlist(playlist_url, download_path)
```

### How to Run

1. Replace `playlist_url` with the URL of the playlist you want to download.
2. Replace `download_path` with your desired download directory.
3. Run the script:

```bash
python download_playlist.py
```

## Download Single Video

This script downloads a single YouTube video.

### Script: `download_video.py`

```python
import yt_dlp

def download_video(video_url, download_path):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',  # Use 'mkv' if you prefer that format
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'noplaylist': True,  # Set to True to ensure only a single video is downloaded
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

video_url = 'https://www.youtube.com/watch?v=OoHPhLV43gg'
download_path = 'E:/Yt_single_videos'
download_video(video_url, download_path)
```

### How to Run

1. Replace `video_url` with the URL of the video you want to download.
2. Replace `download_path` with your desired download directory.
3. Run the script:

```bash
python download_video.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to adjust any paths or URLs as needed!
