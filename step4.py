import tkinter as tk


def plus():
    global number
    number += 1
    label_counter['text'] = f'Броячът има стойност {number}'

def minus():
    global number
    number -= 1
    label_counter['text'] = f'Броячът има стойност {number}'


number = 0


win = tk.Tk()
win.geometry("600x400+100+200")
win.title('Buttons in TkInter')

label_counter = tk.Label(win,
                         text=f'Броячът има стойност {number}',
                         )
label_counter.pack()

button_inc = tk.Button(win,
                       text='+',
                       command=plus,
                       width=10,
                       bg='blue',
                       activebackground='red')
button_inc.pack()
button_dec = tk.Button(win,
                       text='-',
                       command=minus,width=10,
                       background='blue',
                       activebackground='red')
button_dec.pack()

win.mainloop()