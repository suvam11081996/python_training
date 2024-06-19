"""

frozenset
    -- We have option to store collection of values like list of name, list of email ids etc
    -- We can store unique values
    -- No index number to each value
    -- Unordered 


Since we dont have index number to each values
 --- we can use whole collection
 or
 --- we can convert to other type like list/tuple etc
 or
 --- we can iterate using loops


"""

print("tuple PART-2")
print("How to store values")

print("_"*20)
#------------------

#NO shortcut to frozen set so we are directly creating object using class name
my_frozenset_1 = frozenset({"python", "python", "python", "python", "Java", "Java", 10, 20})
print(my_frozenset_1)

print("#"*40, end="\n\n")
#########################################
# Convert to other type

# my_list = list(my_frozenset_1)
# my_tuple = tuple(my_frozenset_1)

print("tuple PART-3")
print("How to store values")

print("_"*20)
#------------------

print(dir(frozenset))
print("#"*40, end="\n\n")

#######################################

print("tuple PART-4")
print("How to store values")

print("_"*20)
#------------------

my_frozenset_1 = frozenset({"C", "C++", "Java"})
my_frozenset_2 = frozenset({"C", "C++", "Perl", "Python"})

union_result = my_frozenset_1.union(my_frozenset_2)
print("union_result: ", union_result, end="\n\n")

print("#"*40, end="\n\n")



