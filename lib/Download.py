from os import system
from random import randint

s = randint(1, 10000)

@staticmethod
def Merge():
    system(f"ffmpeg -i {s}.mp3 -i {s}.mp4 -c copy 'final.mp4'")


@staticmethod
def GetAudio(url):
    system(f"yt-dlp -f 140 {url} -o {s}.mp3")
    return None

class youtube:
    @staticmethod
    def GetVideo(url, quality):
        if quality == 1080:
            GetAudio(url)
            system(f"yt-dlp -f 399 {url} -o {s}.mp4")
            Merge()
        elif quality == 720:
            GetAudio(url)
            system(f"yt-dlp -f 298 {url} -o {s}.mp4")
            Merge()

