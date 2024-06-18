from evaluate.evaluate_expression import evaluate_expression

def midpoint_integral(f, a, b, n):
    """
        Integrate f(x) from a to b using the midpoint rule.

        args:
            f (function): The function to be integrated
            a (float): The lower bound of the integral
            b (float): The upper bound of the integral
            n (int): The number of subintervals to be used

        returns:
            result (float): The value of the integral of f(x) from a to b using the midpoint rule
    """

    h = (b - a) / n

    prev = 1
    result = 0
    for i in range(1, n + 1):
        x_i = 1 + h * i
        x = (prev + x_i) / 2
        prev = x_i

        res = evaluate_expression(expression=f, variables={"x": x}) * h
        result = result + res
    
    return result