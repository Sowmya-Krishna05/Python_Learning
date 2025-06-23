def risky():
    return 1 / 0


try:
    risky()
except Exception as e:
    print(f"An error occurred: {e}")
    # You can also log the error or handle it in a specific way
    # For example, logging the error to a file or sending an alert
