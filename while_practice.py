odd_number = 0
even_number = 0
number = int(input("Enter any number or 0 to stop : "))
while number != 0:
    if number % 2 == 1:
        odd_number += 1
    else:
        even_number += 1
    number = int(input("Enter any number or 0 to stop : "))

print()
print("Odd number count :", odd_number)
print("Even number count : ", even_number)

counter = 5
while counter != 0:
    print("Inside the loop")
    counter -= 1
print("Outside the loop")

counter = 5
while counter:
    print("Inside the loop")
    counter -= 1
print("Outside the loop")

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = 0
while secret_number != number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Enter Secret Number : "))
print("Well done, muggle! you are free now")


largestNumber = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largestNumber:
        largestNumber = number

if counter != 0:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")

largestNumber = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largestNumber:
        largestNumber = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")

while True:
    secret = input("Enter Secret Word : ")
    if secret == "chupacabra":
        break
    else:
        print("You are still in loop!")
        continue
print("You are successfully left the loop")