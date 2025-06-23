import traceback

try:
    1 / 0  # This will raise a ZeroDivisionError
except:
    traceback.print_exc()  # This will print the traceback of the exception
