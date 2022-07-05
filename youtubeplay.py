import pytube
import os

url="https://www.youtube.com/watch?v=5_5oE5lgrhw&list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi"
playlist=pytube.Playlist(url)
t=1
for i in playlist:
    youtube=pytube.YouTube(i)
    video=youtube.streams.get_highest_resolution()
    video.download()
    os.rename(youtube.streams.get_highest_resolution().default_filename, f"{t} {youtube.streams.get_highest_resolution().default_filename} ")
    print(f"succefull download {t}")
    t+=1