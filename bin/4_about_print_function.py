"""

About print function

"""

print("print function PART-1")
print("Using 'sep' in print function")
print("_"*20)

#-----------

a=100
b=200
c=300
d=400

print(a,b,c,d) #default sep=" ", In output, it will print each value separated by space
print(a,b,c,d,sep="ABCD") #In output, it will print each value separated by ABCD
print(a,b,c,d,end=".") #In output, After printing all the vlaues, at the end put"."
print(a,b,c,d,sep=",") #In output, it will print each value separated by comma


#We can pass two more arguments to 'Print'
# 1)flush 2)file
# These 2 options, we will duscuss during file operations


print("#"*40,end="\n\n")
