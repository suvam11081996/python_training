"""

"""

print("Strings PART-1")
print("How to store the Values")
print("_"*20)

#-----------

my_string_1 = 'PERSON'
#internally it will create object of builtin class'str' and store the values

#We can also use class name
my_string_2 = str('PERSON')

my_string_3 = "PERSON'S'"
my_string_4 = '''PERSON'S HEIGHT IS XYZ" ("REPRESENTS inch)'''
my_string_5 = """PERSON'S HEIGHT IS XYZ" ("REPRESENTS inch)"""

#Multi line commens are strings only but not stored in any variable

print(my_string_1, my_string_2, my_string_3, my_string_4, my_string_5, sep="\n")

print("#", end="\n\n")

####################


print("Strings PART-2")
print("How to store the Values")
print("_"*20)

#-----------

my_string_1 = "C:\newfolder\test.py"
# Bt default \n\t will get replaced with newline, tab space etc

print("my_string_1=", my_string_1, end="\n\n")

my_string_2 = r"C:\newfolder\test.py"
# r-> RAW STRING, Don't replace \n\t with newline, tab space etc

print("my_string_2:", my_string_2)


print("#", end="\n\n")

####################

print("Strings PART-3")
print("How to store the Values")
print("_"*20)

#-----------

x=10
y=20
z=x+y

my_string = f"Add of {x} and {y} is {z}"

# f-> format
# f-> replce {} with value

print("my_string=", my_string)



print("#", end="\n\n")

####################

print("Strings PART-4")
print("How to store the Values")
print("_"*20)

#-----------



my_string = "WEL COME"



print("my_string=", my_string, end="\n\n")

#Refer Section-1 in 7_Strings.xlsx

print("1st character of +ve index number:", my_string[1])
print("7th character of -ve index number:", my_string[-7], end="\n\n")



print("#", end="\n\n")

####################

print("Strings PART-5")
print("Slicing: Getting Substring")
print("_"*20)

#-----------



my_string = "WEL COME"



print("my_string=", my_string, end="\n\n")

#Refer Section-1 in 7_Strings.xlsx

print("substring from index-1 to index-6 using +ve index number:", my_string[1:6])
print("substring from index-1 to index-6 using -ve index number:", my_string[-7:-2], end="\n\n")


print("substring from Begining to index-6 using +ve index number:", my_string[:6])


print("substring from Begining to end index-1 to index-6 using +ve index number:", my_string[:], end="\n\n")




print("#", end="\n\n")

####################



print("Strings PART-6")
print("Step Value: Skip Character in Between")
print("_"*20)

#-----------



my_string = "WEL COME"



print("my_string=", my_string, end="\n\n")

#Refer Section-1 in 7_Strings.xlsx

print("substring from index-1 to index-6 using +ve index number, default step by=1 :", my_string[1:6])
print("substring from index-1 to index-6 using -ve index number, default step by=1 :", my_string[-7:-2], end="\n\n")

#Step = 1 which means from index-1 to 6 give me every character


print("substring from index-1 to index-6 using +ve index number, default step by=1 :", my_string[1:6:1])
print("substring from index-1 to index-6 using -ve index number, default step by=1 :", my_string[-7:-2:1], end="\n\n")

#Step = 1 which means from index-1 to 6 give me every character

print("substring from index-1 to index-6 using +ve index number, default step by=2 :", my_string[1:6:2])
print("substring from index-1 to index-6 using -ve index number, default step by=2 :", my_string[-7:-2:2], end="\n\n")

#Step = 2 which means from index-1 to 6 give me every 2nd character

print("substring from index-1 to index-6 using +ve index number, default step by=3 :", my_string[1:6:3])
print("substring from index-1 to index-6 using -ve index number, default step by=3 :", my_string[-7:-2:3], end="\n\n")

#Step = 3 which means from index-1 to 6 give me every 3rd character




print("#", end="\n\n")

####################


print("Strings PART-7")
print("-ve Step Value: Traverse in reverse direction")
print("_"*20)

#-----------



my_string = "WEL COME"

print("my_string=", my_string, end="\n\n")

#Refer Section-1 in 7_Strings.xlsx
#Example: sub string from index -6 to 1 )in Reverse Direction)
# 1) Start Index = 6
# 2) End Index = 1
# 3) Step Value = -1
# All 3 are mandatory

print("substring from index-6 to index-1 using +ve index number, default step by=-1 :", my_string[6:1:-1])
print("substring from index-6 to index-1 using -ve index number, default step by=1 :", my_string[-2:-7:-1], end="\n\n")

#Step = -1 which means from index-6 to 1 give me every character in reverse order (character of end index excluded)

print("substring from index-6 to index-1 using -ve index number, default step by=1 :", my_string[-1:-9:-1], end="\n\n")
print("substring from index-6 to index-1 using -ve index number, default step by=1 :", my_string[ ::-1], end="\n\n")


print("#", end="\n\n")

####################

print("Strings PART-8")
print("methods inside 'str' class")
print("_"*20)

#---------------

print(dir(my_string))
#or
#print(dir(str))

print("#"*40, end="\n\n")
########################################

print("Strings PART-9")
print("learning 'startswith' method")
print("_"*20)

#---------------

my_string = "WEL COME"

print("my_string=", my_string, end="\n\n")

result = my_string.startswith("WEL")
print('my_string.startswith("WEL"):', result) #True/False

print("#"*40, end="\n\n")

################################################

print("Strings PART-10")
print("learning 'split' method")
print("_"*20)

#---------------

my_string = "WEL COME"

print("my_string=", my_string, end="\n\n")

result = my_string.split() #split based on space
print('my_string.split() result:', result) #True/False

print("#"*40, end="\n\n")

#############################################

print("Strings PART-11")
print("learning 'split' method")
print("_"*20)

#---------------

my_string = "WEL COME"

print("my_string=", my_string, end="\n\n")

result = my_string.split("E") #split based on E
print('my_string.split("E") result:', result) #True/False

print("#"*40, end="\n\n")


