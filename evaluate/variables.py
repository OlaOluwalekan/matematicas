from globals import VARIABLES

def get_variables(expression):
    """
        gets the variables of an expression

        args:
            expression (str): The expression to be evaluated

        returns:
            variables (dictionary): A dictionary of variables of the expression
    """

    

    variables_list = []
    for character in expression:
        # print(character)
        if character in VARIABLES and character not in variables_list:
            variables_list.append(character)

    print(f"You have {len(variables_list)} variable(s) ({",".join(variables_list)}) in your expression")

    variables_object = {}

    for var in variables_list:
        variables_object[var] = float(eval(input(f"Enter the value of {var}: ")))

    # print(variables_object)
    return variables_object