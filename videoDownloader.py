from pytube import YouTube
from pytube import Stream

video_url = (
    "https://www.youtube.com/watch?v=",
    "https://www.youtube.com/watch?v=",
)
download_path = r'DownloadedVideos/'

def on_progress(stream:Stream, chunks:bytes, bytes_remaining:int) -> None:
    download_percentage = (1 - bytes_remaining / stream.filesize) * 100
    print(f"Downloaded: {download_percentage:.2f}%", end="\r", flush=True)

def main_function() -> None:
    for video in video_url:
        youtube_api = YouTube(url=video)
        stream = youtube_api.streams.get_highest_resolution()

        print(f"VideoTitle: {youtube_api.title}")
        print(f"Resolution: {stream.resolution}")
        video_size = stream.filesize / pow(2, 20)
        print(f"Video-Size: {video_size:.2f} mb")

        youtube_api.register_on_progress_callback(on_progress)
        stream.download(download_path)

if __name__ == "__main__":
    main_function()