var = 1
print(var > 0)
print(not (var <= 0))

# i: 00000000000000000000000000001111
# j: 00000000000000000000000000010110
# log = i and j
# print(log)

var = 17
varRight = var >> 1
varLeft = var << 2
print(var, varLeft, varRight)
#############################
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)

#############################

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

################################