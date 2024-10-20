import tkinter as tk
import customtkinter as CTk
from pytube import YouTube
from tkinter import filedialog


# Function definitions

#a function to choose download desination path and to update the path label:
def choose_destination():
    folder_path = filedialog.askdirectory()
    if folder_path:
        download_path_var.set(folder_path)
    return folder_path

def update_resolutions(*args):
    try:
        ytlink = url_var.get()
        if ytlink:
            ytObject = YouTube(ytlink)
            resolutions = [stream.resolution for stream in ytObject.streams.filter(progressive=True)]
            resolution_dropdown.configure(values=resolutions)
            resolution_dropdown.set(resolutions[0] if resolutions else "No resolutions available")
    except:
        resolution_dropdown.configure(values=["Error loading resolutions"])
        resolution_dropdown.set("Error")





def startdownload():
    try:
        ytlink= link.get()
        ytObject= YouTube(ytlink, on_progress_callback=on_progress)
        # video = ytObject.streams.get_highest_resolution()
        
        selected_resolution = resolution_var.get()
        video = ytObject.streams.filter(resolution=selected_resolution, progressive=True).first()
        
        # streams = ytObject.streams.filter(progressive=True)
        # Create options for the dropdown
        # resolutions = [f"{stream.resolution} - {stream.mime_type}" for stream in streams]
        
        # # Create and pack the dropdown
        # resolution_var = tk.StringVar(app)
        # resolution_var.set(resolutions[0])  # Set default value
        # resolution_dropdown = CTk.CTkOptionMenu(app, variable=resolution_var, values=resolutions)
        # resolution_dropdown.pack(pady=10)
        
         
        # Update download button command
        download.configure(command=lambda: download_video(ytObject, resolution_var.get()))
        
        
        
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        # video.download()
        
        #to save to a specific location
        download_path = choose_destination()
        if download_path:
            video.download(output_path=download_path)
        else:
            video.download()  # Use default path if none selected
             
        
        print("download is successful")
         # Print the download location
        print("Download location:", download_path)
        
        finishLabel.configure(text="Download successful")
    except Exception as e:
        print(f"Error: {e}")
        finishLabel.configure(text="Download Error", text_color= "red")
    # finishLabel.configure(text="Done")
    print("Done!")

def download_video(ytObject, selected_resolution):
    resolution, _ = selected_resolution.split(' - ')
    video = ytObject.streams.filter(resolution=resolution, progressive=True).first()
    video.download()
    finishLabel.configure(text="Download successful")


# Global variable to store the percentage value
percentage_of_compeletion = 0

def on_progress(stream, chunk, bytes_remaining):
    global percentage_of_compeletion
    
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    print(percentage_of_compeletion)
    per = str(int(percentage_of_compeletion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_compeletion) / 100)



#system settings
CTk.set_appearance_mode("system")
CTk.set_default_color_theme("green")



# #Create the main application window 
#App framE
app= CTk.CTk()
app.geometry("720x380")
# set minimum size
app.minsize(720, 380)
app.title("Ernie's Youtube downloader")

# #Create Tkinter variables
#  a StringVar to hold the path:
download_path_var = tk.StringVar()
download_path_var.set("Default Download Path")



# #Create and pack widgets\\
#Adding UI Elements
title= CTk.CTkLabel(app, text="Insert a youtube link")
title.pack(pady=10, padx=10)

#link input
url_var= tk.StringVar()
link= CTk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()
# trace_add method on our url_var StringVar to call this function whenever the link changes:
url_var.trace_add("write", update_resolutions)


#to display available resolutions:
resolution_var = tk.StringVar()
resolution_dropdown = CTk.CTkOptionMenu(app, variable=resolution_var)
resolution_dropdown.pack(pady=10)
resolution_dropdown.set("Select Resolution")


#Chooseinput fiiledirectory
choose_path_button = CTk.CTkButton(app, text="Choose Download Path", command=choose_destination)
choose_path_button.pack(padx=10, pady=10)

# a label to display the path:
path_label = CTk.CTkLabel(app, textvariable=download_path_var)
path_label.pack(pady=5)



# Finished Downloading
finishLabel = CTk.CTkLabel(app, text="")
finishLabel.pack()

#Progrees percentage
pPercentage=CTk.CTkLabel(app, text= "0%")
pPercentage.pack()

progressBar=CTk.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download= CTk.CTkButton(app, text="Download", command=startdownload)
download.pack(padx=10, pady=10)


# #Start the main event loop for the application
#run app
app.mainloop()




#inspiration
# https://www.youtube.com/watch?v=NI9LXzo0UY0&t=327s&ab_channel=developedbyed


# to dos
# audio download available
# multiple resolution dropdown selection
#select custom download loacation
#improve UI

#transcript download option



# Here are some key features and differences between these packages:

# pytube: Supports multiple video formats, resolutions, and audio-only downloads.
# youtube-dl: Supports multiple video formats, resolutions, and audio-only downloads. Also supports downloading playlists and channels.
# yt-dlp: Supports multiple video formats, resolutions, and audio-only downloads. Also supports downloading playlists and channels, and has additional features like support for YouTube Premium and YouTube Music.
# pafy: Supports multiple video formats, resolutions, and audio-only downloads. Also provides additional features like video metadata and comments.
# youtube-python: Supports multiple video formats, resolutions, and audio-only downloads. Also provides additional features like video metadata and comments.