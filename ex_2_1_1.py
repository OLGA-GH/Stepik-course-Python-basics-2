try:
    foo()
except Exception as e:
    if isinstance(e, ZeroDivisionError) == True:
        print("ZeroDivisionError")
    elif isinstance(e, ArithmeticError) == True:
        print("ArithmeticError")
    elif isinstance(e, AssertionError) == True:
        print("AssertionError")
