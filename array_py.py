colours = ["voilet", "indigo", "blue", "green", "yellow", "orange", "red"]
print(colours)
colours.append("Brown")

print(colours)

del colours[4]
print(colours)

colours.remove("blue")
print(colours)

colours.pop(3)
print(colours)

concat = [1, 2, 3]
print(concat)

concat = concat + [4, 5, 6]
print(concat)

repeat = ['a']
print(repeat)
repeat = repeat * 5
print(repeat)

#slicing an array
fruits = ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange']
print(fruits)
print(fruits[1:4])
print(fruits[:3])
print(fruits[-4:])
print(fruits[-3:-1])

#multidimentional array
multd = [[1,2], [3,4], [5,6], [7,8]]
print(multd)
print(multd[1])
print(multd[3])
print(multd[2][1])
print(multd[3][1])