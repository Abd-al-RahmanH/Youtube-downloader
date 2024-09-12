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

# Replace this with the URL of the single video you want to download
video_url = 'https://youtu.be/7prd-nSw-IU?si=-2FXTlnyqPkrGWQY'
download_path = 'E:/Yt_single_videos'
download_video(video_url, download_path)
