
x = int(input("Enter an integer: "))
if x < 0:
    print(x, "is NOT a Palindrome Number")
else:
    if str(x) == str(x)[::-1]:
        print(x, "is a Palindrome Number")
    else:
        print(x, "is NOT a Palindrome Number")
