from numerical_integrals.midpoint.midpoint_solution import midpoint_integral
from numerical_integrals.trapezoid.trapezoid_solution import trapezoid_integral
from numerical_integrals.simpson.simpson_solution import simpson_integral
from evaluate.format import format_expression

def solve_integral(f, a, b):
    """
        Solves the integral of a given function using a specified method.

        args:
            f (function): The function to be integrated
            a (float): The lower bound of the integral
            b (float): The upper bound of the integral
            method (str): The method to be used to solve the integral

        returns:
            result (float): The result of the integral
    """

    n = int(input("Enter the number of subintervals (n): "))

    method = "simpson"

    f = format_expression(expression=f)

    if method == "midpoint":
        return midpoint_integral(f, a, b, n)
    elif method == "trapezoid":
        return trapezoid_integral(f, a, b, n)
    elif method == "simpson":
        return simpson_integral(f, a, b, n)