import math

def solve_quadratic_equation(coefficients, variable):
    """
        Solves a quadratic equation of the form ax^2 + bx + c = 0

        args:
            coefficients (dict): The coefficients of the quadratic equation

        returns:
            roots (list): The roots of the quadratic equation
    """

    a = coefficients["a"]
    b = coefficients["b"]
    c = coefficients["c"]

    if (a == 0):
        print("Invalid quadratic equation. The coefficient of x^2 cannot be 0.")
        return

    term1 = -b / (2 * a)
    under_root = (b ** 2) - (4 * a * c)
    # print(under_root)

    if under_root < 0:
        term2 = str(math.sqrt(under_root * -1) / (2 * a)) + "i"
        x1 = f"{str(term1)}+{term2}"
        x2 = f"{str(term1)}-{term2}"
    elif under_root == 0:
        term2 = 0
        x1 = x2 = term1
    else:
        term2 = math.sqrt(under_root) / (2 * a)
        x1 = str(term1 + term2)
        x2 = str(term1 - term2)

    print(f"{variable}1 = {x1} and {variable}2 = {x2}")