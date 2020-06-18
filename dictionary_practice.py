dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

#####################

dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

#####

dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

###
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

####################


dictionary = { "dog" : "chien", "horse" : "cheval", "cat" : "chat"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])
#####################

dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

for french in dictionary.values():
    print(french)
#####################
dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)
#####################


dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)


dictionary.update({"duck" : "canard"})
print(dictionary)

del dictionary['dog']
print(dictionary)

#####################

school_class = {}

while True:
    name = input("Enter the student's name (or type exit to stop): ")
    if name == 'exit':
        break

    score = int(input("Enter the student's score (0-10): "))

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
