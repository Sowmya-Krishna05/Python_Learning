for num in range(10):
    if num == 2:
        print("Skipped 2 using continue")
        continue  # skips the rest of the loop for this iteration
    if num == 8:
        print("Breaking at 8")
        break  # exits the loop entirely

    print("Current number:", num)

print("Loop ended.")
