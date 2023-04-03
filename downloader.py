from pytube import YouTube
import pytube
import threading
import progressbar as progress
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import urllib.parse
import io

queue = False

def start2():
    try:
        global yt

        yt = YouTube(link.get(),on_progress_callback=progress)
                
        vtitle.config(text= f"Video Tittle : {yt.title}")
        vauthor.config(text= f"Video Author : {yt.author}")
        viewercount.config(text= f"Video View Count : {yt.views}")
        vlength.config(text= f"Video Length : {yt.length} Saniye")
        vdescription.config(text= f"Video Description : {yt.description}")

        raw_data = urllib.request.urlopen(yt.thumbnail_url).read()
        im = Image.open(io.BytesIO(raw_data))
        image = im.resize((500, 480))
        resize_image = ImageTk.PhotoImage(image)

        thumbnail.config(image= resize_image)
        thumbnail.image = resize_image

        rejectbut.place(x=670,y=500)
        confirmbut.place(x=550,y=500)
    except pytube.exceptions.RegexMatchError:
        messagebox.showerror("Error", "Please Enter Youtube Url Correctly!")

def Confirm2():
    L = yt.streams.filter()

    #print("\n".join([str(x) for x in L]))

    p144.place(x=350,y=150)
    p360.place(x=350,y=250)
    p720.place(x=350,y=350)
    onlysound.place(x=350,y=450)
    confirmbut.place_forget()
    rejectbut.place_forget()

    vtitle.place_forget()
    vauthor.place_forget()
    viewercount.place_forget()
    vlength.place_forget()
    vdescription.place_forget()
    thumbnail.place_forget()

def p144download2():
    global queue
    if queue == False:
        queue = True
        global stream
        stream = yt.streams.get_by_itag(17)
        stream.download(output_path='Videos')
    else:
        messagebox.showerror("Error", "Already downloading video right now!")

def p360download2():
    global queue
    if queue == False:
        queue = True
        global stream
        stream = yt.streams.get_by_itag(18)
        stream.download(output_path='Videos')
    else:
        messagebox.showerror("Error", "Already downloading video right now!")

def p720download2():
    global queue
    if queue == False:
        queue = True
        global stream
        stream = yt.streams.get_by_itag(22)
        stream.download(output_path='Videos')
    else:
        messagebox.showerror("Error", "Already downloading video right now!")
        
def onlysounddownload2():
    global queue
    if queue == False:
        queue = True
        global stream
        stream = yt.streams.get_by_itag(140)
        stream.download(output_path='Songs')
    else:
        messagebox.showerror("Error", "Already downloading video right now!")

def Reject2():
    raw_data = urllib.request.urlopen("https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/1024px-YouTube_full-color_icon_%282017%29.svg.png").read()
    im = Image.open(io.BytesIO(raw_data))
    image = im.resize((500, 380))
    resize_image = ImageTk.PhotoImage(image)

    thumbnail.config(image= resize_image)
    thumbnail.image = resize_image
    vtitle.config(text= "Video Tittle")
    vauthor.config(text= "Video Author")
    viewercount.config(text= "Video Viewer Count")
    vlength.config(text= "Video Length")
    vdescription.config(text= "Video Description")

    confirmbut.place_forget()
    rejectbut.place_forget()

def Confirm():
    threading.Thread(target=Confirm2).start()

def p144download():
    threading.Thread(target=p144download2).start()

def p360download():
    threading.Thread(target=p360download2).start()
    
def p720download():
    threading.Thread(target=p720download2).start()

def onlysounddownload():
    threading.Thread(target=onlysounddownload2).start()

def Reject():
    threading.Thread(target=Reject2).start()

def progress(streams, chunk: bytes, bytes_remaining: int):
    global stream
    global queue
    contentsize = stream.filesize
    size = contentsize - bytes_remaining

    # print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    # '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')
    sonuc = round(float(size/contentsize*100),2)
    text1.config(text= f'Video is Downloading %{sonuc}')

    if sonuc == 100:
        text1.config(text= "Download Successful")
        queue = False
        returnpage()

def refresh():
    tkWindow.update()

def returnpage():
    thumbnail.place(x=0, y=100)
    vtitle.place(x=505,y=100)
    vauthor.place(x=505,y=160)
    viewercount.place(x=505,y=220)
    vlength.place(x=505,y=280)
    vdescription.place(x=505,y=340)

    vtitle.config(text= "Video Tittle")
    vauthor.config(text= "Video Author")
    viewercount.config(text= "Video Viewer Count")
    vlength.config(text= "Video Length")
    vdescription.config(text= "Video Description")
    
    p144.place_forget()
    p360.place_forget()
    p720.place_forget()
    onlysound.place_forget()

def start():
    threading.Thread(target=start2).start()

tkWindow = Tk()
tkWindow.geometry("800x600")
tkWindow.resizable(0, 0)
tkWindow.title("Youtube Video Downloader")

text1 = Label(tkWindow, text=" ")
text1.pack()

link = Entry(tkWindow, width=50)
link.pack()

defraw_data = urllib.request.urlopen("https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/1024px-YouTube_full-color_icon_%282017%29.svg.png").read()
defim = Image.open(io.BytesIO(defraw_data))
defimage = defim.resize((500, 380))
defaultimage = ImageTk.PhotoImage(defimage)

thumbnail = Label(tkWindow, image = defaultimage)
thumbnail.place(x=0, y=100)

Button(tkWindow, text='Video Download', width=15, height=2,
    command=start).place(x=340,y=50)

vtitle = Label(tkWindow, text="Video Tittle", width=40)
vtitle.bind('<Configure>', lambda e: vtitle.config(wraplength=vtitle.winfo_width()))
vtitle.place(x=505,y=100)

vauthor = Label(tkWindow, text="Video Author", width=40)
vauthor.bind('<Configure>', lambda e: vauthor.config(wraplength=vauthor.winfo_width()))
vauthor.place(x=505,y=160)

viewercount = Label(tkWindow, text="Video Viewer Count", width=40)
viewercount.bind('<Configure>', lambda e: viewercount.config(wraplength=viewercount.winfo_width()))
viewercount.place(x=505,y=220)

vlength = Label(tkWindow, text="Video Length", width=40)
vlength.bind('<Configure>', lambda e: vlength.config(wraplength=vlength.winfo_width()))
vlength.place(x=505,y=280)

vdescription = Label(tkWindow, text="Video Description", width=40)
vdescription.bind('<Configure>', lambda e: vdescription.config(wraplength=vdescription.winfo_width()))
vdescription.place(x=505,y=340)

confirmbut = Button(tkWindow, text='Confirm', width=8, height=2, command=Confirm)
confirmbut.place(x=550,y=500)
confirmbut.place_forget()

rejectbut = Button(tkWindow, text='Reject', width=8, height=2, command=Reject)
rejectbut.place(x=670,y=500)
rejectbut.place_forget()

p144 = Button(tkWindow, text='144P', width=8, height=2, command=p144download)
p144.place(x=350,y=150)
p144.place_forget()

p360 = Button(tkWindow, text='360P', width=8, height=2, command=p360download)
p360.place(x=350,y=250)
p360.place_forget()

p720 = Button(tkWindow, text='720P', width=8, height=2, command=p720download)
p720.place(x=350,y=350)
p720.place_forget()

onlysound = Button(tkWindow, text='Sound', width=8, height=2, command=onlysounddownload)
onlysound.place(x=350,y=450)
onlysound.place_forget()


tkWindow.mainloop()
tkWindow.after(1000,refresh)