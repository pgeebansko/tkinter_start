import tkinter as tk

counter = 0


def increment():
    global counter
    counter += 1
    label_1['text'] = f'Брояч: {counter}'


win = tk.Tk()
win.title('TkInter Labels demo')
win.geometry('600x300+500+200')


label_1 = tk.Label(win, text=f'Брояч: {counter}')
label_1.pack()


button_plus = tk.Button(win,
                        text='Increment counter',
                        background='blue',
                        activebackground='red',
                        foreground='yellow',
                        activeforeground='lime',
                        command=increment)
button_plus.pack()

win.mainloop()