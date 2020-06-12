# for i in range(100):
#     print(i)
#
# for i in range(10):
#     print("The value of i is currently", i)
# for i in range(2, 8):
#     print("The value of i is currently", i)
# start = int(input("Enter Start Range :"))
# end1 = int(input("Enter End Range"))
# for i in range(start, end1):
#     print(i)
#
# start = int(input("Enter Start Range :"))
# end1 = int(input("Enter End Range"))
# for i in range(start, end1, 2):
#     print(i)
#
# pow = 1
# for exp in range(16):
#     print("2 to the power of", exp, "is", pow)
#     pow *= 2
#
# import time
#
# # Write a for loop that counts to five.
#     # Body of the loop - print the loop iteration number and the word "Mississippi".
#     # Body of the loop - use: time.sleep(1)
# for i in range(5):
#     print(i, "Mississippi")
#     time.sleep(2)
#
# # Write a print function with the final message.
# print("Ready or not, here I come!")
#
# # break - example
#
# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")
#
#
# # continue - example
#
# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")
#
# # Prompt the user to enter a word
# # and assign it to the userWord variable.
# userWord = input("Enter a word :")
# userWord = userWord.upper()
# for letter in userWord:
#     # Complete the body of the for loop.
#     if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
#         continue
#     else:
#         print(letter)
# ##################################################
# wordWithoutVovels = ""
#
# # Prompt the user to enter a word
# # and assign it to the userWord variable
#
# userWord = input("Enter Word :")
# userWord = userWord.upper()
# for letter in userWord:
#     # Complete the body of the loop.
#     if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
#         continue
#     else:
#         wordWithoutVovels += letter
#
# # Print the word assigned to wordWithoutVowels.
# print(wordWithoutVovels)
#
# #######################
# for i in range(5):
#     print(i)
# else:
#     print("else:", i)
# ################################
#
# i = 111
# for i in range(2, 1):
#     print(i)
# else:
#     print("else:", i)
#
# #####################
#
# # Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
# #
# # Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
# #
# # The figure illustrates the rule used by the builders:
# #
# #
# #
# # Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
# #
# # Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.
# #
# # Test your code using the data we've provided.
#
#
# blocks = int(input("Enter the number of blocks: "))
#
# #
# # Write your code here.
# #
# height = 0
# while True:
#     if blocks < height or blocks == height:
#         break
#     else:
#         height += 1
#         blocks -= height
#
# print("The height of the pyramid:", height)
#
# text = "OpenEDG Python Institute"
# for letter in text:
#     if letter == "P":
#         break
#     print(letter, end="")
#
# name = input("Enter Your Name :")
# i = 0
# for letter in name:
#     print(letter)
#     if letter != " ":
#         i +=1
# print("Total alphabets : ", i)

i = 0
for i in range(1, 20, 2):
    print(i)
    i +=1
#############################
email = input("Enter your email address : ")
name = ""
for letter in email:
    if letter == "@":
        break
    else:
        name += letter
        continue
print(name)
###############################
x = ""
for digit in "0165031806510":

        # line of code
        # line of code
    # line of code
    if digit == "0":
        x += "x"
    else:
        x += digit
print(x)