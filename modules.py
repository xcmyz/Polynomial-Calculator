import math


# Parse Term
def parse_term(term: str):
    if term != "":
        if "X" in term:
            a = 0.
            b = 0.
            ind_x = term.index("X")
            p_f = term[0:ind_x]
            p_s = term[ind_x+1:]
            if p_f == "":
                a = 1.
            elif p_f == "+":
                a = 1.
            elif p_f == "-":
                a = -1.
            else:
                a = float(p_f)
            if p_s == "":
                b = 1.
            else:
                b = float(p_s[1:len(p_s)-1])

            return [a, b]
        else:
            print(term)
            return [float(term), 0.]
    else:
        return [0., 0.]


# Parse String
def parse_input(str_out):
    index_X_list = list()
    for i in range(len(str_out)):
        if str_out[i] == "+" or str_out[i] == "-":
            index_X_list.append(i)

    index_bra_list = list()
    for i in range(len(str_out)):
        if str_out[i] == "(" or str_out[i] == ")":
            index_bra_list.append(i)

    for i in range(len(index_bra_list) // 2):
        for ele in index_X_list:
            if ele > index_bra_list[2*i] and ele < index_bra_list[2*i+1]:
                index_X_list.remove(ele)

    term_list = list()
    index_X_list.append(len(str_out))
    for j in range(len(index_X_list)):
        if j == 0:
            term = str_out[0:index_X_list[j]]
            term_list.append(parse_term(term))
        else:
            term = str_out[index_X_list[j-1]:index_X_list[j]]
            term_list.append(parse_term(term))

    return term_list


# Sort
def reprocess(term_list):
    term_index_list = [i for i in range(len(term_list))]
    new_term_list = [[0., 0.]]
    while len(term_index_list) != 0:
        stan_ind = term_index_list[0]
        term_index_list.remove(stan_ind)
        copy = list(term_index_list)
        for ind in copy:
            if term_list[ind][1] == term_list[stan_ind][1]:
                term_list[stan_ind][0] += term_list[ind][0]
                term_index_list.remove(ind)

        for index, pre_ele in enumerate(new_term_list):
            if index == len(new_term_list)-1 and (term_list[stan_ind][1] < pre_ele[1]):
                new_term_list.append(term_list[stan_ind])
                break

            if term_list[stan_ind][1] >= pre_ele[1]:
                p_1 = new_term_list[0:index]
                p_2 = new_term_list[index:]
                p_1.append(term_list[stan_ind])
                new_term_list = p_1 + p_2
                break

    t_copy = list(new_term_list)
    for term in t_copy:
        if term[0] == 0.:
            new_term_list.remove(term)

    return new_term_list


def draw_P(term_list):
    str_out = ""
    if len(term_list) == 0:
        return "0"
    for term in term_list:
        temp = ""
        if term[0] >= 0.:
            if term[0] == 1.:
                temp += "+"
                if term[1] == 0.:
                    temp += "1"
            else:
                temp += "+" + str(term[0])
        else:
            if term[0] == -1.:
                temp += "-"
                if term[1] == 0.:
                    temp += "1"
            else:
                temp += str(term[0])

        if term[1] != 0.:
            if term[1] == 1.:
                temp += "X"
            else:
                temp += "X("
                temp += str(term[1])
                temp += ")"

        str_out += temp

    if str_out[0] == "+":
        str_out = str_out[1:]

    return str_out


def get_value(new_term_list, a_v):
    value = 0.
    for [a, b] in new_term_list:
        value += a * math.pow(a_v, b)

    return value
