from tkinter import *
from modules import *


def assign(entry):
    entry.config(state=NORMAL)
    entry.insert(END, " [A]->")
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
    if "x" in input:
        str_out = str(input)
        index_list = list()

        for i in range(len(str_out)):
            if str_out[i] == "+" or str_out[i] == "-":
                if i != 0:
                    index_list.append(i)
        index_list.append(len(str_out))

        term_list = list()
        for j in range(len(index_list)):
            if j == 0:
                term = str_out[0:index_list[j]]
                term_list.append(parse_term(term))
            else:
                term = str_out[index_list[j-1]:index_list[j]]
                term_list.append(parse_term(term))
        print(term_list)
        term_index_list = [i for i in range(len(term_list))]
        new_term_list = [[0., 0.]]
        while len(term_index_list) != 0:
            stan_ind = term_index_list[0]
            term_index_list.remove(stan_ind)
            for ind in term_index_list:
                if term_list[ind][1] == term_list[stan_ind][1]:
                    term_list[stan_ind][0] += term_list[ind][0]
                    term_index_list.remove(ind)

            for index, pre_ele in enumerate(new_term_list):
                if term_list[stan_ind][1] >= pre_ele[1]:
                    p_1 = new_term_list[0:index]
                    p_2 = new_term_list[index:]
                    p_1.append(term_list[stan_ind])
                    new_term_list = p_1 + p_2
                    break
        print(new_term_list)

    elif "A" in input:
        pass
    else:
        output = str(eval(input.strip()))
        clear(entry)
        entry.config(state=NORMAL)
        entry.insert(END, output)
        entry.icursor(len(entry.get()))
        entry.xview(len(entry.get()))


def derivation(entry):
    pass
