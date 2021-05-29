from tkinter import *
from pytube import YouTube
from youtube_dl import YoutubeDL
#Window
root = Tk()
root.geometry('700x200')
root.configure(bg='black')
root.resizable(0,0)
root.title("Astin's - Youtube video downloader - 1 file at a time")
label1 = Label(root,text = 'Youtube Video & Audio Downloader', font =('Bitstream Charter', 20, 'bold'), fg='white' ,bg='black').pack()
#Enter link
link = StringVar()
label2 = Label(root, text = 'Paste the Youtube Video Link Here:', font = ('Bitstream Charter', 15, 'bold'), fg='white' ,bg='black').pack()
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
#Download video
def refresh():
    root.destroy()
button1 = Button(root,text = 'Done', font = ('Bitstream Charter', 15, 'bold') ,fg = 'red', bg = 'white', padx = 2, command = refresh).pack(side=RIGHT)
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text = 'Completed', font = ('Bitstream Charter', 15, 'bold'), fg='white' ,bg='black').pack()
button2 = Button(root,text = 'DOWNLOAD Video', font = ('Bitstream Charter', 15, 'bold') ,bg = 'red', padx = 2, command = Downloader).pack(side=BOTTOM)
#Download audio
def Audio():
    URL = str(link.get())
    audio = YoutubeDL({'format':'bestaudio'})
    audio.extract_info(URL)
    Label(root, text = 'Completed', font = ('Bitstream Charter', 15, 'bold'), fg='white' ,bg='black').pack()
button3 = Button(root,text = 'DOWNLOAD Audio', font = ('Bitstream Charter', 15, 'bold') ,bg = 'red', command = Audio).pack(side=BOTTOM)
root.mainloop()
