from tkinter import *
from pytube import YouTube
from time import sleep
from os import listdir

tryied_to_download=0
temp_status=""
file_size=0
# functions
def clear_url_box():
    URL.set("")
def update_status(temp):
    statusvar.set(temp)
    sbar.update()
def update_percentage_status(temp):
    statusvar.set(f"{temp_status}\nDone : {int(temp*100)}%")
    sbar.update()
def progress(stream,chunk,byte_remaining):
    percent = (file_size-byte_remaining)/file_size
    update_percentage_status(percent)
    
def download_video():
    global tryied_to_download
    global temp_status
    global file_size
    # print('temp')
    update_status("Checking link")
    link=URL.get()
    if link!="":
        try:
            yt=YouTube(link,on_progress_callback=progress)
        except:
            tryied_to_download+=1
            if tryied_to_download<3:
                download_video()
                return
            update_status("Enter valid link")
            sleep(0.6)
            clear_url_box()
            update_status("Ready to download video")
            return
        try:
            update_status("Collecting information to download video.")
            video = yt.streams.filter(progressive=True,file_extension='mp4')
            video = video.get_highest_resolution()
        except:
            update_status("Some Error!")
            clear_url_box()
            return

        # print(video)

        try:
            # downloading the video
            file_size=video.filesize
            temp_status=f"Downloading video\nTitle:{video.title}\nSize:{video.filesize/1000000} MB"
            update_percentage_status(0)
            video.download()
        except:
            tryied_to_download+=1
            if tryied_to_download<3:
                download_video()
                return
            update_status("Some Error!")
            clear_url_box()
            return
            # print("Some Error!")
            # print('Task Completed!')
        update_status("Video Downloaded")
        sleep(0.4)
        clear_url_box()
        update_status("Ready to download video")
        delete_list()
    else:
        update_status("Enter valid link")
        sleep(0.4)
        clear_url_box()
        update_status("Ready to download video")
def delete_list():
   mylist.delete(0,END)
   showfiles()
def showfiles():
    for video_file in listdir():
        if video_file.endswith(".mp4"):
            mylist.insert(END," "+str(video_file)) 
    

    


# main body
if __name__=="__main__":
    root = Tk()
    # window size
    root.title("Elite Youtube Video Downloader")
    root.geometry("1000x600")
    root.minsize(1000,600)
    
    tryied_to_download=0

    # Variables
    URL = StringVar()
    statusvar = StringVar()
    statusvar.set("Ready to download video")
    # code to download a video
    heading1=Label(root,text="ELITE VAIBHAV",font="calibre 40 bold",relief=RAISED,background="red",padx=10,pady=9)
    heading1.pack()
    space=Label(root,text="",font="calibre 2 bold")
    space.pack()
    heading2=Label(root,text="YOUTUBE VIDEO DOWNLOADER",font="Times 25 bold",relief=RAISED,background="cyan",padx=10,pady=9,)
    heading2.pack()
    f1=Frame(root)
    f1.pack(side=TOP,fill=BOTH,expand=True,pady=10)
    name=Label(f1,text="ENTER URL OF VIDEO",font="calibre 20 bold italic",relief=FLAT,padx=8,pady=5,)
    name.pack()
    space=Label(f1,text="",font="calibre 2 bold")
    space.pack()
    url_input=Entry(f1,textvariable=URL,font="calibre 25 normal",fg="blue",relief=SUNKEN)
    url_input.pack()

    download_btn=Button(f1,text="Download",command=download_video,bd=5,fg="blue",font="calibre 18 bold")
    download_btn.pack(side = LEFT, expand = True, fill = X)
    clear_url_btn=Button(f1,text="CLEAR URL",command=clear_url_box,bd=5,font="calibre 18 bold")
    clear_url_btn.pack(side = LEFT, expand = True, fill = X)

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
