import tkinter as tk

win = tk.Tk()
win.title('Моят първи прозорец')
photo = tk.PhotoImage(file='icon_2.png')
win.iconphoto(True, photo)
win.geometry('600x400+600+200')
win.minsize(300, 200)
win.maxsize(800, 400)
# win.resizable(False, False)
win.config(
        bg='#CEC465',
        )
win.mainloop()

