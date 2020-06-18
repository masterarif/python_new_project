#########################

myTuple = (1, 10, 100, 1000)

myTuple.append(10000)  #### ERROR Can not append Tuple
del myTuple[0]
myTuple[1] = -10

###########################

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

###
myTuple = (1, 10, 100)

t1 = myTuple + (1000, 10000)
t2 = myTuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in myTuple)
print(-10 not in myTuple)

##########################