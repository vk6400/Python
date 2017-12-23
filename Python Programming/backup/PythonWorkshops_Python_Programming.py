
# coding: utf-8

# # Intro to Python 
# 
# ### Copyright by PythonWorkshops

# Python is easy to learn, understand and debug
# 
# Python is interpreted, that means

# In[ ]:


15 * 5 + 10 * 6


# In[ ]:


16384/1024


# code is executed line by line. 
# 
# We don't need a main function or standard structure to run code in python.

# ## Install Python

# Download and Install [Python Annaconda](https://docs.anaconda.com/anaconda/install/)
# 
# Incase if you have any trouble with Installation, [First search here](https://stackoverflow.com)
# 
# Open Anaconda Navigator > Launch Jupyter > New-Notebook-Python3

# ### What are we going to learn 
# 
#  [First program](#First-Program)<br>
#  [Variables and Types](#Variables-and-Types)<br>
#  [Numbers and Math](#Numbers-and-Math)<br>
#  [Input from users](#Input-from-users)<br>
#  [Passing arguments](#Passing-Arguments)<br>
#  [Indentation and Block of code](#Indentation-and-Block-of-code)<br>
#  [Functions, Parameters, Returns](#Functions,-Parameters,-Returns)<br>
#  [Conditional statements - If elif else](#Conditional-statements---If-elif-else)<br>
#  [Loops - For and While](#Loops---For-and-While) <br>
#  [Lists](#Lists)<br>
#  [Tuples](#Tuples)<br>
#  [Dictonaries](#Dictonaries)<br>
#  [Sets](#Sets)<br>
#  [Strings](#Strings)<br>
#  [File operations](#File-operations)<br>
#  [Exception handling](#Exception-handling)<br>
#  [Python Project](#Python-Project)<br>
#  

# # First Program 

# In[ ]:


print("I want to learn Python")
print("I love programming")
print("This is the way to print output in Python")


# ### Complete  [Try it #01](PythonWorkshops_Python_Excercises.ipynb#Try-it-#01)
# 

# # Variables and Types 
# 
# Variables are used to store & access data<br>
# Most of the programs are targeted at processing data, in such programs we need to access store and output different kinds of data. <br>
# Variables with specific Types are useful in such cases. Find examples below. 
# 

# In[ ]:


x = 10
y = 20 
print(x)
print(y)


# In[ ]:


#to know the type of a variable we will use type method as below
print("type of x is ",type(x))
a = 10.0
print("type of a is ",type(a))
b = "python"
print("type of b is ",type(b))
c = True
print("type of c is ",type(c))




# As you see variables are not tightly coupled with types, see below example on how a single variable will change types basing on input value. 

# In[ ]:


x = 10
print("type of x is ",type(x))
x = 2.3
print("type of x is ",type(x))
x = "sameVariableName"
print("type of x is ",type(x))
x = False
print("type of x is ",type(x))
#Null in Python is represented as None 
x=None


# In[ ]:


#create your own set of variables and assign some values


# ### Type Conversions 
# In some situation , we need to convert one type to other for doing some operation. 
# 
# Predefined methods may return specific type , but for processing or calculations we may need to convert. 

# In[ ]:


str = "1"
print("type of str is ",str, " - ", type(str))

#Converted to int
print("type of int(str) is ",int(str), " - ",type(int(str)))

#Converted to float
print("type of float(str) is ",float(str), " - ",type(float(str)))

#Converted to bolean
print("type of bool(str) is ",bool(str), " - ",type(bool(str)))


# In[ ]:


#Find the types of your variables


# ### Complete  [Try it #02](PythonWorkshops_Python_Excercises.ipynb#Try-it-#02)
# 

# # Indentation and Block of code
# 
# Python strictly follows indentation in its code, other programing languages suggests Indentation as a good practice. But in python non indenteded code may throw errors <br><br>
# 
# [What is the use of Indentation ?](http://mrbool.com/importance-of-code-indentation/29079)<br><br>
# 
# We indent code in python by adding four spaces to the previous command line's starting position<br><br>
# a,b,c<br>
# ....h,i,j<br>
# ........u,v,w<br>
# ........x,y,z<br>
# ....k,l,m<br>
# e,f,g<br>
# 
# ** . is representing a space<br><br>
# 
# In above example, <br>
# a,b,c<br>
# e,f,g are with same indentation <br>
# 
# h,i,j<br>
# k,l,m are with same indentation <br>
# 
# x,y,z are with same indentation <br>
# 
# So block of code is group of lines with same indentation (x spaces)  until the line which has less than x spaces is written,<br> 
# for example: <br>
# Block of code started at h,i,j (4 spaces) and is there till (k,l,m) when next line e,f,g has only 0(less than 4) spaces. <br>
# Block of code started at u,v,w (8 spaces) and is there till (x,y,z) when next line k,l,m has only 4(less than 8) spaces. <br><br>
# 
# 
# 
# 
# 
# 

# # Numbers and Math
# 
# Calculations are core part of Programing (Data processing) <br>
# How many users registered today ? <br>
# What is the final bill with shipping ? <br> 
# Total number of Visitors to the website ? 

# In[ ]:


#Registered: 15 users each in 8 centers
15*8


# In[ ]:


#Final Bill: 4 items of 12, 26, 29, 32 each and Shipping of 20
12 + 26 + 29 + 32 + 20


# ## Lets learn few python operators we can use with numbers

# ### Arthmetic Operators

# In[ ]:


a = 6
b = 12
print("For given a =", a," For given b =", b)
# + # Addition operator
print("a+b = ",a+b)

# - # Substraction operator
print ("a-b = ",a-b)

# * # Multiplication operator
print ("a*b = ",a*b)

# / # Division operator
print ("a/b = ",a/b)

# % # Modulus operator
print ("a%b = ",a%b)

# // # Floor Division operator
print ("a//b = ",a//b)

# ** # Exponent operator
print ("a**b = ",a**b)


# ### Complete  [Try it #03](PythonWorkshops_Python_Excercises.ipynb#Try-it-#03)
# 

# ### Comparission Operators

# In[ ]:


x = 10
y = 12

print("For given x =", x," For given y =", y)
# Output: x > y is False
print('x > y  is',x>y)

# Output: x < y is True
print('x < y  is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)
print("\n")


# ### Booleans
# 
# All Logical operators expression will return boolean output either True or False 
# So we will use statements with these operators to make decisions or flow of the overall program. 

# ### Complete  [Try it #04](PythonWorkshops_Python_Excercises.ipynb#Try-it-#04)

# ### Logical Operators

# In[ ]:


x = 10
y = 20
z = 10
print("For given x =", x," For given y =", y," For given z =", z)

print('x > z and y > z is',x > z and y > z)

print('x > z or y > z is',x > z or y > z)

print('not x > z is',not x > z)
print("\n")


# ### Complete  [Try it #05](PythonWorkshops_Python_Excercises.ipynb#Try-it-#05)

# ### Bitwise Operators
# 
# Bitwise operators act on operands as if they were string of binary digits. It operates bit by bit, hence the name.
# 
# For example, 2 is <i>010</i> in binary and 6 is <i>110</i>.

# In[ ]:


x = 2
y = 6

print("For given x =", x," For given y =", y)

# & # Bitwise And operator
print("x&y = ",x&y, " 010 & 110 = 010")

# | # Bitwise or operator
print("x|y = ",x|y, " 010 | 110 = 110")

# ^ # Bitwise Xor operator
print("x^y = ",x^y, " 010 ^ 110 = 010")

# ~ # Bitwise not operator
print("~x = ",~x, " ~ 010 = 101")

# >> # Bitwise Right Shift operator
print("x>>1 = ",x>>1, "010 >> 1 = 001")

# << # Bitwise Left Shift operator
print("x<<1 = ",x<<1, "010 << 10")
print("\n")


# ### Complete  [Try it #06](PythonWorkshops_Python_Excercises.ipynb#Try-it-#06)
# 

# ### Assignment operator
# We have already seen the assignment operator in above examples<br>
# a = 25<br>
# because of above statement variable a takes the value 25 and type int<br>
# 
# Similarly above Arthimetic and Bitwise operators can also be applied with assignment operator as shorter version as shown below

# In[ ]:


a = 25
b = 15

#Arthimetic and Bitwise operators along with Assignment
a *= 4
print("a *= 4 is ",a,"\n that is equal to a = a*4")

b **= 2
print("b **= 2", b,"\n that is equal to b = b**2")


a ^= 4
print("a ^= 4 is ",a,"\n that is equal to a = a^4")

b &= 2
print("b &= 2", b,"\n that is equal to b = b&2")



# In[ ]:


#using assignment operator increase a by 1 


# ### Identity Operators
# 
# is and is not are used to verify the type or class of variable as shown in the below example

# In[ ]:


x = 10
print("x value is ",x)
print(type(x) is int)
print(type(x) is float)
print(type(x) is str)

x = "python"
print("x value is ",x)
print(type(x) is not int)
print(type(x) is not float)
print(type(x) is not str)
print(type(x) is str)


# In[ ]:


#variables you created before check if they are int or not ?


# ### Membership operators
# 
# in and not in are used to find out if the x value is present in y<br>
# Please check the examples below

# In[ ]:


x = 'a'
y = 'raja'
z = 'b'
print(x in y)
print(z not in y)


# In[ ]:


#check if string y has a , e , i, o or u 


# We will see more about membership operators along with Python datastructures.

# ## Input from users
# 

# In[ ]:


#To take input from users
no_of_prods = input("Enter the number of products: ")


# input method will return string by default, you need to [convert the type](#Type-Conversions) as per requirement. 

# In[ ]:


bill_amount = int(no_of_prods)*30
print("You need to pay - ",bill_amount)


# In[ ]:


#take input from user if he liked python workshop so far


# ### Complete  [Try it #07](PythonWorkshops_Python_Excercises.ipynb#Try-it-#07)
# 

# ## Passing Arguments
# 
# Python code could be written in files and usually stored with extension <filename>.py<br>
# To execute python code in a file, we run python <filename>.py <br>
# For example: <br>
# We want to create python file which can print bill from Input from users section <br>
# open your code editor or notepad and copy paste your code <br><br>
# 
# #To take input from users<br>
# no_of_prods = input("Enter the number of products: ")<br>
# bill_amount = int(no_of_prods)*30<br>
# print("You need to pay - ",bill_amount)<br><br>
# 
# save it as printBill.py<br><br>
# 
# open command prompt/terminal, go to the path where you saved the file<br>
# run command <i>python printBill.py</i><br>
## Add an image here with the output screen in documents folder. 
# For the above case , we have hardcoded the product cost as 30, lets say we want to pass custom price for every bill<br>
# we need to pass the product cost for every execution, as below <br>
# run command <i>python printBill.py 25</i><br><br>
# 
# Good we know, how to pass an argument, but we are yet to figure out how to access the value in the program<br><br>
# 
# add below lines to the program<br><br>
# 
# import sys<br>
# #This is how to import [python libraries](https://docs.python.org/3/library)<br>
# #details of [sys library](https://docs.python.org/3/library/sys.html)<br>
# #sys.argv[0] --> program name<br>
# #sys.argv[1]-> first argument<br>
# #sys.argv[2-> second argument<br><br>
# 
# #argument is by default a string so we need to convert it<br>
# product_price = int(sys.argv[1])<br><br>
# 
# #To take input from users<br>
# no_of_prods = input("Enter the number of products: ")<br>
# bill_amount = int(no_of_prods)*product_price<br>
# print("You need to pay - ",bill_amount)<br><br>

# ### Complete  [Try it #08](PythonWorkshops_Python_Excercises.ipynb#Try-it-#08)
# 

# ## Functions, Parameters, Returns
# 
# Functions are a block of code written to solve some purpose, to reuse the same block of code and to increase the overall readability of the code. <br>
# 
# We have already used few functions like print, type, int, str, float etc. These are all predefined functions(available in Python libraries)<br>
# 
# But what if we want to define our own function, <br>
# 
# For example: Lets say, we want a fucntion which will apply discount on a given bill amount and return the effective amount post discount. <br>
# we will define a function as below 
# 

# In[ ]:


def apply_discount():
    discount = 10
    final_amount = amount - (amount*discount)/100
    return final_amount


# So defining function is one part and access it is the other part. How do we call the above method is as given below. 

# In[ ]:


bill_amount = apply_discount()


# oh bad it failed, what is the problem ? <br>
# Yes, to apply discount, Function needs to know what is the bill amount. So there needs to be way to pass values to function<br<
# as below

# In[ ]:


def apply_discount(amount):
    discount = 10
    final_amount = amount - (amount*discount)/100
    return final_amount

#To take input from users
no_of_prods = input("Enter the number of products: ")

bill_amount = int(no_of_prods)*30
print("Your bill before discount - ",bill_amount)

final_bill_amount = apply_discount(bill_amount)
print("Your Final bill after discount - ",final_bill_amount)
print("you saved - ",bill_amount - final_bill_amount)



# What if you want to apply discount also dynamically as per customer. 

# In[ ]:


#Below is a function defintion 
def apply_discount(amount,discount):
    #amount and discount are he parameters to the function
    final_amount = amount - (amount*discount)/100
    #final_amount is the return value from function, if there is nothing you can say return None
    return final_amount

#To take input from users
no_of_prods = input("Enter the number of products: ")

bill_amount = int(no_of_prods)*30
print("Your bill before discount - ",bill_amount)
#This is how the function call with arguments or parameters will work  
final_bill_amount = apply_discount(bill_amount,20)
print("Your Final bill after discount - ",final_bill_amount)
print("you saved - ",bill_amount - final_bill_amount)


# In[ ]:


# Write a function that will take mobile number input from user 
# and return last 2 digits of the mobile number


# ### Complete  [Try it #09](PythonWorkshops_Python_Excercises.ipynb#Try-it-#09)
# 

# ## Conditional statements - If elif else
# 
# Following above example of billing system, <br>
# 
# we assumed there is only one product and hardcoded the cost, what if there are three products 'A', 'B', 'C' with 10, 20, 30 cost respectively. So basing on which product he has taken we need to pick the cost. <br>
# 
# So we use if , elif and else statement here as below<br>
# 
# if(<i>condition1</i>):<br>
#     #block_of_code1<br>
# elif(<i>condition2</i>):<br>
#     #block_of_code2<br>
# else:<br>
#     #block_of_code3<br>
#     
# Above code does this, <br>
# If condition1 is correct it will execute block_of_code1<br>
# else-if(elif) (condition1 is wrong -)condition2 is correct it will execute block_of_code2<br>
# else alone used at the end represents both condition1 and condition2 are false<br>
# 

# In[ ]:


cost_A = 10
cost_B = 20
cost_C = 30

#Below is a function defintion 
def apply_discount(amount,discount):
    #amount and discount are he parameters to the function
    final_amount = amount - (amount*discount)/100
    #final_amount is the return value from function, if there is nothing you can say return None
    return final_amount

#To take input from users
product_name  = input("Enter the product Name, A, B, C: ")
no_of_prods = input("Enter the number of products: ")
if(product_name == "A"):
    bill_amount = int(no_of_prods)*cost_A
elif(product_name == "B"):
    bill_amount = int(no_of_prods)*cost_B
elif(product_name == "C"):
    bill_amount = int(no_of_prods)*cost_C
else:
    bill_amount = int(no_of_prods)*30


print("Your bill before discount - ",bill_amount)
#This is how the function call with arguments or parameters will work  
final_bill_amount = apply_discount(bill_amount,20)
print("Your Final bill after discount - ",final_bill_amount)
print("you saved - ",bill_amount - final_bill_amount)


# In[ ]:


#Take input of age from first person

#Take input of age from second person 

#write code which will print below output 
#first person is elder to second
#or
#second person is elder to first
#Both are of the same age

#use if, elif and else


# ## Loops - For and While 
# 
# Continuing above example of billing system,<br>
# we had a key assumption, Somu can buy only one product A or B or C<br>
# What if Somu want to buy 1 or 2 or 3 type of the products at the same time.<br>
# 
# So when ever there is situation where we need to repeat an action multiple times basing on condition or data, we will use loops<br>
# Check the example below, 
# Lets say Somu is in quick counter where they allow only 5 items for billing

# In[ ]:


cost_A = 10
cost_B = 20
cost_C = 30
bill_amount = 0
#Below is a function defintion 
def apply_discount(amount,discount):
    #amount and discount are he parameters to the function
    final_amount = amount - (amount*discount)/100
    #final_amount is the return value from function, if there is nothing you can say return None
    return final_amount

for i in range(5):
    #To take input from users
    product_name  = input("Enter the product Name, A, B, C: ")
    no_of_prods = input("Enter the number of products: ")
    if(product_name == "A"):
        bill_amount += int(no_of_prods)*cost_A
    elif(product_name == "B"):
        bill_amount += int(no_of_prods)*cost_B
    elif(product_name == "C"):
        bill_amount += int(no_of_prods)*cost_C
    else:
        bill_amount += int(no_of_prods)*30
    


print("\nYour bill before discount - ",bill_amount)
#This is how the function call with arguments or parameters will work  
final_bill_amount = apply_discount(bill_amount,20)
print("Your Final bill after discount - ",final_bill_amount)
print("you saved - ",bill_amount - final_bill_amount)


# What if Somu picks more than 5 items and we dont know, how many items are present. how do we do billing ? 

# In[ ]:


cost_A = 10
cost_B = 20
cost_C = 30
more = "1"
bill_amount = 0
#Below is a function defintion 
def apply_discount(amount,discount):
    #amount and discount are he parameters to the function
    final_amount = amount - (amount*discount)/100
    #final_amount is the return value from function, if there is nothing you can say return None
    return final_amount

while(more == "1" or more =="Yes"):
    #To take input from users
    product_name  = input("Enter the product Name, A, B, C: ")
    no_of_prods = input("Enter the number of products: ")
    if(product_name == "A"):
        bill_amount += int(no_of_prods)*cost_A
    elif(product_name == "B"):
        bill_amount += int(no_of_prods)*cost_B
    elif(product_name == "C"):
        bill_amount += int(no_of_prods)*cost_C
    else:
        bill_amount += int(no_of_prods)*30
    more=input("Do you need more products? 1-Yes or 0-No ")


print("\nYour bill before discount - ",bill_amount)
#This is how the function call with arguments or parameters will work  
final_bill_amount = apply_discount(bill_amount,20)
print("Your Final bill after discount - ",final_bill_amount)
print("you saved - ",bill_amount - final_bill_amount)


# In[ ]:


#Write a program, which will ask user for input 

#Print if the number is even or odd 

#if the input number is 0 , exit the loop

#Use while loop


# * For Loop<br>
# Mostly used for access of data and processing as searching etc. <br>
# <img src="https://www.tutorialspoint.com/python/images/python_for_loop.jpg">
# 
# 
# 
# * While Loop<br>
# condition most of the times uses logical operators along with some data.<br>
# <img src="https://www.tutorialspoint.com/python/images/loop_architecture.jpg">
# 
# 

# Good, you helped Somu buy things in a super market, for both 5 items and items more than 5. <br><br>
# But 5 items section we are assuming that he will be taking 5 items, but normally it can also be less than 5 items. <br>
# 
# If you run the code with For loop, even though it has less than 5 items, it asks for 5 items. TO fix it, as in while loop, in for loop also we can break in between through <i> break </i> command.<br>
# We can also handle scenario where the product name is not in the list, we need to ignore it and ask for next product. we use <i> continue </i> command for it. 

# In[ ]:


cost_A = 10
cost_B = 20
cost_C = 30
bill_amount = 0
#Below is a function defintion 
def apply_discount(amount,discount):
    #amount and discount are he parameters to the function
    final_amount = amount - (amount*discount)/100
    #final_amount is the return value from function, if there is nothing you can say return None
    return final_amount

for i in range(5):
    #To take input from users
    product_name  = input("Enter the product Name, A, B, C, NM(No more): ")
    if(product_name == "NM"):
        break
    elif(product_name != "A" and product_name != "B" and product_name != "C" ):
        print("Invalid product Name, check it again - ",product_name)
        continue
    no_of_prods = input("Enter the number of products: ")
    if(product_name == "A"):
        bill_amount += int(no_of_prods)*cost_A
    elif(product_name == "B"):
        bill_amount += int(no_of_prods)*cost_B
    elif(product_name == "C"):
        bill_amount += int(no_of_prods)*cost_C
    else:
        bill_amount += int(no_of_prods)*30
    
    


print("\nYour bill before discount - ",bill_amount)
#This is how the function call with arguments or parameters will work  
final_bill_amount = apply_discount(bill_amount,20)
print("Your Final bill after discount - ",final_bill_amount)
print("you saved - ",bill_amount - final_bill_amount)


# In[ ]:



#loop through 0 to 35 and print all 3 multiples

#use for loop and if statement


# ### Complete  [Try it #10](PythonWorkshops_Python_Excercises.ipynb#Try-it-#10)
# 

# ## Data Structures 

# ### [Lists](PythonWorkshops_Python_Lists.ipynb)

# ## Tuples
#  Tuples are unmutable Lists, They cant be updated <br>
#  starts with ( and end with ), has data with , seperated values - (1,2,3,4)<br>
#  

# In[ ]:


new_tuple = ()
print(new_tuple)
new_tuple = (1)
print(new_tuple)


# In[ ]:


#but updating and removing a element in tuple is not possible
new_tuple[0] = 10

del new_tuple[0]

#Above statements will throw errors


# In[ ]:


#By default python takes it as a tuple , not a list 
second_tuple = 1,2,3,4
print(second_tuple)


# * For more info about tuples fucntions [refer this link](https://docs.python.org/3/library/stdtypes.html#tuple)

# ### Complete  [Try it #11](PythonWorkshops_Python_Excercises.ipynb#Try-it-#11)
# 

# ### [Dictionaries](PythonWorkshops_Python_Dictionaries.ipynb)

# ###  Sets
# 
# A set object is an unordered collection of distinct hashable objects. Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference.<br>
# 
# For more detailed info on Sets [Refer here](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

# In[ ]:


first_set = set([1,2,3,3,1,2,4,5])
second_set = set([22,4,1,8,9,9])


# In[ ]:


print(len(first_set))

print(3 in second_set)

print(first_set.issubset(second_set))


# #### Functions on Sets

# In[ ]:


print(first_set.union(second_set))

print(first_set.intersection(second_set))

print(second_set.difference(first_set))

#Few more functions on sets Add, Remove, Discard, Clear


# * To get more details and function details on Sets, [Refer to this link](https://docs.python.org/3/library/stdtypes.html#set)

# ### [Strings](PythonWorkshops_Python_Strings.ipynb)

# ### File operations
# 
# This section deals with how you can read a file , write to a file and other operations. <br>
# 
# Writing to a File

# In[ ]:


#open a file with certain access
file_access = open('learn_python.txt','w+')

file_access.write("I am writing this string to the file through file object")

print(file_access.name)

#clsoe the file object
file_access.close()


# Reading from a File

# In[ ]:


import os
file_again = open('learn_python.txt','r+')

#read method can take argument which will tell how many character needs to be read, if not specified it will read everything. 
print(file_again.read(15))
#os.getcwd()    
file_again.close();


# In[ ]:


import os
#os level file operations

#renaming file name 
os.rename("learn_python.txt","learnpython.txt")

#Deleting the file
os.remove("learnpython.txt")

#Create directory
os.mkdir("pythondir")

#get present working director
print(os.getcwd())

#changing the director
os.chdir("pythondir")


# ### Complete  [Try it #14](PythonWorkshops_Python_Excercises.ipynb#Try-it-#14)
# 

# 
# ### Exception handling

# In[ ]:


try:
    print("useless"+3)
    # Change plus to multiplication operator * to see different output
except IOError:
    print("IO Error")
except Exception as inst:
    print("Exception",type(inst),inst)
else: 
    print("If there is no Exception")
finally: 
    print("If there is a exception or not this Finally will get executed.")


# To see list of built in Exception , you can use the below link<br>
# [Python Builtin Exception](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)

# ### Complete  [Try it #15](PythonWorkshops_Python_Excercises.ipynb#Try-it-#15)
# 

# * For official reference of Python [Refer this link](https://docs.python.org/3/library/index.html)

# ## Python Project 

# Now that you have completed the python practice of all basic commands and their usage. And after you have completed  and uploaded the Excercises Solutions. Lets do what ever we have learnt to work<br><br>
# 
# [Click on this link and Complete the Project.](PythonWorkshops_Python_Project.ipynb) 
# 
