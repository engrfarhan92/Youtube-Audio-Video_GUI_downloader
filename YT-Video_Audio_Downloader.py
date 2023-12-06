# importing the necessary modules
from tkinter import *  # importing all widgets and modules from tkinter
from tkinter import messagebox as mb  # importing the messagebox module from tkinter
from tkinter import filedialog as fd  # importing the filedialog module from tkinter
from pytube import YouTube  # importing the YouTube class from pytube
import yt_dlp
import os



def browse_folder():
    Label(text="Note: Please wait while Button colour changes back ", font='Arial 12 italic', fg='red',
          bg='#F1F1D3', width='70').pack()
    # using the askdirectory() method of the filedialog module to select the directory
    download_path = fd.askdirectory(initialdir="D:/Downloads", title="Select the folder to save the video")
    # using the set() method to set the directory path in the entry field
    download_dir.set(download_path)



def download_video():

    # using the get() method to retrieve the string from the entry fields
    # mb.showinfo('concepts.pk','please wait Video File is downloading')
    youtube_url = video_url.get()
    download_folder = download_dir.get()

    # checking if the entry fields are not entry
    if youtube_url != "" and download_folder != "":
        # creating an object of the YouTube class for the request URL
        video = YouTube(youtube_url)

        # selecting the stream with file extension = 'mp4', progressive = 'True',
        # and itagl = '22' in order to download the video of 720p resolution
        video_stream = video.streams.filter(file_extension="mp4", progressive=True, res="360p",
                                            type="video").get_by_itag(18)

        # selecting the download folder
        video_stream.download(download_folder)

        # displaying a message indicating the successful download
        mb.showinfo("Download Complete", "Selected Video is downloaded\nand saved successfully in " + download_folder)

        # else statement
    else:
        # displaying an error message indicating empty fields
        mb.showerror("Empty Fields", "Fields are empty!")

    # function to reset the entries


def download_audio():

    # using the get() method to retrieve the string from the entry fields
    # mb.showinfo('concepts.pk', 'please wait Audio file is downloading')
    youtube_url = video_url.get()
    download_folder = download_dir.get()

    # checking if the entry fields are not entry
    if youtube_url != "" and download_folder != "":

        if youtube_url.find('&list') > 0:
            y = int(youtube_url.find('&list'))
            z = youtube_url[0:y]
        else:
            z = youtube_url

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '240',
            }],
            'outtmpl': download_folder + '/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([z])

        # creating an object of the YouTube class for the request URL
        # video = YouTube(youtube_url)

        # selecting the stream with file extension = 'mp4', progressive = 'True',
        # and itag = '22' in order to download the video of 720p resolution
        # video_stream = video.streams.filter(file_extension="mp4", progressive=True, res="720p",
        #                                   type="video").get_by_itag(22)

        # selecting the download folder
        # video_stream.download(download_folder)

        # displaying a message indicating the successful download
        mb.showinfo("Download Complete", "Selected Audio is downloaded\nand saved successfully in " + download_folder)

        # else statement
    else:
        # displaying an error message indicating empty fields
        mb.showerror("Empty Fields", "Fields are empty!")

    # function to reset the entries


def reset():
    # using the set() method to set the values
    # of the entry fields to empty string
    video_url.set("")
    download_dir.set("")

    # using the focus_set() method to set the
    # cursor focus to first entry field
    url_field.focus_set()


# function to close the application


def exiti():
    # using the destroy() method to close the application
    gui_root.destroy()


# ------------------------- main function -------------------------

if __name__ == "__main__":
    # creating an object of the Tk() class
    gui_root = Tk()

    # setting the title of the window
    gui_root.title("Youtube Downloader by Concepts.pk")

    # setting the size and position of the window
    gui_root.geometry("580x250")

    # disabling the resizable option for better UI
    # gui_root.resizable(0, 0)

    # configuring the background color of the window
    gui_root.config(bg="#F1F1D3")


    p1 = PhotoImage(file='ico.png')
    gui_root.iconphoto(False, p1)



# Edit Environment Variale for mp3 conversion using ffmpeg codec


    x = 'C:/ffmpeg/bin'
    pathi = os.environ.get('Path') + x
    os.environ['Path'] = pathi
    print(os.environ.get('Path'))



    def popup(event):
        try:
            menu.tk_popup(event.x_root, event.y_root)  # Pop the menu up in the given coordinates
        finally:
            menu.grab_release()  # Release it once an option is selected


    def paste():
        clipboard = gui_root.clipboard_get()  # Get the copied item from system clipboardem clipboar
        url_field.insert('end', clipboard)  # Insert the item into the entry widget


    def copy():
        inp = url_field.get()  # Get the text inside entry widget
        gui_root.clipboard_clear()  # Clear the tkinter clipboard
        gui_root.clipboard_append(inp)  # Append to system clipboard


    menu = Menu(gui_root, tearoff=0)  # Create a menu
    menu.add_command(label='Copy', command=copy)  # Create labels and commands
    menu.add_command(label='Paste', command=paste)

    # configuring the icon of the window
    gui_root.iconbitmap()

    # adding frames to the window using the Frame() widget
    header_frame = Frame(gui_root, bg="#F1F1D3")
    entry_frame = Frame(gui_root, bg="#F1F1D3")
    button_frame = Frame(gui_root, bg="#F1F1D3")

    # using the pack() method to set the positions of the frames
    header_frame.pack()
    entry_frame.pack()
    button_frame.pack()


    image_label = Label(
        header_frame,
        # t        image=the_image,
        bg="#F1F1D3",
        fg="#FE0700",
        anchor=SE
    )
    header_label = Label(
        header_frame,
        text="YouTube Downloader by Concepts.pk",
        font=("verdana", "14", "bold"),
        fg="#2F2465",
        bg="#F1F1D3"

    )


    image_label.grid(row=0, column=0, padx=10, pady=10)
    header_label.grid(row=0, column=1, padx=10, pady=10)

    # ------------------------- the entry_frame frame -------------------------


    url_label = Label(
        entry_frame,
        text="Video URL:",
        font=("verdana", "10"),
        bg="#F1F1D3",
        fg="#000000",
        anchor=SE
    )
    des_label = Label(
        entry_frame,
        text="Destination:",
        font=("verdana", "10"),
        bg="#F1F1D3",
        fg="#000000",
        anchor=SE
    )


    url_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)
    des_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    # creating the objects of the StringVar() class
    video_url = StringVar()
    download_dir = StringVar()


    url_field = Entry(
        entry_frame,
        textvariable=video_url,
        width=35,
        font=("verdana", "10"),
        bg="#FFFFFF",
        fg="#000000",
        relief=GROOVE
    )
    des_field = Entry(
        entry_frame,
        textvariable=download_dir,
        width=26,
        font=("verdana", "10"),
        bg="#FFFFFF",
        fg="#000000",
        relief=GROOVE
    )


    url_field.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
    des_field.grid(row=1, column=1, padx=5, pady=5)


    browse_button = Button(
        entry_frame,
        text="Browse",
        width=7,
        font=("verdana", "10"),
        bg="#FF9200",
        fg="#FFFFFF",
        activebackground="#FFE0B7",
        activeforeground="#000000",
        relief=GROOVE,
        command=browse_folder
    )


    browse_button.grid(row=1, column=2, padx=5, pady=5)

    # ------------------------- the button_frame frame -------------------------


    download_button = Button(
        button_frame,
        text="Download Video",
        width=14,
        font=("verdana", "10"),
        bg="#1B6E20",
        fg="#FFFFF8",
        activebackground="#17F9B8",
        activeforeground="#000000",
        relief=GROOVE,
        command=download_video
    )

    download_audio_button = Button(
        button_frame,
        text="Download AUdio",
        width=14,
        font=("verdana", "10"),
        bg="#352887",
        fg="#FFFFFF",
        activebackground="#A496F9",
        activeforeground="#000000",
        relief=GROOVE,
        command=download_audio
    )

    reset_button = Button(
        button_frame,
        text="Clear",
        width=12,
        font=("verdana", "10"),
        bg="#23B1E6",
        fg="#FFFFFF",
        activebackground="#C3E6EF",
        activeforeground="#000000",
        relief=GROOVE,
        command=reset
    )
    close_button = Button(
        button_frame,
        text="Exit",
        width=12,
        font=("verdana", "10"),
        bg="#F64247",
        fg="#FFFFFF",
        activebackground="#F7A2A5",
        activeforeground="#000000",
        relief=GROOVE,
        command=exiti
    )


    download_button.grid(row=0, column=0, padx=5, pady=10)
    download_audio_button.grid(row=0, column=1, padx=5, pady=10)
    reset_button.grid(row=0, column=2, padx=5, pady=10)
    close_button.grid(row=0, column=3, padx=5, pady=10)



    url_field.bind('<Button-3>', popup)




    Label(text="Concepts Coding--www.concepts.pk--Farhan--03009665776", font='Times 15 bold', fg='#2F2465',
          bg='#F1F1D3', width='70', relief=SUNKEN).pack(side='bottom')

    Label(text="For feedback or suggestions email us : ENGR.FARHAN.92@gmail.com", font='Arial 10 italic', fg='#2F2465',
          bg='#F1F1D3', width='70', relief=SUNKEN).pack(side='bottom')

    gui_root.mainloop()
