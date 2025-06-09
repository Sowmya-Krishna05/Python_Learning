# Even or Odd number check
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Palindrome check
string = input("Enter a string:")
if string[::-1] == string:
    print(f"{string} is a palidrome string.")
else:
    print(f"{string} is not a palindrome string.")