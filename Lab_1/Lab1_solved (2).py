#Lab 1  (First Step in AI word.)
#basic python syntax stuff

print("hello world!")

#comment example
print("1st statement") ;print("2nd statement")

#indentation practice
x=1
if x>0 :
    print("indentation")

#now checking types
a=111
print(type(a)) #int

b=-122
print(type(b)) #still int, negative numbers work too

c=-234.5
print(type(c)) #float

d=3.e33
print(type(d)) #this is also float, scientific notation

#complex numbers, weird but ok
z=1+2j
print(type(z))

x=complex(1,2)
print(type(x))
print(x)

#boolean type
bool1=True
print(type(bool1))

bool2=False
print(type(bool2))

#strings
str1="string_1"
print(str1)

str2='stri"ng_1'
print(str2)

#quote inside quote stuff
str3="Day's"
print(str3)

str4='Day"s'
print(str4)

#special characters, backslash stuff from the pdf
print("The is a backslash (\\) mark.")
print("This is tab \tkey")
print("These are \'single quotes\'")
print("These are \"double quotes\"")
print("This is a new line\nNew line")

#string indexing
string1 = "PYTHON TUTORIAL"
print(string1[0]) #first char
print(string1[-15]) #same thing but from right side
print(string1[14]) #last char
print(string1[-1]) #last char again but negative index
print(string1[4]) #5th letter
print(string1[-11]) #same as above just negative

#slicing a string
print(string1[3:7]) #should give characters 3,4,5,6

#creating list

my_list=[1,2,3]
print(my_list)

my_list1=["red","blue","black"]
print(my_list1)

my_list2=["red",12,112.12] #mixed types in one list
print(my_list2)

empty_list=[]
print(empty_list) #just an empty one

#list indices
color_list=["RED","Blue","Green","Black"]
print(color_list[0]) #first item
print(color_list[0],color_list[3]) #first and last
print(color_list[-1]) #last item, negative index

#list slicing
print(color_list[0:2]) #first two
print(color_list[1:2]) #just second one
print(color_list[1:-2]) #second one again, negative version
print(color_list[:3]) #first three
print(color_list[:]) #basically copies whole list

#conditional statements, from the last part of the pdf
a=5
b=10

if b>a:
    print("b is greater than a")

if a==b:
    print("a is equal to b")
else:
    print("a is not equal to b")

if a!=b:
    print("a is not equal to b")

if a<b:
    print("a is less than b")

if a<=b:
    print("a is less than or equal to b")

if b>=a:
    print("b is greater than or equal to a")

#done with lab 1
#First Step in AI word.
