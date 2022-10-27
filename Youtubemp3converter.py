from msilib.schema import _Validation
from tkinter import *
from tkinter.font import BOLD
from pytube import YouTube
import os

#vid = YouTube(str(input("Enter URL of the youtube video \n =>")))
#mp = int(input("Do you want MP3 or MP4 file? (3 for MP3, 4 for MP4)"))
#print("Please Wait....")
#if mp==4:
#    yvideo = vid.streams.filter(file_extension='mp4').first()
#    print("Downloading the video")
#elif mp==3:
#    yvideo = vid.streams.filter(only_audio=True).first()
#    print("Downloading the audio")
#else:
#    print("ERROR: Input Not Recognised")
#down = yvideo.download()

window = Tk()
window.title("Youtube to MP3/MP4")
window.geometry('900x600')
icon = PhotoImage(file='youtube.png')
giticon = PhotoImage(file="github-logo.png")
linkicon = PhotoImage(file="linkedin.png")
window.iconphoto(True,icon)
window.config(background="black")
alab = Label(window,text="Download Youtube Videos in MP3 or MP4 :D",font=('Arial',30,"bold"),fg='white',bg="black")
alab.pack()
enth = Entry(window,font=("Arial",20))
enth.place(relx=0.4,rely=0.1)
    
def submit():
    global ylink 
    ylink = YouTube(str(enth.get()))
    mp3down.place_forget()
def fun_mp3():
    global mp3down
    ylink.streams.filter(only_audio=True).first().download()
    mp3down = Label(window,text="Downloaded Succesfully", font=("Arial",20,"italic"),fg="green",bg="black")
    mp3down.place(relx=0.32,rely=0.45)
def fun_mp4():
    ylink.streams.filter(file_extension='mp4').first().download()
    mp3down.place(relx=0.32,rely=0.45)
sub_but = Button(window,text="SUBMIT",command=submit)
sub_but.place(relx=0.75,rely=0.11)
sublab = Label(window,text="Enter Youtube URL:",font=("Arial",20,"bold"),fg="red",bg="black")
sublab.place(relx=0.1,rely=0.1)
mp3_but = Button(window,text="MP3",command=fun_mp3,font=("Arial",40),fg="white",bg="black")
mp3_but.place(relx=0.1,rely=0.4)
mp4_but = Button(window,text="MP4",command=fun_mp4,font=("Arial",40),fg="white",bg="black")
mp4_but.place(relx=0.7,rely=0.4)
gitlab = Label(window,text="@KartikeyCode",font=("Arial",20),fg="pink",bg="red",image=giticon,compound="left")
gitlab.place(relx=0.1,rely=0.8)
linklab = Label(window,text="@codekartikey",font=("Arial",20),fg="pink",bg="red",image=linkicon,compound="left")
linklab.place(relx=0.6,rely=0.8)
window.mainloop()
