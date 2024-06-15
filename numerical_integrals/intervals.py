def get_intervals():
    """
        gets the intervals of the integral.

        returns:
            intervals (dictionary): A dictionary of the intervals a and b
    """

    a = float(input("Enter the integral lower bound (a): "))
    b = float(input("Enter the integral upper bound (b): "))

    return {"a": a, "b": b}