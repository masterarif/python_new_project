numbers = [10, 5, 7, 2, 1]
print("List content:", numbers) # printing original list content

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers) # printing original list content

numbers[0] = 111
print("New list content: ", numbers) # current list content

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers) # printing original list content

numbers[0] = 111
print("\nPrevious list content:", numbers) # printing previous list content

numbers[1] = numbers[4] # copying value of the fifth element to the second
print("New list content:", numbers) # printing current list content

##################################

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers) # printing original list content

numbers[0] = 111
print("\nPrevious list content:", numbers) # printing previous list content

numbers[1] = numbers[4] # copying value of the fifth element to the second
print("Previous list content:", numbers) # printing previous list content

print("\nList length:", len(numbers)) # printing the list's length
###################################
numbers = [1, 2, 3, 4, 5]
del numbers[1]
print(len(numbers))
print(numbers)

##############################
## An element with an index equal to -1 is the last one in the list.
## Similarly, the element with an index equal to -2 is the one before last in the list.
numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])

#################################

hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
user = input("Enter Secret Number : ")

# to replace the middle number with an integer number entered by the user.
hatList[round(len(hatList)/2)] = int(user)
# Step 2: write a line of code here that removes the last element from the list.
del hatList[len(hatList)-1]
# Step 3: write a line of code here that prints the length of the existing list.

print(hatList)
print(len(hatList))

###################################

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

##############################

myList = [] # creating an empty list

for i in range(5):
    myList.append(i + 1)

print(myList)

myList = [] # creating an empty list

for i in range(5):
    myList.insert(0, i + 1)

print(myList)

################################
variable1 = 1
variable2 = 2

variable1, variable2 = variable2, variable1

print(variable1)
print(variable2)

#################################

myList = [10, 1, 8, 3, 5]

myList[0], myList[4] = myList[4], myList[0]
myList[1], myList[3] = myList[3], myList[1]

print(myList)

##################################

myList = [10, 1, 8, 3, 5]
length = len(myList)
print(myList)
for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]
    print(i)
print(myList)

###################################
myList = [1, None, True, 'I am a string', 256, 0]
print(myList[3]) # outputs: I am a string
print(myList[-1]) # outputs: 0

myList[1] = '?'
print(myList) # outputs: [1, '?', True, 'I am a string', 256, 0]

myList.insert(0, "first")
myList.append("last")
print(myList) # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

####################################

myList = [1, 2, 3, 4]
del myList[2]
print(myList) # outputs: [1, 2, 4]

del myList # deletes the whole list

#####################################

myList = ["white", "purple", "blue", "yellow", "green"]

for color in myList:
    print(color)


#######################################

myList = ["white", "purple", "blue", "yellow", "green"]
print(len(myList)) # outputs 5

del myList[2]
print(len(myList)) # outputs 4

#######################################

lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)

###############################

lst = [1, 2, 3, 4, 5]
lst2 = []
add = 0

for number in lst:
    add += number
    lst2.append(add)

print(lst2)

##################################

lst = []
del lst
print(lst)

####################################

lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))

#############################

myList = [8, 2, 10, 5]
swapped = True
i = -0
while swapped:
    swapped = False
    if myList[i] > myList[i + 1]
        myList[i], myList[i + 1] = myList[i + 1], myList[i]
        i += 1
        if i == (len(myList) - 1):
            swapped = True


