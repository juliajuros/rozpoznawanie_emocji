from tkinter import *
from tkinter import messagebox
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import pyaudio


class Audio:


    def znajdz_audio(self):
        filetypes = ['*.wav', "*.mp3", "*.flac", "*.m4a"]
        file = filedialog.askopenfilename(filetypes=[("Audio files", filetypes)])
        if file:
            print(file)
            # openfile tu pewnie
            # content = file.read()
            # file.close()
            # print("%d characters in this file" % len(content))


# class F0:

# class Klasyfikacja:


class GUI:

    def __init__(self):
        self.rozpocznij_nagrywanie = False
        self.audio = pyaudio.PyAudio()
        self.p = pyaudio.PyAudio()
        self.frames = []
        self.window = Tk()
        self.window.geometry("900x500")

        self.aud = Audio()
        self.wprowadz_audio = Button(text='wprowadź audio', command=self.aud.znajdz_audio)
        self.wprowadz_audio.place(x=50, y=60)
        self.rozpocznij_nagrywanie = Button(text='rozpocznij nagrywanie',  command= self.nagraj_audio)
        self.rozpocznij_nagrywanie.place(x=50, y=120)
        self.zakoncz_nagrywanie = Button(text='zakończ nagrywanie', command= self.zakoncz_audio)
        self.zakoncz_nagrywanie.place(x=50, y=150)
        self.wyswietl_f0 = Button(text='wyświetl kontur F0', command=self.show_msg)
        self.wyswietl_f0.place(x=250, y=150)
        self.zapisz_f0 = Button(text='zapisz kontur F0', command=self.show_msg)
        self.zapisz_f0.place(x=250, y=190)
        self.zapisz_audio = Button(text='zapisz audio', command=self.show_msg)
        self.zapisz_audio.place(x=250, y=230)
        self.window.mainloop()


    def nagraj_audio(self):
        self.rozpocznij_nagrywanie = True
        stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                                      frames_per_buffer=1024)
        self.frames = []
        while self.rozpocznij_nagrywanie == True:
            data = stream.read(1024)
            self.frames.append(data)
            # print(len(self.frames))

        stream.stop_stream()
        stream.close()
        self.audio.terminate()

    def zakoncz_audio(self):
        self.rozpocznij_nagrywanie = False
        print("koniec dupy")

    def show_msg(self):
        messagebox.showinfo("Message", "Hey There! I hope you are doing well.") # do wywalenia

    def buttons(self):
        window = Tk()
        window.geometry("900x500")

        audio = Audio()
        wprowadz_audio = Button(text='wprowadź audio', command=audio.znajdz_audio)
        wprowadz_audio.place(x=50, y=60)
        rozpocznij_nagrywanie = Button(text='rozpocznij nagrywanie',  command= self.nagraj_audio)
        rozpocznij_nagrywanie.place(x=50, y=120)
        zakoncz_nagrywanie = Button(text='zakończ nagrywanie', command= self.zakoncz_audio)
        zakoncz_nagrywanie.place(x=50, y=150)
        wyswietl_f0 = Button(text='wyświetl kontur F0', command=self.show_msg)
        wyswietl_f0.place(x=250, y=150)
        zapisz_f0 = Button(text='zapisz kontur F0', command=self.show_msg)
        zapisz_f0.place(x=250, y=190)
        zapisz_audio = Button(text='zapisz audio', command=self.show_msg)
        zapisz_audio.place(x=250, y=230)
        window.mainloop()


gui = GUI()
# gui.buttons()