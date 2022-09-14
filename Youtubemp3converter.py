from pytube import YouTube
import os
vid = YouTube(str(input("Enter URL of the youtube video \n =>")))
mp = int(input("Do you want MP3 or MP4 file? (3 for MP3, 4 for MP4)"))
print("Please Wait....")
if mp==4:
    yvideo = vid.streams.filter(file_extension='mp4').first()
    print("Downloading the video")
elif mp==3:
    yvideo = vid.streams.filter(only_audio=True).first()
    print("Downloading the audio")
else:
    print("ERROR: Input Not Recognised")
down = yvideo.download()
print(vid.title, "\n Downloaded Succesfully")
