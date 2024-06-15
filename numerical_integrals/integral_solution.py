from numerical_integrals.midpoint.midpoint_solution import midpoint_integral

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

    method = "midpoint"

    if method == "midpoint":
        return midpoint_integral(f, a, b, 3)