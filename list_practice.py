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

##########################################
myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop

while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print(myList)

################################

myList = [8, 10, 6, 2, 4]
myList.sort()
print(myList)

##################################

lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst) # outputs: [4, 2, 1, 3, 5]

##################################

a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()

print(lst)

##################################
myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))
for i in range(num):
    val = float(input("Enter a list element: "))
    myList.append(val)
while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print("\nSorted:")
print(myList)
###################
list1 = [1]
list2 = list1
list1[0] = 2
print(list2)
list1[0] = 3
print(list2)

#########################

ist1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

#####################

# Copying the whole list
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)
#######################
# Copying part of the list
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)
##########################
myList = [10, 8, 6, 4, 2]
newList = myList[1:-1]
print(newList)
#######################
myList = [10, 8, 6, 4, 2]
newList = myList[-1:1]
print(newList)
####################
myList = [10, 8, 6, 4, 2]
newList = myList[:3]
print(newList)

##################
myList = [10, 8, 6, 4, 2]
newList = myList[:3]
print(newList)

############################

myList = [10, 8, 6, 4, 2]
newList = myList[3:]
print(newList)

#################

myList = [10, 8, 6, 4, 2]
newList = myList[:]
print(newList)

############################

del myList[1:3]
print(myList)

############################

myList = [10, 8, 6, 4, 2]
del myList[:]
print(myList)

############################

myList = [10, 8, 6, 4, 2]
del myList
print(myList) ##runtime error

############################

myList = [0, 3, 12, 8, 2]

print(5 in myList)
print(5 not in myList)
print(12 in myList)

##########################

myList = [1, "Arif", "Khan", 15]
print("Arif" in myList)

#############################

myList = [3, 11, 5, 1, 9, 7, 15, 13, 17]
largest = myList[0]

for i in range(1, len(myList)):
    if myList[i] > largest:
        largest = myList[i]

print(largest)
print(len(myList))

###############################

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = 5
found = False

for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")


#######################

myList = []
found = False

n = int(input("Enter number of element :"))
for i in range(0, n):
    ele = int(input("Enter Number :"))
    myList.append(ele)
print(myList)

toFind = int(input("Enter to be find : "))
for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break

if found:
    print("Element found at index", i + 1, "and the number was ", myList[i])
else:
    print("absent")

#############################

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# put your code here
#
tempList = []
for i in range(len(myList)):
    if i not in tempList:
        tempList.append(i)

print("The list with unique elements only:")
print("Hello :", str(tempList))
##############################
# Python 3 code to demonstrate
# removing duplicated from list
# using naive methods

# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))

# using naive method
# to remove duplicated
# from list
res = []
for i in test_list:
    if i not in res:
        res.append(i)

    # printing list after removal
print("The list after removing duplicates : " + str(res))

####################

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# put your code here
#
res = []
for i in myList:
    if i not in res:
        res.append(i)
print("The list with unique elements only:")
print(res)

########################

squares = [x ** 2 for x in range(10)]
print(squares)

########################

squares = [x ** 2 for x in range(10)]
print(squares)
twos = [2 ** i for i in range(8)]
print(twos)
odds = [x for x in squares if x % 2 != 0 ]
print(odds)

######################################

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

#####################################

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

####################################

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, "days were hot.")

###############################
