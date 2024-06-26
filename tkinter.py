import os
import subprocess
import pygame
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class MediaPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Медиа Плеер")

        pygame.init()

        self.image_label = None
        self.image = None

        self.play_audio_button = tk.Button(master, text="Воспроизвести аудио", command=self.play_audio, font=('Arial', 16), bg='lightblue', fg='black')
        self.play_audio_button.pack(pady=10) 

        self.play_video_button = tk.Button(master, text="Воспроизвести видео", command=self.play_video, font=('Arial', 16), bg='lightgreen', fg='black')
        self.play_video_button.pack(pady=10)

        self.show_image_button = tk.Button(master, text="Показать изображение", command=self.show_image, font=('Arial', 16), bg='lightyellow', fg='black')
        self.show_image_button.pack(pady=10)

    def play_audio(self):
        audio_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if audio_file:
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

    def play_video(self):
        video_file = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
        if video_file:
            os.system(f"ffplay {video_file}")

    def show_image(self):
        image_file = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")])
        if image_file:
            if self.image_label:
                self.image_label.destroy()  

            self.image = Image.open(image_file)
            self.image.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(self.image)
            self.image_label = tk.Label(self.master, image=photo)
            self.image_label.image = photo
            self.image_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    player = MediaPlayer(root)
    root.mainloop()
