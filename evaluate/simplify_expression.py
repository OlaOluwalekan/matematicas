from globals import OPERATORS, VARIABLES
from evaluate.special_solution import solve_special_cases

def solve_term(term, variables):
    temp = []
    # SPLIT EACH TERM INTO COMPONENTS EG: 2x INTO 2 AND x
    for i, t in enumerate(term):
        if t in VARIABLES:
            new_t = "~" + t + "~"
            temp.append(new_t)
        else:
            temp.append(t)
    temp = "".join(temp).split("~")
    
    product = 1
    # SUBSTITUTE THE VALUE OF THE VARIABLES IN THE TERM AND SIMPLIFY TO DIGIT
    for char in temp:
        if char == "":
            product = product * 1
        elif char in VARIABLES:
            product = product * variables[char]
        else:
            product = product * float(char)
    
    return product

def simplify_expression(expression_list, variables):
    """
        simplify the list of expression into a simple list of numbers and operators

        args:
            expression_list (list): The list of expression to be simplified
            variables (dictionary): key value pair of variables and their values
        
        returns:
            simplified_list (list): a simplified list of numbers and operators
    """

    simplified_list = []

    for term in expression_list:
        if term not in OPERATORS:
            if "Ĉ" in term or "§" in term or "Ť" in term or "√" in term or "Ł" in term:
                symbol = term[0]
                new_term = term.replace(symbol, "")
                solution = solve_special_cases(new_term, symbol)
                simplified_list.append(solution)
            else:
                if "^" in term:
                    term_split = term.split("^")
                    power = float(term_split[1])
                    if set(VARIABLES) & set(term_split[0]):
                        base = term_split[0][-1]
                        base = variables[base]
                        exp = base ** power
                        rest = term_split[0][:-1]
                        prod = solve_term(rest, variables) * exp
                    else:
                        prod = float(term_split[0]) ** power
                    simplified_list.append(prod)
                else:
                    product = solve_term(term, variables)
                    simplified_list.append(product)
        else:
            simplified_list.append(term)

    return simplified_list

# x-tan(40)y+xcos(60)-ysin(20)