from main_options import print_main_options
from evaluate.evaluate_expression import evaluate_expression
from evaluate.input_expression import input_expression
from numerical_integrals.intervals import get_intervals
from numerical_integrals.integral_solution import solve_integral
from evaluate.variables import get_variables
from quadratic.quadratic import solve_quadratic_equation
from quadratic.quadratic_expression import get_quadratic_expression
from evaluate.format import format_expression

print("WELCOME TO MATEMATICAS")

main_choice = print_main_options()

if main_choice == 1:
    expression = input_expression()
    expression = format_expression(expression=expression)
    variables = get_variables(expression=expression)
    result = evaluate_expression(expression=expression, variables=variables)
    print("RESULT: ", result)
elif main_choice == 2:
    print("SOLVING FOR UNKNOWN VARIABLES")
    res = get_quadratic_expression()
    coefficients = res["coefficients"]
    unknown = res["unknown"]
    solve_quadratic_equation(coefficients=coefficients, variable=unknown)
elif main_choice == 3:
    print("NUMERICAL INTEGRATION")
    f = input_expression()
    intervals = get_intervals()
    result = solve_integral(f, intervals["a"], intervals["b"])
    print(f"integral of {f} from {intervals['a']} to {intervals['b']} is {result}")
else:
    print("INVALID CHOICE")
