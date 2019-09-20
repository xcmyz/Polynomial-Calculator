from tkinter import *
from operation import *
import tkinter.font as tkFont
import os
from functools import partial


def show():
    root = Tk()
    root.title("Polynomial Calculator --XCMYZ")
    root.resizable(0, 0)

    button_bg = '#8EC5D8'
    button_active_bg = '#144455'

    entry_font = tkFont.Font(size=25)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4, sticky=N+W+S+E,
               ipadx=5, ipady=7, padx=5, pady=5)

    myButton = partial(Button, root, bg=button_bg, padx=12,
                       pady=3, activebackground=button_active_bg)

    buttonx = myButton(text='X', command=lambda: get_input(entry, 'X'))
    buttonx.grid(row=4, column=2, ipadx=5, ipady=7,
                 padx=3, pady=5, sticky=N+W+S+E)

    button0 = myButton(text='0', command=lambda: get_input(entry, '0'))
    button0.grid(row=4, column=1, ipadx=5, ipady=7,
                 padx=3, pady=5, sticky=N+W+S+E)

    button1 = myButton(text='1', command=lambda: get_input(entry, '1'))
    button1.grid(row=3, column=0, ipadx=5, ipady=7,
                 padx=3, pady=5, sticky=N+W+S+E)

    button2 = myButton(text='2', command=lambda: get_input(entry, '2'))
    button2.grid(row=3, column=1, ipadx=5, ipady=7,
                 padx=3, pady=5, sticky=N+W+S+E)

    button3 = myButton(text='3', command=lambda: get_input(entry, '3'))
    button3.grid(row=3, column=2, ipadx=5, ipady=7,
                 padx=3, pady=5, sticky=N+W+S+E)

    button4 = myButton(text='4', command=lambda: get_input(entry, '4'))
    button4.grid(row=2, column=0, ipadx=5, ipady=7,
                 padx=3, pady=5, sticky=N+W+S+E)

    button5 = myButton(text='5', command=lambda: get_input(entry, '5'))
    button5.grid(row=2, column=1, ipadx=5, ipady=7,
                 padx=3, pady=5, sticky=N+W+S+E)

    button6 = myButton(text='6', command=lambda: get_input(entry, '6'))
    button6.grid(row=2, column=2, ipadx=5, ipady=7,
                 padx=3, pady=5, sticky=N+W+S+E)

    button7 = myButton(text='7', command=lambda: get_input(entry, '7'))
    button7.grid(row=1, column=0, ipadx=5, ipady=7,
                 padx=3, pady=5, sticky=N+W+S+E)

    button8 = myButton(text='8', command=lambda: get_input(entry, '8'))
    button8.grid(row=1, column=1, ipadx=5, ipady=7,
                 padx=3, pady=5, sticky=N+W+S+E)

    button9 = myButton(text='9', command=lambda: get_input(entry, '9'))
    button9.grid(row=1, column=2, ipadx=5, ipady=7,
                 padx=3, pady=5, sticky=N+W+S+E)

    buttonadd = myButton(text='+', command=lambda: get_input(entry, '+'))
    buttonadd.grid(row=1, column=3, ipadx=5, ipady=7,
                   padx=3, pady=5, sticky=N+W+S+E)

    buttonsub = myButton(text='-', command=lambda: get_input(entry, '-'))
    buttonsub.grid(row=2, column=3, ipadx=5, ipady=7,
                   padx=3, pady=5, sticky=N+W+S+E)

    buttonpoint = myButton(text='.', command=lambda: get_input(entry, '.'))
    buttonpoint.grid(row=4, column=0, ipadx=5, ipady=7,
                     padx=3, pady=5, sticky=N+W+S+E)

    buttondelete = Button(root, text='<-', bg=button_bg, padx=10, pady=3,
                          command=lambda: backspace(entry), activebackground=button_active_bg)
    buttondelete.grid(row=6, column=0, columnspan=1, ipadx=5, ipady=7,
                      padx=3, pady=5, sticky=N+W+S+E)

    buttonclear = Button(root, text='C', bg=button_bg, padx=10, pady=3,
                         command=lambda: clear(entry), activebackground=button_active_bg)
    buttonclear.grid(row=5, column=2, columnspan=2, ipadx=5, ipady=7,
                     padx=3, pady=5, sticky=N+W+S+E)

    buttonassign = myButton(text='A', command=lambda: assign(entry))
    buttonassign.grid(row=3, column=3, ipadx=5, ipady=7,
                      padx=3, pady=5, sticky=N+W+S+E)

    buttonlbra = Button(root, text='(', bg=button_bg, padx=10, pady=3, command=lambda: get_input(
        entry, '('), activebackground=button_active_bg)
    buttonlbra.grid(row=5, column=0, columnspan=1,
                    padx=3, pady=5, ipadx=5, ipady=7, sticky=N+S+E+W)

    buttonrbra = Button(root, text=')', bg=button_bg, padx=10, pady=3, command=lambda: get_input(
        entry, ')'), activebackground=button_active_bg)
    buttonrbra.grid(row=5, column=1, columnspan=1,
                    padx=3, pady=5, ipadx=5, ipady=7, sticky=N+S+E+W)

    buttonequal = Button(root, text='=', bg=button_bg, padx=10, pady=3,
                         command=lambda: cal(entry), activebackground=button_active_bg)
    buttonequal.grid(row=6, column=1, columnspan=3,
                     padx=3, pady=5, ipadx=5, ipady=7, sticky=N+S+E+W)

    buttonderivation = Button(root, text='D', bg=button_bg, padx=10, pady=3,
                              command=lambda: derivation(entry), activebackground=button_active_bg)
    buttonderivation.grid(row=4, column=3, columnspan=1,
                          padx=3, pady=5, ipadx=5, ipady=7, sticky=N+S+E+W)

    root.mainloop()
