from pytube import YouTube
import yt_dlp

video = YouTube('https://www.youtube.com/watch?v=grPjRbBWuQQ')

video_stream = video.streams.filter(file_extension="mp4", progressive=True, res="360p",
                                    type="video").get_by_itag(18)

# selecting the download folder
video_stream.download('D:/')


URLS = ['https://www.youtube.com/watch?v=grPjRbBWuQQ']

ydl_opts = {
    'format': 'mp3/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)