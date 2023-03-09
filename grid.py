import  tkinter as tk


win = tk.Tk()
win.geometry('600x400+500+200')
win.title('tkinter widget grid')

lbl1 = tk.Label(win, text='**********************')
btn1 = tk.Button(win, text='бутон 1')
btn2 = tk.Button(win, text='бутон 2')
btn3 = tk.Button(win, text='бутон 3')
btn4 = tk.Button(win, text='бутон 4')
btn5 = tk.Button(win, text='бутон 5')
btn6 = tk.Button(win, text='бутон 6')

lbl1.grid(row=0, column=0, columnspan=3, stick='ew')
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=2, column=0)
btn4.grid(row=2, column=1)
btn5.grid(row=2, column=0, columnspan=2, stick='ew')
btn6.grid(row=1, column=2, rowspan=3, sticky='sn')

win.mainloop()