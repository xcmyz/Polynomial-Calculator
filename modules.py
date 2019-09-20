def parse_term(term: str):
    if "x" in term:
        ind_x = term.index("x")
        if ind_x == len(term)-1:
            return [float(term[0:ind_x]), 1.]
        elif ind_x == 1 and (term[0] == "+" or term[0] == "-"):
            if term[0] == "+":
                return [1., float(term[1:])]
            else:
                return [-1., float(term[1:])]
        else:
            return [float(term[0:ind_x]), float(term[ind_x+1:])]
    else:
        return [float(term), 0]
