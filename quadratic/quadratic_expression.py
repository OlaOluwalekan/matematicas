from evaluate.input_expression import input_expression
from globals import VARIABLES, OPERATORS

def get_quadratic_expression():
    """
        Asks the user for a quadratic expression and returns the coefficients

        returns:
            the coefficients of the quadratic expression
    """

    expression = input_expression("Enter a quadratic expression (use '^' for exponent) or enter the values of a, b and c in that order each separated by a comma (,): ")

    coefficients = {"a": 0, "b": 0, "c": 0}
    if set(expression) & set(VARIABLES):
        temp = []
        vars = []
        for char in expression:
            if char in VARIABLES and char not in vars:
                vars.append(char)
        
        if len(vars) > 1:
            print("You can only have one unknown in a quadratic equation.")
            return

        unknown = vars[0]

        for i, char in enumerate(expression):
            if char in OPERATORS:
                if i == 0:
                    temp.append(char)
                else:
                    temp.append("," + char)
            else:
                temp.append(char)
        expression = "".join(temp)
        temp = expression.split(",")
        for i, term in enumerate(temp):
            if "^" in term:
                new_term = term.split(unknown)
                if new_term[0] == "":
                    coefficients["a"] = 1
                elif new_term[0] == "-" or new_term[0] == "+":
                    coefficients["a"] = float(new_term[0] + "1")
                else:
                    coefficients["a"] = float(new_term[0])
            elif unknown in term and "^" not in term:
                new_term = term.split(unknown)
                if new_term[0] == "":
                    coefficients["b"] = 1
                elif new_term[0] == "-" or new_term[0] == "+":
                    coefficients["b"] = float(new_term[0] + "1")
                else:
                    coefficients["b"] = float(new_term[0])
            else:
                coefficients["c"] = float(term)
    else:
        unknown = "x"
        expression = expression.replace(" ", "")
        expression = expression.split(",")
        if len(expression) == 2:
            expression.append(0)
        elif len(expression) == 1:
            expression.append(0)
            expression.append(0)
        
        coefficients = {"a": 0 if expression[0] == "" else float(expression[0]), "b": float(expression[1]), "c": float(expression[2])}

    # print(expression)
    return {"coefficients": coefficients, "unknown": unknown}