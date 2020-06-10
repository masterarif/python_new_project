for i in range(100):
    print(i)

for i in range(10):
    print("The value of i is currently", i)
for i in range(2, 8):
    print("The value of i is currently", i)
start = int(input("Enter Start Range :"))
end1 = int(input("Enter End Range"))
for i in range(start, end1):
    print(i)

start = int(input("Enter Start Range :"))
end1 = int(input("Enter End Range"))
for i in range(start, end1, 2):
    print(i)

pow = 1
for exp in range(16):
    print("2 to the power of", exp, "is", pow)
    pow *= 2

import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)
for i in range(5):
    print(i, "Mississippi")
    time.sleep(2)

# Write a print function with the final message.
print("Ready or not, here I come!")

# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")