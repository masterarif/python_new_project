# #####Loop####################### while
#
# # i = 1
# # while i < 6:
# #   print(i)
# #   i += 1
# ################################
#
# # i = 1
# # while i < 6:
# #   if i == 3:
# #     break
# #    i +=  1
#
# ##########################
# '''
# In the loop, when i is 3,
# jump directly to the next iteration.'
# ''
# # i = 0
# # while i < 6:
# #     i += 1
# #     if i == 3:
# #         continue
# #     print(i)
#
# ###########################
##Print a message once the condition is false.
x = 1
while x < 6:
    x = x + 1
else:
 print("i is no longer less than 6")

#############Loop########################For

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

###########################################
#
# for x in range(6):
#   print(x)

###########################################

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#  if x == "banana":
#     continue:
#   print(x)


 ###############################
#  fruits = ["apple", "banana", "cherry"]
#  for x in fruits:
#      if x == "banana":
#          break
#      print(x)
#
# ############################
# city_to_check = "Tucson"
# cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]
# #print("Hello World!")
# if city_to_check == cleanest_cities[0]:
#      print("It's one of the cleanest cities")
# elif city_to_check == cleanest_cities[1]:
#      print("It's one of the cleanest cities")
# elif city_to_check == cleanest_cities[2]:
#      print("It's one of the cleanest cities")
# elif city_to_check == cleanest_cities[3]:
#      print("It's one of the cleanest cities")
# elif city_to_check == cleanest_cities[4]:
#      print("It's one of the cleanest cities")

#############################

greetings = input("What is your name ")
def print_greetings():
# Python interpreter recognises intendation is key

    print("Welcome on board dear " + greetings)
print_greetings()