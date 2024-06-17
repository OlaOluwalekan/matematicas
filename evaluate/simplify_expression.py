from globals import OPERATORS, VARIABLES
from evaluate.special_solution import solve_special_cases

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

    # for term in expression_list:
    #     if term not in OPERATORS:
    #         temp = []
    #         # SPLIT EACH TERM INTO COMPONENTS EG: 2x INTO 2 AND x
    #         for i, t in enumerate(term):
    #             if t in VARIABLES:
    #                 new_t = "~" + t + "~"
    #                 temp.append(new_t)
    #             else:
    #                 temp.append(t)
    #         temp = "".join(temp).split("~")
            
    #         product = 1
    #         # SUBSTITUTE THE VALUE OF THE VARIABLES IN THE TERM AND SIMPLIFY TO DIGIT
    #         for char in temp:
    #             if char == "":
    #                 product = product * 1
    #             elif char in VARIABLES:
    #                 product = product * variables[char]
    #             else:
    #                 product = product * float(char)
                
    #         simplified_list.append(product)
    #     else:
    #         simplified_list.append(term)

    for term in expression_list:
        if term not in OPERATORS:
            if "Ĉ" in term or "§" in term or "Ť" in term:
                symbol = term[0]
                new_term = term.replace(symbol, "")
                solution = solve_special_cases(new_term, symbol)
                simplified_list.append(solution)
            else:
                temp = []
                # SPLIT EACH TERM INTO COMPONENTS EG: 2x INTO 2 AND x
                for i, t in enumerate(term):
                    if t in VARIABLES:
                        new_t = "~" + t + "~"
                        temp.append(new_t)
                    else:
                        temp.append(t)
                temp = "".join(temp).split("~")
                
                product = 1
                # SUBSTITUTE THE VALUE OF THE VARIABLES IN THE TERM AND SIMPLIFY TO DIGIT
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

# x-tan(40)y+xcos(60)-ysin(20)