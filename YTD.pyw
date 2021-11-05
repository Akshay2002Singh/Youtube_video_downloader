from tkinter import *
from tkinter.font import BOLD
from pytube import YouTube
from os import getcwd, link

# functions
def download_video():
    link=URL.get()
    if link!="":
        try:
            yt=YouTube(link)
        except:
            print("Connection Error")

        video = yt.streams.filter(progressive=True,file_extension='mp4')
        video = yt.streams.get_highest_resolution()

        # print(video)

        try:
            # downloading the video
            video.download()
        except:
            print("Some Error!")
        print('Task Completed!')

# main body
if __name__=="__main__":
    root = Tk()
    # window size
    root.title("Elite Youtube Video Downloader")
    root.geometry("1000x500")
    root.minsize(1000,200)

    # Variables
    URL = StringVar()
    # code
    heading1=Label(root,text="ELITE AKSHAY",font="calibre 40 bold",relief=RAISED,background="red",padx=10,pady=9)
    heading1.pack()
    space=Label(root,text="",font="calibre 2 bold")
    space.pack()
    heading2=Label(root,text="YOUTUBE VIDEO DOWNLOADER",font="Times 25 bold",relief=RAISED,background="cyan",padx=10,pady=9,)
    heading2.pack()
    f1=Frame(root)
    f1.pack(side=TOP,fill=BOTH,expand=True,pady=10)
    name=Label(f1,text="ENTER URL OF VIDEO",font="calibre 30 bold italic",relief=FLAT,padx=8,pady=5,background="yellow",foreground="magenta")
    name.pack()
    space=Label(f1,text="",font="calibre 2 bold")
    space.pack()
    url_input=Entry(f1,textvariable=URL,font="calibre 25 normal",bg="cyan",fg="red",relief=SUNKEN)
    url_input.pack()

    download_btn=Button(f1,text="Download",command=download_video,pady=5,bd=5,fg="magenta",font="calibre 18 bold")
    download_btn.pack()
    
    
    




    root.mainloop()