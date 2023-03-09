# Въведение в TkInter - ЕТИКЕТ

import tkinter as tk

win = tk.Tk()
win.title('My first window')
win.geometry('600x400+500+100')
label_1 = tk.Label(win, text="""Hello
world!""",
                   bg='red',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   # padx=20,
                   # pady=40,
                   width=20,
                   height=10,
                   anchor='sw',
                   relief=tk.RAISED,
                   bd=5,
                   justify=tk.RIGHT,
                   )
label_1.pack()
win.mainloop()