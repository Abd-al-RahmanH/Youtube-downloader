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

playlist_url = 'https://youtube.com/playlist?list=PL0igoq7HFDfC2JzFko58G1cXETcYKq9Mu&si=NDXZzz_1mncgcq7B'
download_path = 'E:\\Data_Engineer\\islamicvid'
download_playlist(playlist_url, download_path)
