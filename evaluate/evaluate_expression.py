from evaluate.split_expression import split_expression
from evaluate.variables import get_variables
from evaluate.simplify_expression import simplify_expression
from evaluate.solve import solve_expression
from globals import VARIABLES

def evaluate_expression(expression, variables):
    """
        Evaluates a given expression

        args:
            expression (str): The expression to be evaluated

        returns:
            result (int): The result of the expression
    """
    # print(expression)

    # print("EVALUATING EXPRESSION")

    # GET THE LIST OF VARIABLES
    # variables = get_variables(expression=expression)

    temp = []
    for i, char in enumerate(expression):
        # prevChar = expression[i - 1]
        # print("CHAIN:", char, prevChar)
        if (i != 0 and char == "(" and expression[i - 1].isdigit()) or (i != 0 and char == "(" and expression[i - 1] == ")") or i != 0 and char == "(" and expression[i - 1] in VARIABLES:
            # print("before: ", expression[i - 1])
            newChar = "*("
            temp.append(newChar)
        else:
            temp.append(char)

    expression = "".join(temp)


    while "(" in expression and ")" in expression:
        startIndex = expression.index("(")
        # print("before brackets: ", expression[startIndex], expression[startIndex - 1])
        endIndex = expression.index(")")
        tempExp = expression[startIndex + 1: endIndex]
        # print(tempExp)
        exp_comp = split_expression(expression=tempExp)
        vars = variables
        simp_list = simplify_expression(expression_list=exp_comp, variables=vars)
        expression = expression[:startIndex] + str(solve_expression(simplified_list=simp_list)) + expression[endIndex + 1:]
        # expression = expression[:startIndex] + tempExp + expression[endIndex + 1:]

    # print(expression)

    # SPLIT EXPRESSION INTO COMPONENTS
    expression_components = split_expression(expression=expression)
    # print(expression_components)

    # SIMPLIFY THE LIST OF EXPRESSION COMPONENTS
    simplified_list = simplify_expression(expression_list=expression_components, variables=variables)
    # print(simplified_list)

    # SOLVE THE SIMPLIFIED LIST
    result = solve_expression(simplified_list=simplified_list)
    # print(result)
    return result
    
        