import math

def operate(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    return result

def solve_expression(simplified_list):
    """
        gives the result of the simplified list of expression

        args:
            simplified_list (list): The list of components of the expression

        returns:
            result (float): The result of the expression
    """
    result_list = simplified_list.copy()

    # if "/" in result_list:

    while len(result_list) > 1 and "/" in result_list:
        # print("LIST: ", count, ":", result_list)
        indexOfOperator = result_list.index("/")
        res = operate(result_list[indexOfOperator - 1], result_list[indexOfOperator], result_list[indexOfOperator + 1])
        result_list.pop(indexOfOperator - 1)
        result_list.pop(indexOfOperator - 1)
        result_list.pop(indexOfOperator - 1)
        result_list.insert(indexOfOperator - 1, res)

    while len(result_list) > 1 and "*" in result_list:
        indexOfOperator = result_list.index("*")
        res = operate(result_list[indexOfOperator - 1], result_list[indexOfOperator], result_list[indexOfOperator + 1])
        result_list.pop(indexOfOperator - 1)
        result_list.pop(indexOfOperator - 1)
        result_list.pop(indexOfOperator - 1)
        result_list.insert(indexOfOperator - 1, res)

    while len(result_list) > 1:
        res = operate(result_list[0], result_list[1], result_list[2])
        result_list.pop(0)
        result_list.pop(0)
        result_list.pop(0)
        result_list.insert(0, res)

    # print("RES: ", result_list)
    return result_list[0]
    # for i, term in enumerate(simplified_list):
        # res = operate(term, simplified_list[i+1], simplified_list[i+2])
