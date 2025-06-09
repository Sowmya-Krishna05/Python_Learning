marks = 85
if marks >= 50:
    print("You passed!")
    if marks >= 75:
        print("You passed with distinction!")
        if marks == 100:
            print("Perfect score!")
    else:
        print("Good effort.")
else:
    print("You failed.")
