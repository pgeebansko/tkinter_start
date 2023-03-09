# Въведение в TkInter - ЕТИКЕТ

import tkinter as tk

win = tk.Tk()
win.title('My first window')
win.geometry('600x400+500+100')
multirowtext = """Това
е
текст
на много редове
"""
label_1 = tk.Label(win, text=multirowtext,
                   bg='blue',
                   fg='yellow',
                   font=('Arial', 30, 'italic'),
                   height=30,
                   width=50,
                   padx=10,
                   pady=10,
                   anchor='center',
                   justify=tk.CENTER
                   )

label_1.pack()
win.mainloop()