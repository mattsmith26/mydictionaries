import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()


print(phonebook)
print(type(phonebook))
phone = phonebook["Chris"]

print(phone)


mydictionary = {}

print(mydictionary)

mydictionary = dict(m=8, n=9) # another way to create dictionaries

print(mydictionary)


print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = "Chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(name, "is not found in phonebook")




print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

# keys can not get updated only values
print(phonebook)
phonebook["Chris"] = "555-0123"

phonebook["Joe"] = "555-4444" # if it does not exist it just adds it as a key value pair
print(phonebook)






print()
print('*****  end section 3 ********')
print()







print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()




#del phonebook["Chris"] # will give you error if Chris is not found
#print(phonebook)








print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

# the defualt iteration for the for loop is the KEYS (in this example it prints out the keys, all the names)
for key in phonebook:
    print(key)
    print(phonebook[key])
# have to call the .values method to go through the values
for value in phonebook.values():
    print(value)


## both goes through keys and values at the same time
for k,v in phonebook.items():
    print("key: ", k, "   value:", v)


# tuples are immutable objects that you cannot change
for tuple in phonebook.items():
    print(tuple)





print()
print('*****  end section 5 ********')
print()






print()
print('*****  start section 6 - using get and clear ********')
print()


# get method allows you to put in an optional argument
phone = phonebook.get("Chris", "key not found")
print(phone)


#clear out your dictionary, dictionary exists but nothing in it
#phonebook.clear()


#print(phonebook)



print()
print('*****  end section 6 ********')
print()






print()
print('*****  start section 7 - using pop method ********')
print()



#a = phonebook.pop("Chris", "not found") # pops chris out of the phonebook dictionary

#print(a)

#print(phonebook)




print()
print('*****  end section 7 ********')
print()







print()
print('*****  start section 8 - using popitem ********')
print()


print(phonebook)
#a = phonebook.popitem() # item gives you both the key and value, so it is a tuple
# doesn't do the random part, just pops out the last key/item in the dictionary


#print(a)
#print(phonebook)






print()
print('*****  end section 8 ********')
print()





print()
print('*****  start section 9 - using random and converting to list ********')
print()


list_of_keys = list(phonebook)
print(list_of_keys)

random_key = random.choice(list_of_keys)
print(random_key)

random_value = phonebook[random_key]
print(random_value)



#alternatively

random_value = phonebook[random.choice(list(phonebook))]
print(random_value)

print()
print('*****  end section 9 ********')
print()



