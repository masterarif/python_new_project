var = 1
while var < 10:
    print("#")
    var = var << 1

#lst = [[0, 1, 2] for i in range(2)]
#print(lst[2][0])
###################
lst = [i for i in range(-1, 2)]
print(lst)
#######################
lst1 = [1, 2, 3]
lst2 = []
for v in lst1:
    lst2.insert(0,v)
print(lst2)
###################
nums = [1, 2, 3]
vals = nums
del vals[1:2]
print(nums)
print(vals)
######################
t = [[3-i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)
#################
lst = [1, 2, 3]
for v in range(len(lst)):
    lst.insert(1, lst[v])
print(lst)
####################
for i in range(1):
    print("#")
else:
    print("#")
#####################
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c + d + e)
################
nums = [1, 2, 3]
vals = nums[-1:-2]
print(nums)
print(vals)