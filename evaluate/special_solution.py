import math

def solve_special_cases(term, symbol):
    """
        Solves special cases of the expression like trigonometry, logarithms and exponential

        args:
            term (str): The term to be solved

        returns:
            term (float): The solved term
    """

    angle = math.radians(float(term))

    if symbol == "Ĉ":
        return math.cos(angle)
    elif symbol == "§":
        return math.sin(angle)
    elif symbol == "Ť":
        return math.tan(angle)
    
    