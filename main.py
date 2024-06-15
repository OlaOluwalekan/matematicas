from main_options import print_main_options
from evaluate.evaluate_expression import evaluate_expression
from evaluate.input_expression import input_expression

print("WELCOME TO MATEMATICAS")

main_choice = print_main_options()

if main_choice == 1:
    expression = input_expression()
    result = evaluate_expression(expression=expression)
    print("RESULT: ", result)
elif main_choice == 2:
    print("SOLVING FOR UNKNOWN VARIABLES")
else:
    print("INVALID CHOICE")
