from __future__ import unicode_literals
from selenium import webdriver
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

#browser = webdriver.Chrome("76.exe", options=options)

videoUrl = r"https://www.youtube.com/watch?v=TRUHxUjXv0A" #input("Youtube link: ")

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([videoUrl])

#browser.get(r"https://www.youtube.com")

