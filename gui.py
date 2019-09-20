from tkinter import *
import tkinter.font as tkFont
import os
from functools import partial
from PIL import Image, ImageTk


def get_input(entry, argu):
    entry.insert(END, argu)


def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)


def clear(entry):
    entry.delete(0, END)


def calc(entry):
    input = entry.get()
    output = str(eval(input.strip()))
    clear(entry)
    entry.insert(END, output)


def cal():
    root = Tk()
    root.title("lzx")
    root.resizable(0, 0)

    entry_font = tkFont.Font(size=36)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4, sticky=N+W+S+E,
               ipadx=5, ipady=5, padx=5, pady=5)

    button_bg = '#D5E0EE'
    button_active_bg = '#E5E35B'

    myButton = partial(Button, root, bg=button_bg, padx=12,
                       pady=3, activebackground=button_active_bg)

    button7 = myButton(text='7', command=lambda: get_input(entry, '7'))
    button7.grid(row=1, column=0, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button8 = myButton(text='8', command=lambda: get_input(entry, '8'))
    button8.grid(row=1, column=1, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button9 = myButton(text='9', command=lambda: get_input(entry, '9'))
    button9.grid(row=1, column=2, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button10 = myButton(text='+', command=lambda: get_input(entry, '+'))
    button10.grid(row=1, column=3, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button4 = myButton(text='4', command=lambda: get_input(entry, '4'))
    button4.grid(row=2, column=0, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button5 = myButton(text='5', command=lambda: get_input(entry, '5'))
    button5.grid(row=2, column=1, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button6 = myButton(text='6', command=lambda: get_input(entry, '6'))
    button6.grid(row=2, column=2, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button11 = myButton(text='-', command=lambda: get_input(entry, '-'))
    button11.grid(row=2, column=3, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button1 = myButton(text='1', command=lambda: get_input(entry, '1'))
    button1.grid(row=3, column=0, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button2 = myButton(text='2', command=lambda: get_input(entry, '2'))
    button2.grid(row=3, column=1, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button3 = myButton(text='3', command=lambda: get_input(entry, '3'))
    button3.grid(row=3, column=2, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    buttonx = myButton(text='x', command=lambda: get_input(entry, 'x'))
    buttonx.grid(row=4, column=1, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button0 = myButton(text='0', command=lambda: get_input(entry, '0'))
    button0.grid(row=4, column=0, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button13 = myButton(text='.', command=lambda: get_input(entry, '.'))
    button13.grid(row=4, column=2, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button15 = Button(root, text='<', bg=button_bg, padx=10, pady=3,
                      command=lambda: backspace(entry), activebackground=button_active_bg)
    button15.grid(row=5, column=0, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button16 = Button(root, text='C', bg=button_bg, padx=10, pady=3,
                      command=lambda: clear(entry), activebackground=button_active_bg)
    button16.grid(row=5, column=1, ipadx=5, ipady=5, pady=5, sticky=N+W+S+E)

    button17 = Button(root, text='=', bg=button_bg, padx=10, pady=3,
                      command=lambda: calc(entry), activebackground=button_active_bg)
    button17.grid(row=5, column=2, columnspan=2,
                  padx=3, pady=5, ipadx=5, ipady=5, sticky=N+S+E+W)

    root.mainloop()


if __name__ == '__main__':
    cal()
