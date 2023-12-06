from pytube import YouTube
import yt_dlp

download = 0

def download_audio(path,URL):
    x= path
    if URL.find('&list') > 0:
        y = int(URL.find('&list'))
        z = URL[0:y]
    else:
        z = URL

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '240',
        }],
        'outtmpl':x + '/%(title)s.%(ext)s',
    }

#    link = request.GET.get('video_url')

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([z])


def download_video(path, URL):
    video = YouTube(URL)

    video_stream = video.streams.filter(file_extension="mp4", progressive=True, res="360p",
                                        type="video").get_by_itag(18)

    # selecting the download folder
    video_stream.download(path)

if download == 0:
    download_audio('D:/', 'https://www.youtube.com/watch?v=X-yIEMduRXk&list=RDQMGOS1-cYu928&start_radio=1')
else:
    download_video('D:/', 'https://www.dailymotion.com/video/x8p1n8a')