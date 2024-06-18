from evaluate.split_expression import split_expression
from globals import OPERATORS, VARIABLES

def format_expression(expression):
    """
        Formats the expression to be evaluated

        args:
            expression (str): The expression to be formatted

        returns:
            formatted_expression (str): The formatted expression to be evaluated
    """

    # splitted = split_expression(expression=expression)
    if "cos" in expression:
        # print("cos is present")
        expression = expression.replace("cos", "Ĉ")
    if "sin" in expression:
        expression = expression.replace("sin", "§")
    if "tan" in expression:
        expression = expression.replace("tan", "Ť")
    if "sqrt" in expression:
        expression = expression.replace("sqrt", "√")
    if "log" in expression:
        expression = expression.replace("log", "Ł")
    if "^" in expression:
        split = split_expression(expression=expression)
        # print("split^", split)
        temp = []
        for term in split:
            if "^" in term:
                new_term = term.split("^")
                if new_term[1][0] != "(":
                    temp.append(f"{new_term[0]}^({new_term[1]})")
                else:
                    temp.append(term)
            else:
                temp.append(term)
        expression = "".join(temp)

        # print("^:", expression)



    new_text = expression
    
    temp = []
    for i, char in enumerate(new_text):
        if i == 0:
            temp.append(char)
        else:
            if char in "Ĉ§Ť√Ł" and (new_text[i - 1].isdigit() or new_text[i - 1] in VARIABLES):
                temp.append("*"+char)
            else:
                temp.append(char)

    new_text = "".join(temp)
    # print(new_text)
    return new_text
        