try:
    try:
       1/0
    except ZeroDivisionError:
        print("Handled ZeroDivisionError in inner try block")
except:
    print("Handled exception in outer try block")