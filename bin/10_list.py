"""
Mutable
- list
    -- We have option to store collection of values like list of name, list of email ids etc
    -- We can store duplicate values
    -- For each values, automatically index number will be assigned

"""

print("list PART-1")
print("_"*20)
#------------------
my_list_1 = (10,12.5, "python", (100, 200))
#internally it will create object of buily-in class 'list' and store the values

#OR we can use class name
my_list_2= (10,12.5, "python", (100, 200))
print(my_list_1, my_list_2, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#########################################

print("list PART-2")
print("Indexes are similar to String")

print("_"*20)
#------------------

my_list= (10,12.5, "python", (100, 200))
print("my_list:", my_list, end="\n\n")

print("Course Name:", my_list[2]) #python
print("2nd character in Course Name:", my_list[2][1], end="\n\n") #y

print("Inner list: ", my_list[-1][1]) #(100,200)

print("#"*40, end="\n\n")
#########################################

print("list PART-3")
print("Methods inside list class")

print("_"*20)
#------------------

print(dir(list))

print("#"*40, end="\n\n")
#########################################

print("list PART-4")
print("Count Method")

print("_"*20)
#------------------

my_list= (10,12.5, "python", "python", "python" ,(100, 200))
print("my_list:", my_list, end="\n\n")

count_of_python = my_list.count("python")
print("count_of_python: ", count_of_python)

print("#"*40, end="\n\n")
#########################################


