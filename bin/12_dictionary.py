"""
 - Dictionary
    -- We have option to store collection of values like list of name, list of email ids etc
    -- We can store duplicate values
    -- We need provide our own index to each value called KEY/VALUE pair

"""

print("dictionary PART-1")
print("How to store values")

print("_"*20)
#------------------

my_dictionary_1 = {0:"python", 1:5, 2:"online"}
# Internally it will create object of builyin class 'dict' and store the values

# FOR KEYS: We can use any IMMUTABLE VALUES like number, String, tuple etc for KEY
my_dictionary_2 = {"course":"python", "duration":5, "mode":"online"}

#FOR VALUES: We can store any type of values
my_dictionary_3 = {
    "duration" : 5,
    "course" : "python",
    "mode" : ["online", "offline"],
    "trainer" : {"fname" : "abc", "lname" : "xyz"}
}

print("my_dictionary_1: ", my_dictionary_1, end="\n\n")
print("my_dictionary_2: ", my_dictionary_2, end="\n\n")
print("my_dictionary_2: ", my_dictionary_3, end="\n\n")



print("#"*40, end="\n\n")

######################

print("dictionary PART-2")
print("Access individual values")

print("_"*20)
#------------------

my_dictionary = {
    "duration" : 5,
    "course" : "python",
    "mode" : ["online", "offline"],
    "trainer" : {"fname" : "abc", "lname" : "xyz"}
}

print("my_dictionary: ", my_dictionary, end="\n\n")

print("duration: ", my_dictionary["duration"], end="\n\n")

print("course name: ", my_dictionary["course"], end="\n\n") #python
print("2nd character in course name: ", my_dictionary["course"][1], end="\n\n")

print("mode: ", my_dictionary["mode"], end="\n\n")
print("2nd value in mode: ", my_dictionary["mode"][1], end="\n\n")
print("4th character in 2nd value in mode: ", my_dictionary["mode"][1][3], end="\n\n")

print("trainer:", my_dictionary["trainer"])
print("lname of trainer:", my_dictionary["trainer"]["lname"])
print("2nd character in lname of trainer:", my_dictionary["trainer"]["lname"][1])

print("#"*40, end="\n\n")

######################


print("dictionary PART-3")
print("Methods inside 'dict' class")

print("_"*20)
#------------------

print(dir(dict))


print("#"*40, end="\n\n")

######################

print("dictionary PART-4")
print("Methods inside 'dict' class")

print("_"*20)
#------------------

my_dictionary_2 = {"course":"python", "duration":5, "mode":"online"}
print("my_dictionary: ", my_dictionary, end="\n\n")

#Add/Update
my_dictionary["location"] = "India"

print("my_dictionary after adding location: ", my_dictionary, end="\n\n")

#Remove
my_dictionary.popitem()
print("my_dictionary after removing last element: ", my_dictionary, end="\n\n")

print("#"*40, end="\n\n")

######################