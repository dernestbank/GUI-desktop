# import tkinter
# from tkinter import *
# from tkinter import ttk, messagebox
# import googletrans
# import textblob


# root = Tk()


# root.title("Google Translator")
# root.geometry("1080x400")

# # # icon
# # image_icon = PhotoImage(file="google.png")
# # root.iconphoto(False, image_icon)


# def label_change():
#     c = combo1.get()
#     c1 = combo2.get()
#     label1.configure(text=c)
#     labe12.configure(text=c1)
#     root.after(1000, label_change)


# # def translate_now():
# #     global language
# #     try:
# #         text_ = text1.get(1.0, END)
# #         c2 = combo1.get()
# #         c3 = combo2.get()
# #         if text_:
# #             words = textblob.TextBlob(text_)
# #             lan = words.detect_language()
# #             for i, j in language.items():
# #                 if j == c3:
# #                     lan_ = i,
                
# #                     words = words.translate(from_lang=lan, to=str(lan_))
# #                     text2.delete(1.0, END)
# #                     text2.insert(END, words)
# #     except Exception as e:
# #         messagebox.showerror("googletrans", "please try againl")


# # from tkinter import END, messagebox
# # from textblob import TextBlob


# # def translate_now():
# #     global language
# #     try:
# #         text_ = text1.get(1.0, END)
# #         c2 = combo1.get()
# #         c3 = combo2.get()
# #         if text_:
# #             words = TextBlob(text_)
# #             lan = words.detect_language()
# #             for i, j in language.items():
# #                 if j == c3:
# #                     lan_ = i
# #                     words = words.translate(from_lang=lan, to=str(lan_))
# #                     text2.delete(1.0, END)
# #                     text2.insert(END, str(words))
# #                     break
# #     except Exception as e:
# #         messagebox.showerror("googletrans", "Please try again.")


# def translate_now():
#     # Perform the translation
#     try:
#         text_ = text1.get(1.0, tk.END)  # Get the text from the input text box
#         c2 = combo1.get()  # Get the source language from the combobox
#         c3 = combo2.get()  # Get the target language from the combobox
#         if text_:
#             words = TextBlob(text_)  # Create a TextBlob object from the input text
#             lan = words.detect_language()  # Detect the language of the input text
#             for i, j in language.items():
#                 if j == c3:
#                     lan_ = i
#                     words = words.translate(from_lang=lan, to=str(lan_))  # Translate the text
#                     text2.delete(1.0, tk.END)  # Clear the output text box
#                     text2.insert(tk.END, str(words))  # Insert the translated text into the output text box
#                     break  # Exit the loop after finding the correct language
#     except Exception as e:
#         # Show an error message if the translation fails
#         messagebox.showerror("googletrans", "Please try again.")






# # icon for title bar
# image_icon = PhotoImage(file="GUI/icons/google.png")
# root.iconphoto(False, image_icon)

# # arrow
# arrow_image = PhotoImage(file="GUI/icons/arrow2.png")
# image_label = Label(root, image=arrow_image, width=150)
# image_label.place(x=460, y=50)


# language = googletrans.LANGUAGES
# languageV = list(language.values())
# lang1 = language.keys()


# # left hand side box
# combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
# combo1.place(x=110, y=20)
# combo1.set("ENGLISH")

# label1 = Label(
#     root,
#     text="ENGLISH",
#     font="segoe 30 bold",
#     bg="white",
#     width=18,
#     bd=5,
#     relief=GROOVE,
# )
# label1.place(x=10, y=50)

# f = Frame(root, bg="Black", bd=5)
# f.place(x=10, y=118, width=440, height=210)

# text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
# text1.place(x=0, y=0, width=430, height=200)

# scrollbar1 = Scrollbar(f)
# scrollbar1.pack(side="right", fill="y")

# scrollbar1.configure(command=text1.yview)
# text1.configure(yscrollcommand=scrollbar1.set)


# # right hand side box
# # combo2 = ttk.Combobox(root, values=languageV, font="RobotV 14", state="r")
# # combo2.place(x=730, y=20)
# # combo2.set("SELECT LANGUAGE")

# combo2 = ttk.Combobox(root, values=languageV, font="RobotV 14", state="r")
# combo2.place(x=730, y=20)
# combo2.set("SELECT LANGUAGE")

# labe12 = Label(
#     root,
#     text="ENGLISH",
#     font="segoe 30 bold",
#     bg="white",
#     width=18,
#     bd=5,
#     relief=GROOVE,
# )
# labe12.place(x=620, y=50)
# # frame for translated output
# f1 = Frame(root, bg="Black", bd=5)
# f1.place(x=620, y=118, width=440, height=210)

# text2 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
# text2.place(x=0, y=0, width=430, height=200)

# scrollbar2 = Scrollbar(f1)
# scrollbar2.pack(side="right", fill="y")

# scrollbar2.configure(command=text2.yview)
# text2.configure(yscrollcommand=scrollbar2.set)


# # translate button
# translate = Button(
#     root,
#     text="Translate",
#     font="Roboto 15 bold italic",
#     activebackground="purple",
#     cursor="hand2",
#     bd=5,
#     bg="red",
#     fg="white",
#     command=translate_now,
# )
# translate.place(x=480, y=250)


# label_change()


# root.configure(bg="white")
# root.mainloop()


# https://www.youtube.com/watch?v=3ydfbFFrPWE&list=PLl316cKxhMxtOWHa88kDqm42uWz1aqGfD&index=5&ab_channel=ParvatComputerTechnology



import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from langdetect import detect

# Initialize the main application window
root = tk.Tk()
root.title("Google Translator")
root.geometry("1080x400")

# Set the icon for the title bar
image_icon = tk.PhotoImage(file="GUI/icons/google.png")
root.iconphoto(False, image_icon)

# Initialize the Translator
translator = Translator()

def label_change():
    # Update the text of the labels to match the selected languages in the comboboxes
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    # Call this function again after 1000 ms (1 second)
    root.after(1000, label_change)

def translate_now():
    try:
        text_ = text1.get(1.0, tk.END).strip()  # Get the text from the input text box and remove leading/trailing spaces
        c2 = combo1.get()  # Get the source language from the combobox
        c3 = combo2.get()  # Get the target language from the combobox
        if text_:
            lan = detect(text_)  # Detect the language of the input text using langdetect
            print(f"Detected language: {lan}")  # Debug print
            for i, j in language.items():
                if j == c3:
                    lan_ = i
                    print(f"Translating from {lan} to {lan_}")  # Debug print
                    translation = translator.translate(text_, src=lan, dest=lan_)  # Translate the text
                    text2.delete(1.0, tk.END)  # Clear the output text box
                    text2.insert(tk.END, translation.text)  # Insert the translated text into the output text box
                    break  # Exit the loop after finding the correct language
        else:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
    except Exception as e:
        print(f"Error: {e}")  # Print the error message for debugging
        messagebox.showerror("Translation Error", "Please try again.")

# Set up the arrow image
arrow_image = tk.PhotoImage(file="GUI/icons/arrow2.png")
image_label = tk.Label(root, image=arrow_image, width=150)
image_label.place(x=460, y=50)

# Get the list of languages from googletrans
language = LANGUAGES
languageV = list(language.values())

# Set up the left-hand side combobox and label
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("english")

label1 = tk.Label(
    root,
    text="ENGLISH",
    font="segoe 30 bold",
    bg="white",
    width=18,
    bd=5,
    relief=tk.GROOVE,
)
label1.place(x=10, y=50)

# Frame for the input text box
f = tk.Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = tk.Text(f, font="Robote 20", bg="white", relief=tk.GROOVE, wrap=tk.WORD)
text1.place(x=0, y=0, width=430, height=200)

# Scrollbar for the input text box
scrollbar1 = tk.Scrollbar(f)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Set up the right-hand side combobox and label
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("select language")

label2 = tk.Label(
    root,
    text="ENGLISH",
    font="segoe 30 bold",
    bg="white",
    width=18,
    bd=5,
    relief=tk.GROOVE,
)
label2.place(x=620, y=50)

# Frame for the output text box
f1 = tk.Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = tk.Text(f1, font="Robote 20", bg="white", relief=tk.GROOVE, wrap=tk.WORD)
text2.place(x=0, y=0, width=430, height=200)

# Scrollbar for the output text box
scrollbar2 = tk.Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Button to trigger the translation
translate = tk.Button(
    root,
    text="Translate",
    font="Roboto 15 bold italic",
    activebackground="purple",
    cursor="hand2",
    bd=5,
    bg="red",
    fg="white",
    command=translate_now,
)
translate.place(x=480, y=250)

# Start the label change loop
label_change()

# Set the background color of the main window and start the Tkinter event loop
root.configure(bg="white")
root.mainloop()


#ai help  and modification
#https://chatgpt.com/share/dd08011f-1e17-4255-82a2-cd64d636ad5f