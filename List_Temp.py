def strangeFunction(n):
    if(n % 2 == 0):
        return True
x = int(input("Enter any number : "))
result = strangeFunction(x)
if result == True:
    print("The number is divisible by 2")
else:
    print("The number is not divisible by 2")
