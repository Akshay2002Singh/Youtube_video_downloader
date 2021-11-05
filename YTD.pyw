from tkinter import *
from tkinter.font import BOLD


# functions
def download_video():
    pass


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
    heading1=Label(root,text="ELITE AKSHAY",font="calibre 40 bold",background="red",padx=10,pady=9)
    heading1.pack()
    heading2=Label(root,text="YOUTUBE VIDEO DOWNLOADER",font="calibre 20 bold",pady=9)
    heading2.pack()
    f1=Frame(root)
    f1.pack(side=TOP,fill=BOTH,expand=True,pady=10)
    name=Label(f1,text="ENTER URL OF VIDEL",font="calibre 30 bold",pady=5)
    name.pack()
    url_input=Entry(f1,textvariable=URL,font="calibre 30 normal")
    url_input.pack()

    download_btm=Button(f1,text="Download",command=download_video,pady=5)
    download_btm.pack()
    
    
    




    root.mainloop()