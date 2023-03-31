try:
    foo()
except Exception as e:
    if isinstance(e, ZeroDivisionError):
        print("ZeroDivisionError")
    elif isinstance(e, ArithmeticError):
        print("ArithmeticError")
    elif isinstance(e, AssertionError):
        print("AssertionError")
