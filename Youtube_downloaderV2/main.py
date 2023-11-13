import tkinter
from tkinter import *
import customtkinter as ct
from pytube import YouTube

ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")
bgcolor = "gray13"


# Functions
def StartDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        #title.config(text="ytObject.title")
        if not checked_state.get():
            print("Video Mode")
            stream = ytObject.streams.get_highest_resolution()
        else:
            print("Audio Mode")
            stream = ytObject.streams.filter(only_audio=True, file_extension='mp4').first()

    except:
        print("Error in link.")
        return info_label.config(text="youtube Link is Invalid!", fg="red")

    print("Downloading...............")
    info_label.config(text="Downloading...............", fg="green")
    stream.download()
    print("Download Complete")
    info_label.config(text="Download Complete", fg="green")

def on_progress(stream, chunk, bytes):
    total = stream.filesize
    byte_download = total - bytes
    percentage = (byte_download / total) * 100
    per = str(int(percentage))
    pPercentage.configure(text=per + "%")
    pPercentage.update()
    print(percentage)

    progress_bar.set(float(percentage)/100)


# Our app Frame
app = ct.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")
app.config(padx=10, pady=10)

# UI
title = ct.CTkLabel(master=app, text="Youtube Downloader", font=("Arial", 24)) #text_color="red"
title.pack()

# link
url = tkinter.StringVar()
linklabel = ct.CTkLabel(master=app, text="Enter the link:", font=("Arial", 16))
linklabel.place(x=20, y=50)
link = ct.CTkEntry(master=app, width=300, height=30, textvariable=url)
link.place(x=120, y=50)

# Check Button
checked_state = ct.BooleanVar()
checkbutton = Checkbutton(master=app, text="Audio", variable=checked_state, font=("Arial", 10), bg="grey30")
checked_state.get()
checkbutton.place(x=550, y=66)

# download button
download = ct.CTkButton(master=app, text="Download", command=StartDownload, font=("Arial", 16))
download.place(x=500, y=50)

#Progress Bar
pPercentage = ct.CTkLabel(master=app, text="0%", font=("Arial", 16))
pPercentage.place(x=630, y=92)

progress_bar = ct.CTkProgressBar(master=app, width=500, height=15)
progress_bar.set(0)
progress_bar.place(x=120, y=100)

# Information label
info_label = Label(master=app, text="", font=("Arial", 10), fg="white", bg=bgcolor)
info_label.place(x=180, y=100)



# To keep running
app.mainloop()
