from tkinter import *
from tkinter.font import BOLD
from typing import List
from pytube import YouTube
from time import sleep
import os

# functions
def update_status(temp):
    statusvar.set(temp)
    sbar.update()
def download_video():
    update_status("Checking link")
    link=URL.get()
    if link!="":
        try:
            yt=YouTube(link)
        except:
            update_status("Enter valid link")
            sleep(0.6)
            update_status("Ready to download video")
            return

        update_status("Collecting information to download video.")
        video = yt.streams.filter(progressive=True,file_extension='mp4')
        video = video.get_highest_resolution()


        # print(video)

        try:
            # downloading the video
            update_status("Downloading video")
            video.download()
        except:
            update_status("Some Error!")
            return
            # print("Some Error!")
            # print('Task Completed!')
        update_status("Video Downloaded")
        delete_list()
    else:
        update_status("Enter valid link")
        sleep(0.4)
        update_status("Ready to download video")
def delete_list():
   mylist.delete(0,END)
   showfiles()
def showfiles():
    for video_file in os.listdir():
        if video_file.endswith(".mp4"):
            mylist.insert(END,str(video_file)) 
    

    


# main body
if __name__=="__main__":
    root = Tk()
    # window size
    root.title("Elite Youtube Video Downloader")
    root.geometry("1000x600")
    root.minsize(1000,600)
    
    # Variables
    URL = StringVar()
    statusvar = StringVar()
    statusvar.set("Ready to download video")
    # code to download a video
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

    download_btn=Button(f1,text="Download",command=download_video,pady=5,bd=5,fg="red",font="calibre 18 bold")
    download_btn.pack()

    # show files 
    f2=Frame(root)
    f2.pack(side=TOP,fill=BOTH,expand=True)
    heading_files=Label(f2,text="Downloaded Files",font="Times 20 bold",relief=RAISED,background="yellow",padx=10,pady=9,)
    heading_files.pack(side=TOP)
    # files 
    mylist = Listbox(f2,height=4)
    mylist.pack(side=LEFT,fill=BOTH,expand=True)
    Scroll =Scrollbar(f2)
    Scroll.pack(side=RIGHT,fill=Y)
    showfiles()

    Scroll.config(command=mylist.yview)
    mylist.config(yscrollcommand=Scroll.set)


    
    
    # statusbar
    sbar = Label(root,textvariable=statusvar, relief=SUNKEN, anchor="w",padx=10,pady=7,background="cyan",fg="red",font="calibre 12 bold")
    sbar.pack(side=BOTTOM, fill=X)



    root.mainloop()