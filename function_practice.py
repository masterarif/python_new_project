def message():
    print("Enter a Value :", end="")

#print("Enter a value: ")
message()
a = int(input())

#print("Enter a value: ")
message()
b = int(input())

#print("Enter a value: ")
message()
c = int(input())
print(a, b, c)

####################

def ent():
    input("Enter Your Name :")
def name(x):
    print("Your Name is : ", x)


y = ent()
print(y)
name(str(y))
############################

def hello(name):    # defining a function
    print("Hello,", name)    # body of the function


name = input("Enter your name: ")

hello(name)    # calling the function

##########################

def message(number):
    print("Enter a number:", number)
number = 1234
message(1)
print(number)

###################
def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")
#######################

def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

##############################

def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

############################################

def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction(firstName = "James", lastName = "Bond")
introduction(lastName = "Skywalker", firstName = "Luke")

##################################

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# call the adding function here
adding(1, 2, 3)
adding(c = 1, b = 2, a = 3)
####################################

def introduction(firstName, lastName="Smith"):
    print("Hello, my name is", firstName, lastName)

# call the function here
introduction("abc")
introduction("abc", "xuz")

###############################

def hiAll(name1, name2):
    print("Hi,", name2)
    print("Hi,", name1)

hiAll("Sebastian", "Konrad")

#########################

def address(street, city, postalCode):
    print("Your address is:", street, "St.,", city, postalCode)

s = input("Street: ")
pC = input("Postal Code: ")
c = input("City: ")

address(s, c, pC)

##############################

#Ex. 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


#Ex. 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

#Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3
#########################

def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(a=5, 2)    # Syntax Error

#########################

def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")

happy_new_year()
happy_new_year(True)
happy_new_year(False)

########################

def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned its result. It's:", x)

#########################

def boring_function(a):
    b = a * 2
    return b

x = boring_function(5)

print("The boring_function has returned its result. It's:", x)

####################

def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")

##################

def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
b = boring_function()
print("This lesson is boring...", b)

##########################

value = None
if value is None:
   print("Sorry, you don't carry any value")

####################

def strangeFunction(n):
    if(n % 2 == 0):
        return True
x = int(input("Enter any number : "))
result = strangeFunction(x)
if result == True:
    print("The number is divisible by 2")
else:
    print("The number is not divisible by 2")
#########################

def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s


print(list_sum([1, 2, 3, 4]))

###########################

def strangeListFunction(n):
    strangeList = []

    for i in range(0, n):
        strangeList.insert(0, i)
        print(strangeList)

    return strangeList


print(strangeListFunction(5))

########################
## Check for leap year

def isYearLeap(year):
    #
    # put your code here
    #
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
    else:
        return False


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr, "->", end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")

#################################

def isYearLeap(year):
#
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
    else:
        return False
# your code from LAB 4.1.3.6
#

def daysInMonth(year, month):
#
# put your new code here
    mm = [1, 3, 5, 7, 8, 10, 11]
    if isYearLeap(year) == True and month == 2:
       return 28
    if isYearLeap(year) == False and month == 2:
        return 29
    if month in mm:
        return 31
    else:
        return 30
#

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

###################################
# PRIME NUMBER SERIES
def isPrime(num):
#
# put your code here
#
    x = 2
    while x < num - 1:
        if num % x == 0:
            return False
        x += 1
    return True


for i in range(1, 20):
	if isPrime(i + 1):
		print(i + 1, end=" ")
print()


#####################################

def multiply(a, b):
    return a * b

print(multiply(3, 4))    # outputs: 12
#################################
def multiply(a, b):
    return

print(multiply(3, 4))    # outputs: None

###########################

# Example 1
def wishes():
    print("My Wishes")
    return "Happy Birthday"

wishes()    # outputs: My Wishes

#####################################
# Example 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"

print(wishes())    # outputs: My Wishes
                   #          Happy Birthday
######################################

def mylist(names):
    for i in range(mylist):
        print("Hi", i)

mylist(["abc","xys", "Efg"])

######################################

def mylist(names):
    for i in names:
        print("Hi", i)

def wishes():
    print("Hello")
    return "bye"

mylist(["abc","xys", "Efg"])
wishes()
print(wishes())

############################

def isInt(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(isInt(5))
print(isInt(5.0))
print(isInt("5"))

###########################


def listUpdater(lst):
    updList = []
    for elem in lst:
        elem **= 2
        updList.append(elem)
    return updList

l = [1, 2, 3, 4, 5]
print(listUpdater(l))

############################

def myFunction():
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)

##############################

def myFunction():
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)

###############################

## Functions and scopes: the global keyword

def myFunction():
    global var
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)

##############################

def myFunction(myList1):
    print(myList1)
    myList1 = [0, 1]

myList2 = [2, 3]
myFunction(myList2)
print(myList2)

#############################

