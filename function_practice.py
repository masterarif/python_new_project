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

def myFunction():
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)

### result : Do I know that variable? 2
### 1

################################

def myFunction():
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)

### result : Do I know that variable? 1
### 1

################################

def myFunction(n):
    print("I got", n)
    n += 1
    print("I have", n)

var = 1
myFunction(var)
print(var)

## result I got 1
##        I have 2
##        1

########################
## 1. A variable that exists outside a function has a scope
# inside the function body (Example 1) unless the function
# defines a variable of the same name

var = 2

def multByVar(x):
    return x * var

print(multByVar(7))

# outputs: 14

#########################

def multip(x):
    var = 7
    return x * var

var = 3
print(multip(7))    # outputs: 49

###########################

def adding(x):
    var = 7
    return x + var

print(adding(4))    # outputs: 11

print(var)    # NameError

##########################

var = 2
print(var)    # outputs: 2

def retVar():
    global var
    var = 5
    return var

print(retVar())    # outputs: 5

print(var)    # outputs: 5

###########################

a = 1

def fun():
    a = 2
    print(a)

fun()
print(a)

###########################

a = 1

def fun():
    global a
    a = 2
    print(a)

fun()
a = 3
print(a)

###################

a = 1

def fun():
    global a
    a = 2
    print(a)

a = 3
fun()
print(a)

#########################

#Some simple functions: evaluating the BMI
#Let's get started on a function to evaluate the Body Mass Index (BMI).

#BMI equals weight in kilograms divided by height in meters squared

def bmi(weight, height):
    return weight / height ** 2

print(bmi(52.5, 1.65))

##########################

def lbtokg(lb):
    return lb * 0.45359237

print(lbtokg(1))

########################
def ftintom(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254


def lbstokg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
            weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(weight=lbstokg(176), height=ftintom(5, 7)))

#########################

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
            weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))

##########################

#Some simple functions: continued
#Let's play with triangles now. We'll start with a function to check whether three sides of given lengths can build a triangle.

#A triangle with equal sides

#We know from school that the sum of two arbitrary sides has to be longer than the third side.

#It won't be a hard challenge. The function will have three parameters - one for each side.

def isItATriangle(a, b, c):
    if a + b <= c or b + c <= a or \
    c + a <= b:
        return False
    return True

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))

#####

def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))

#####

def isItATriangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))

####


def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def isItRightTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(isItRightTriangle(5, 3, 4))
print(isItRightTriangle(1, 3, 4))

####

def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Enter the first side's length: "))
b = float(input("Enter the second side's length: "))
c = float(input("Enter the third side's length: "))

if isItATriangle(a, b, c):
    print("Congratulations - it can be a triangle.")
else:
    print("Sorry, it won't be a triangle.")

##################################################

#Some simple functions: evaluating a triangle's field
#We can also evaluate a triangle's field. Heron's formula will be handy here:

#s = (a + b + c) / 2
#A = the suare root of s(s - a)(s - b)(s - c)
#We're going use the exponentiation operator to find the square root - it may seem strange, but it works:

#The square root of x = x to the power of 1/2

#This is the resulting code:

def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def fieldOfTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return None
    return heron(a, b, c)

print(fieldOfTriangle(1., 1., 2. ** .5))

####

def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Enter the first side's length: "))
b = float(input("Enter the second side's length: "))
c = float(input("Enter the third side's length: "))

if isItATriangle(a, b, c):
    print("Congratulations - it can be a triangle.")
else:
    print("Sorry, it won't be a triangle.")

####################################

#Some simple functions: factorials
#Another function we're about to write is factorials. Do you remember how a factorial is defined?

0! = 1 (yes! it's true)
1! = 1
2! = 1 * 2
3! = 1 * 2 * 3
4! = 1 * 2 * 3 * 4
:
:
n! = 1 * 2 ** 3 * 4 * ... * n-1 * n

####


def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 6):  # testing
    print(n, factorialFun(n))


#################################

#Some simple functions: Fibonacci numbers
#Are you familiar with Fibonacci numbers?

#They are a sequence of integer numbers built using a very simple rule:

#the first element of the sequence is equal to one (Fib1 = 1)
#the second is also equal to one (Fib2 = 1)
#every subsequent number is the sum of the two preceding numbers (Fibi = Fibi-1 + Fibi-2)
#Here are some of the first Fibonacci numbers:

fib1 = 1
fib2 = 1
fib3 = 1 + 1 = 2
fib4 = 1 + 2 = 3
fib5 = 2 + 3 = 5
fib6 = 3 + 5 = 8
fib7 = 5 + 8 = 13


#####

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # testing
    print(n, "->", fib(n))

################################

# Recursive implementation of the factorial function
def factorial(n):
    if n == 1:    # the base case (termination condition)
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4)) # 4 * 3 * 2 * 1 = 24


####

def factorial(n):
    return n * factorial(n - 1)

print(factorial(4))    #### ERROR

####

def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))

## Output 56



