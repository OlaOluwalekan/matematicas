from globals import OPERATORS, VARIABLES

def simplify_expression(expression_list, variables):
    """
        simplify the list of expression into a simple list of numbers and operators

        args:
            expression_list (list): The list of expression to be simplified
            variables (dictionary): key value pair of variables and their values
        
        returns:
            simplified_list (list): a simplified list of numbers and operators
    """
    simplified_list = []
    for term in expression_list:
        if term not in OPERATORS:
            temp = []
            for i, t in enumerate(term):
                if t in VARIABLES:
                    new_t = "~" + t + "~"
                    temp.append(new_t)
                else:
                    temp.append(t)
            temp = "".join(temp).split("~")
            
            product = 1
            for char in temp:
                if char == "":
                    product = product * 1
                elif char in VARIABLES:
                    product = product * variables[char]
                else:
                    product = product * float(char)
                
            simplified_list.append(product)
        else:
            simplified_list.append(term)

    return simplified_list