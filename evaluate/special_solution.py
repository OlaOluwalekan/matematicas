import math

def solve_special_cases(term, symbol, angle_unit="r"):
    """
        Solves special cases of the expression like trigonometry, logarithms and exponential

        args:
            term (str): The term to be solved

        returns:
            term (float): The solved term
    """
    if angle_unit == "r":
        angle = math.radians(float(term))
    elif angle_unit == "d":
        angle = term

    if symbol == "Ĉ":
        return math.cos(angle)
    elif symbol == "§":
        return math.sin(angle)
    elif symbol == "Ť":
        return math.tan(angle)
    elif symbol == "√":
        return math.sqrt(float(term))
    elif symbol == "Ł":
        return math.log10(float(term))
    
    