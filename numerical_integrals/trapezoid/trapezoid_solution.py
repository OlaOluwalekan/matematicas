from evaluate.evaluate_expression import evaluate_expression

def trapezoid_integral(f, a, b, n):
    """
        Integrate f(x) from a to b using the trapezoid rule.

        args:
            f (function): The function to be integrated
            a (float): The lower bound of the integral
            b (float): The upper bound of the integral
            n (int): The number of subintervals to be used

        returns:
            result (float): The value of the integral of f(x) from a to b using the trapezoid rule
    """

    h = (b - a) / n
    result = 0

    # print("INTERVAL IS:", h)
    prev = a
    fprev = evaluate_expression(f, {"x": prev})
    for i in range(1, n + 1):
        x_i = prev + h
        fx_i = evaluate_expression(f, {"x": x_i})
        result += (fprev + fx_i) / 2
        prev = x_i
        fprev = fx_i

    result = result * h

    return result
    # return (h / 2) * (f(a) + 2 * sum + f(b))