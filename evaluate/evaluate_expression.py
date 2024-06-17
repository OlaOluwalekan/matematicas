from evaluate.split_expression import split_expression
from evaluate.variables import get_variables
from evaluate.simplify_expression import simplify_expression
from evaluate.solve import solve_expression
from globals import VARIABLES, OPERATORS

def evaluate_expression(expression, variables):
    """
        Evaluates a given expression

        args:
            expression (str): The expression to be evaluated

        returns:
            result (int): The result of the expression
    """

    # (i != 0 and char == "(" and expression[i - 1].isdigit()) or (i != 0 and char == "(" and expression[i - 1] == ")") or (i != 0 and char == "(" and expression[i - 1] in VARIABLES) or (i != 0 and char == "(" and expression[i - 1] == "(")

    temp = []
    for i, char in enumerate(expression):
        # EXPLICITLY ADD "*" TO INDICATE MULTIPLICATION WHERE WE HAVE PARENTHESIS
        if i == 0:
            temp.append(char)
        else:
            if char == "(":
                if expression[i - 1].isdigit() or expression[i - 1] == ")" or expression[i - 1] in VARIABLES:
                    newChar = "*("
                    temp.append(newChar)
                else:
                    temp.append(char)
            else:
                if char in OPERATORS or char == ")":
                    temp.append(char)
                else:
                    if expression[i - 1] == ")":
                        newChar = "*" + char
                        temp.append(newChar)
                    else:
                        temp.append(char)

    expression = "".join(temp)
    # print(expression)

# 6-(2x-5(x+7))(1-2x)/8


    # SIMPLIFY BRACKETS
    while "(" in expression and ")" in expression:
        start = None
        for i, char in enumerate(expression):
            if char == "(":
                start = i
            elif char == ")":
                if start != None:
                    inner_expression = expression[start + 1: i]
                    res = evaluate_expression(inner_expression, variables)
                    # exp_com = split_expression(expression=inner_expression)
                    # sim_lis = simplify_expression(expression_list=exp_com, variables=variables)
                    # res = solve_expression(simplified_list=sim_lis)
                    expression = expression[:start] + str(res) + expression[i + 1:]
                    break

    # print(expression)

    # SPLIT EXPRESSION INTO COMPONENTS
    expression_components = split_expression(expression=expression)
    # print(expression_components)

    # SIMPLIFY THE LIST OF EXPRESSION COMPONENTS
    simplified_list = simplify_expression(expression_list=expression_components, variables=variables)
    # print("SIMPLE:", simplified_list)

    # SOLVE THE SIMPLIFIED LIST
    result = solve_expression(simplified_list=simplified_list)
    # print(result)
    # return expression_components
    return result
    
    # 2x – 3xy + 9y – 7y + 8
        