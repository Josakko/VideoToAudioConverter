import os
import time
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from moviepy.editor import VideoFileClip


root = Tk()

window_width = 400
window_hight = 400

monitor_width = root.winfo_screenwidth()
monitor_hight = root.winfo_screenheight()

x = (monitor_width / 2) - (window_width / 2)
y = (monitor_hight / 2) - (window_hight / 2)

root.geometry(f'{window_width}x{window_hight}+{int(x)}+{int(y)}')
root.title("Video To Audio Converter")
root.iconbitmap("JK.ico")
root.resizable(False, False)
root.config(bg="#dbdbdb")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])   #(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv;*.mov")])
    file_path_label.config(width=35, text=file_path)

def select_save_path():
    save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
    save_path_label.config(width=35, text=save_path)

def status():
    for i in range(duration):
        progress_bar.config(value=i)
        root.update_idletasks()
        time.sleep(0.01)
    result_label.config(text="Conversion successful!")
    root.title("File Converted")
    progress_bar.config(maximum=duration)
    time.sleep(5)
    root.title("Video To Audio Converter")
    progress_bar.config(value=0)
    result_label.config(text="")
    file_path_label.config(text="")
    save_path_label.config(text="")

def convert_file():
    global duration
    file_path = file_path_label.cget("text")
    save_path = save_path_label.cget("text")
    if file_path.endswith(".mp4"):
        if save_path:
            mp4_audio = VideoFileClip(file_path)
            duration = int(mp4_audio.duration) + 1
            root.title("Converting File...")
            mp3_filename = os.path.splitext(save_path)[0] + ".mp3"
            mp4_audio.audio.write_audiofile(mp3_filename)
            result_label.config(text="Conversion successful!")
            status()
        else:
            result_label.config(text="Please select a save path")
    else:
        result_label.config(text="Please select a Video file")
        
progress_bar = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
progress_bar.pack(pady=30)

file_path_label = Label(root, font=("arial", 12), bg="#dbdbdb", text="")
file_path_label.pack(pady=5)

file_select_button = Button(root, text="Select Video File", font=("arial", 12), width=20, command=select_file)
file_select_button.pack(pady=0)

save_path_label = Label(root, font=("arial", 12), bg="#dbdbdb", text="")
save_path_label.pack(pady=0)

save_path_button = Button(root, text="Select Save Path", font=("arial", 12), width=20, command=select_save_path)
save_path_button.pack(pady=5)

result_label = Label(root, font=("arial", 12), bg="#dbdbdb", text="")
result_label.pack()

convert_button = Button(root, font=("arial", 12), width=20, text="Convert to MP3", command=convert_file)
convert_button.pack(pady=30)

root.mainloop()
