from evaluate.evaluate_expression import evaluate_expression

def simpson_integral(f, a, b, n):
    """
        integrate f(x) from a to b using the simpson rule.

        args:
            f (function): The function to be integrated
            a (float): The lower bound of the integral
            b (float): The upper bound of the integral
            n (int): The number of subintervals to be used

        returns:
            result (float): The value of the integral of f(x) from a to b using the simpson's rule
    """

    h = (b - a) / n

    # print(h)

    result = 0

    for i in range(0, n + 1):
        x_i = a + i * h
        # print(f"x_{i} = {x_i}")
        fx_i = evaluate_expression(f, {"x": x_i})
        if i == 0 or i == n:
            result += fx_i
        elif i % 2 == 0:
            result += 2 * fx_i
        else:
            result += 4 * fx_i

    # print(f"RESULT: {result}")

    result *= (h / 3)

    return result
