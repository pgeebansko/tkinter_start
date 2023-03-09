import tkinter as tk

win = tk.Tk()
win.geometry("600x400+100+200")
win.title('Grid in TkInter')

button_1 = tk.Button(win, text='button 1')
button_2 = tk.Button(win, text='button 2')
button_3 = tk.Button(win, text='button 3')
button_4 = tk.Button(win, text='button 4')
button_5 = tk.Button(win, text='button 5')

button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=1, column=0)
button_4.grid(row=1, column=1)
button_5.grid(row=4, column=0, columnspan=2, stick='ew')

win.mainloop()