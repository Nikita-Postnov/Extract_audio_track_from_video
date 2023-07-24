from tkinter import *
from tkinter import filedialog
from moviepy.editor import *

def extract_audio():
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
    if not video_path:
        return

    audio_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio files", "*.mp3")])
    if not audio_path:
        return

    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    audio.close()
    video.close()

    message_label.config(text="Аудиодорожка успешно извлечена!", fg="green")

# Создаем графический интерфейс
root = Tk()
root.title("Извлечение аудиодорожки из видео")
root.geometry("400x200")

title_label = Label(root, text="Извлечение аудиодорожки из видео", font=("Arial", 16))
title_label.pack(pady=10)

extract_button = Button(root, text="Выберите видео и извлеките аудио", command=extract_audio)
extract_button.pack(pady=20)

message_label = Label(root, text="", fg="red")
message_label.pack()

root.mainloop()
