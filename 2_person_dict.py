person = {} #creates an empty dictionary
person["fname"] = "Joe" # if this does not exist then it adds it, if it does exist it just updates it

person["lname"] = "Fonebone"
person["age"] = 51 # elements can be any value type

person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] # list object

person["pets"] = {"dog": "Fido", "cat": "Sox"} # dicitonary object, dictionary can have a value of a list or dicitonary

print(person)

print(person["children"][1]) 

print(person["pets"]["cat"]) # can not use index value for a dictionary, ex: can not use [1]
print()


for line in person["children"]:
    print(line)

for line in person["pets"]:
    print(person["pets"][line]) # need to specify that pets is the key

    


