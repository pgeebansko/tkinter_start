# Въведение в TkInter

import tkinter as tk

win = tk.Tk()
photo = tk.PhotoImage(file='icon1.png')
win.iconphoto(False, photo)
win.config(bg='#ECE75B',

           )
win.title('My first window')
win.geometry('600x400+500+100')
win.minsize(400,200)
win.maxsize(800,400)
win.resizable(True, True)

win.mainloop()