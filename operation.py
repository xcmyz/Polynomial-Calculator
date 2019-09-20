from tkinter import *
from modules import *


def assign(entry):
    entry.config(state=NORMAL)
    entry.insert(END, " [A]: ")
    entry.icursor(len(entry.get()))
    entry.xview(len(entry.get()))


def get_input(entry, argu):
    entry.config(state=NORMAL)
    entry.insert(END, argu)
    entry.icursor(len(entry.get()))
    entry.xview(len(entry.get()))


def backspace(entry):
    entry.config(state=NORMAL)
    input_len = len(entry.get())
    entry.delete(input_len - 1)


def clear(entry):
    entry.config(state=NORMAL)
    entry.delete(0, END)


def cal(entry):
    entry.config(state=NORMAL)
    input = entry.get()
    if "X" in input and "A" not in input:
        str_out = str(input)
        term_list = parse_input(str_out)
        print(term_list)
        new_term_list = reprocess(term_list)
        print(new_term_list)
        str_P = draw_P(new_term_list)
        print(str_P)

        clear(entry)
        entry.insert(END, str_P)
        entry.icursor(len(entry.get()))
        entry.xview(len(entry.get()))
    elif "A" in input:
        str_out = input[0:input.index("A")-2]
        a_v = float(input[input.index("A")+4:])
        term_list = parse_input(str_out)
        print(term_list)
        new_term_list = reprocess(term_list)
        print(new_term_list)

        value = get_value(new_term_list, a_v)
        clear(entry)
        entry.insert(END, str(value))
        entry.icursor(len(entry.get()))
        entry.xview(len(entry.get()))
    else:
        output = str(eval(input.strip()))
        clear(entry)
        entry.config(state=NORMAL)
        entry.insert(END, output)
        entry.icursor(len(entry.get()))
        entry.xview(len(entry.get()))


def derivation(entry):
    pass
