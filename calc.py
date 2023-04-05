import tkinter as tk

value = '0'
expr = '0'


def show_results():
    global value
    results['text'] = value


def show_epr():
    global expr
    expression['text'] = expr


def compute():
    global value
    a = eval(value)
    value = str(a)
    show_results()


def add_digit(d):
    global value, to_clear
    if value == '0' or to_clear:
        value = d
    else:
        value += d
    show_results()
    print('new digit ', d)
    to_clear = False


def add_action(a):
    if a in {'+', '-', '*', '/'}:
        print('sign')
    else:
        print('digit')


def clear():
    global value
    value = '0'
    show_results()


def convert_to_binary():
    global value, to_clear
    print(value)
    d = int(value)
    b = ''
    print(d, b)
    while d > 0:
        if (d % 2) == 1:
            b = '1' + b
        else:
            b = '0' + b
        d = int(d / 2)
        print('d=', d, 'b=', b)
    value = b
    results['text'] = value
    to_clear = True


to_clear = False
win = tk.Tk()
win.title('Калкулатор')
win.geometry('320x450+600+200')


win.grid_columnconfigure(0, minsize=80)
win.grid_columnconfigure(1, minsize=80)
win.grid_columnconfigure(2, minsize=80)
win.grid_columnconfigure(3, minsize=80)

win.grid_rowconfigure(0, minsize=30)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)
win.grid_rowconfigure(6, minsize=60)
win.grid_rowconfigure(7, minsize=60)

expression = tk.Label(win, text='0', anchor='e', font=('Ariel', 12, 'normal'), fg='gray')
expression.grid(row=0, column=0, sticky='ew', columnspan=4, )

results = tk.Label(win, text='0', anchor='e', font=('Ariel', 25, 'bold'))
results.grid(row=1, column=0, sticky='ew', columnspan=4, )

btn_prc = tk.Button(win, text='to BIN', command=convert_to_binary).grid(row=2, column=0, sticky='wens')
btn_CE = tk.Button(win, text='CE').grid(row=2, column=1, sticky='wens')
btn_C = tk.Button(win, text='C', command=clear).grid(row=2, column=2, sticky='wens')
btn_bsp = tk.Button(win, text='BackSpace').grid(row=2, column=3, sticky='wens')
btn_rec = tk.Button(win, text='1/x').grid(row=3, column=0, sticky='wens')
btn_pwr = tk.Button(win, text='x**2').grid(row=3, column=1, sticky='wens')
btn_sqr = tk.Button(win, text='**-2').grid(row=3, column=2, sticky='wens')
btn_div = tk.Button(win, text='/', command=lambda: add_action('/')).grid(row=3, column=3, sticky='wens')
btn_7 = tk.Button(win, text='7', command=lambda: add_digit('7')).grid(row=4, column=0, sticky='wens')
btn_8 = tk.Button(win, text='8', command=lambda: add_digit('8')).grid(row=4, column=1, sticky='wens')
btn_9 = tk.Button(win, text='9', command=lambda: add_digit('9')).grid(row=4, column=2, sticky='wens')
btn_mul = tk.Button(win, text='x', command=lambda: add_action('*')).grid(row=4, column=3, sticky='wens')
btn_4 = tk.Button(win, text='4', command=lambda: add_digit('4')).grid(row=5, column=0, sticky='wens')
btn_5 = tk.Button(win, text='5', command=lambda: add_digit('5')).grid(row=5, column=1, sticky='wens')
btn_6 = tk.Button(win, text='6', command=lambda: add_digit('6')).grid(row=5, column=2, sticky='wens')
btn_sub = tk.Button(win, text='-', command=lambda: add_action('-')).grid(row=5, column=3, sticky='wens')
btn_1 = tk.Button(win, text='1', command=lambda: add_digit('1')).grid(row=6, column=0, sticky='wens')
btn_2 = tk.Button(win, text='2', command=lambda: add_digit('2')).grid(row=6, column=1, sticky='wens')
btn_3 = tk.Button(win, text='3', command=lambda: add_digit('3')).grid(row=6, column=2, sticky='wens')
btn_add = tk.Button(win, text='+', command=lambda: add_action('+')).grid(row=6, column=3, sticky='wens')
btn_sgn = tk.Button(win, text='+/-').grid(row=7, column=0, sticky='wens')
btn_0 = tk.Button(win, text='0').grid(row=7, column=1, sticky='wens')
btn_dot = tk.Button(win, text='.').grid(row=7, column=2, sticky='wens')
tk.Button(win, text='=', command=compute).grid(row=7, column=3, sticky='wens')
win.mainloop()
