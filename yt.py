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
download_path = 'D:/boomi/nn'
download_playlist(playlist_url, download_path)
