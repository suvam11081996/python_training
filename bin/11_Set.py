"""
- set
    -- We have option to store collection of values like list of name, list of email ids etc
    -- We can store unique values

"""


print("set PART-2")
print("How to store values")

print("_"*20)
#------------------

#NO shortcut to frozen set so we are directly creating object using class name
my_set_1 = set({"python", "python", "python", "python", "Java", "Java", 10, 20})
print(my_set_1)

print("#"*40, end="\n\n")
#########################################
# Convert to other type

# my_list = list(my_set_1)
# my_set = set(my_set_1)

print("set PART-3")
print("How to store values")

print("_"*20)
#------------------


print(dir(set))
print("#"*40, end="\n\n")

#######################################

print("set PART-4")
print("ADD/REMOVE element")

print("_"*20)
#------------------

my_set = {"C", "C++", "Java"}
print("my_set: ", my_set, end="\n\n")


my_set.add("perl")
print("my_set after adding Perl : ", my_set, end="\n\n")

my_set.remove("C")
print("my_set after removing C : ", my_set, end="\n\n")

print("#"*40, end="\n\n")

#################################################################


