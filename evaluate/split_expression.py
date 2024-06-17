from globals import OPERATORS

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
                    if expression[i - 1] not in OPERATORS:
                        new_char = "~" + character + "~"
                        temp.append(new_char)
                    else:
                        temp.append(character)
                    # new_char = "~" + character + "~"
                    # temp.append(new_char)
                else:
                    temp.append("-1~*~")
            else:
                temp.append(character)
    
    temp = "".join(temp)
    expression_components = temp.split("~")
    # print("TEMPO:", temp)

    return expression_components