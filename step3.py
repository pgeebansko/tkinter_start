import tkinter as tk


def new_label():
    global number
    number += 1
    label = tk.Label(win, text=f'new label #{number}')
    label.pack()


number = 0


win = tk.Tk()
win.geometry("600x400+100+200")
win.title('Buttons in TkInter')
button_1 = tk.Button(win, text='Hello!',
                     command=new_label)
button_1.pack()

win.mainloop()