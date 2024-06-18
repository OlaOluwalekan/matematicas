from globals import OPERATORS, VARIABLES
from evaluate.simplify_expression import simplify_expression
from evaluate.solve import solve_expression

def split_expression(expression):
    """
        splits an string in the form of mathematical expression into a list

        args:
            expression (str): The expression to be splitted

        returns:
            expression_components (list): The list of components of the expression
    """

    expression_components = []
    temp = []
    for i, character in enumerate(expression):
        if character != " ":
            if character in OPERATORS:
                if i != 0:
                    # print(character, "prev is", expression[i - 1] in OPERATORS)
                    if expression[i - 1] in OPERATORS:
                        temp.append(character)
                    else:
                        if expression[i - 1] == "^":
                            temp.append(character)
                        else:
                            new_char = "~" + character + "~"
                            temp.append(new_char)
                    # new_char = "~" + character + "~"
                    # temp.append(new_char)
                else:
                    temp.append("-1~*~")
            else:
                temp.append(character)
    
    temp = "".join(temp)
    
    expression_components = temp.split("~")

    # print("test_exp_comp: ", expression_components)

    # new_temp = []
    # for term in expression_components:
    #     if "^" in term:
    #         new_term = term.split("^")
    #         print("TERM", new_term)
    #         # if set(VARIABLES) & set(new_term[0]):
    #         #     last_in_term = new_term[0][-1]
    #         #     # new_char = new_term[0].replace(last_in_term, last_in_term*int(new_term[1]))
    #         #     new_char = new_term[0].replace(last_in_term, "2")
    #         #     new_temp.append(new_char)
    #         # else:
    #         #     new_char = int(new_term[0]) ** int(new_term[1])
    #         #     new_temp.append(new_char)
    #         new_temp.append(term)
    #     else:
    #         new_temp.append(term)

    # expression_components = new_temp

    # print("TEMPO:", temp)

    return expression_components