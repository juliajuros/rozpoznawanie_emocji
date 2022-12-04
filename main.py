import threading
import wave
from tkinter import *
from tkinter import messagebox
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfilename
import pyaudio


class Audio:
    def __init__(self):
        self.rozpocznij_nagrywanie = False
        self.frames = []
        self.format = pyaudio.paInt16
        self.channels = 1
        self.fs = 44100
        self.frames_per_buffer = 1024
        self.filename = ''
        self.filetypes = ['*.wav', "*.mp3", "*.flac", "*.m4a"]

    def nagraj_audio(self):
        self.rozpocznij_nagrywanie = True
        t = threading.Thread(target=self.nagrywanie)
        t.start()

    def nagrywanie(self):
        self.frames = []
        stream = pyaudio.PyAudio().open(format=self.format, channels=self.channels, rate=self.fs, input=True,
                                        frames_per_buffer=self.frames_per_buffer)
        while self.rozpocznij_nagrywanie:
            data = stream.read(self.frames_per_buffer)
            self.frames.append(data)

        stream.stop_stream()
        stream.close()
        pyaudio.PyAudio().terminate()

    def zakoncz_audio(self):
        self.rozpocznij_nagrywanie = False

    def znajdz_audio(self):
        file = filedialog.askopenfilename(filetypes=[("Audio files", self.filetypes)])
        if file:
            print(file)
            # openfile tu pewnie
            # content = file.read()
            # file.close()
            # print("%d characters in this file" % len(content))

    def zapisz_audio(self):
        self.filename = asksaveasfilename(title="Save as",
                                          filetypes=[("wav", '*.wav'), ("mp3", '*.mp3'), ("m4a", '*.m4a'), ("flac", '*.flac')],
                                          defaultextension=".wav")
        obj = wave.open(self.filename, 'wb')
        obj.setnchannels(self.channels)
        obj.setsampwidth(pyaudio.PyAudio().get_sample_size(self.format))
        obj.setframerate(self.fs)
        obj.writeframes(b''.join(self.frames))
        obj.close()


# class F0:

# class Klasyfikacja:


class GUI:

    def show_msg(self):
        messagebox.showinfo("Message", "Hey There! I hope you are doing well.")  # do wywalenia

    def buttons(self):
        window = Tk()
        window.geometry("900x500")

        audio = Audio()

        wprowadz_audio = Button(text='wprowadź audio', command=audio.znajdz_audio)
        wprowadz_audio.place(x=50, y=60)
        rozpocznij_nagrywanie = Button(text='rozpocznij nagrywanie', command=audio.nagraj_audio)
        rozpocznij_nagrywanie.place(x=50, y=120)
        zakoncz_nagrywanie = Button(text='zakończ nagrywanie', command=audio.zakoncz_audio)
        zakoncz_nagrywanie.place(x=50, y=150)
        zapisz_audio = Button(text='zapisz audio', command=audio.zapisz_audio)
        zapisz_audio.place(x=250, y=230)
        wyswietl_f0 = Button(text='wyświetl kontur F0', command=self.show_msg)
        wyswietl_f0.place(x=250, y=150)
        zapisz_f0 = Button(text='zapisz kontur F0', command=self.show_msg)
        zapisz_f0.place(x=250, y=190)
        wyswietl_emocje = Button(text='wyświetl emocje', command=self.show_msg)
        wyswietl_emocje.place(x=350, y=250)
        window.mainloop()


gui = GUI()
gui.buttons()
