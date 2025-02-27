import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        print("Download Complete!")
    except:
        print("Youtube link is invalid")
    # print("Download Complete!")

# System Settings
customtkinter. set_appearance_mode("system")
customtkinter. set_default_color_theme("blue")


# Our app frame
app = customtkinter. CTk()
app.geometry("720x480")
app. title("Youtube Downloader")

# Adding UI Elements
title = customtkinter. CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link input\
url_var = tkinter.StringVar()
link = customtkinter. CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download Button
download = customtkinter. CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()