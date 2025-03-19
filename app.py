'''#Arithematic operators


#additions
num1 : int = 5
num2 : int = 5
sum =(num1+num2)
print(sum)

#substraction
num1 : int = 5
num2 : int = 5
sub =(num1-num2)
print(sub)

#multiplication 
num1 : int = 5
num2 : int = 5
mul =(num1*num2)
print(mul)

#division 
num1 : int = 5
num2 : int = 5
div = (num1/num2)
print (div)

#exponent 
num1 : int = 5
num2 : int = 5
exp =(num1**num2)
print (exp)

#float division 
num1 : int = 5
num2 : int = 5
float =(num1//num2)
print(float)

#remainder modulus 
num1 : int = 5
num2 : int = 5
mod =(num1%num2)
print(mod)

# Assignment operators 
#(=)
x : int =5
x=5
print(x)

x: int = 5
x = x+5
print(x)

x: int =5
x = x - 5
print(x)

x: int = 5
x = x * 5
print (x)

x : int =5
x = x/ 5
print (x)

x : int =5
x = x%5
print(x)

#comparision operators 
#(boolean) true/ false 
#== equal
# >greater than 
# <less than 
# >=greater than or equal to
# <=less than or equal to 
# !=not equal to 

#mera pehla operand/ value dosry operand /value k barabar hai 
num1 : int = 10
num2 : int = 10
print(num1 == num2)

num1 : int = 10
num2 : int = 10
print(num1 > num2)

num1 : int = 10
num2 : int = 10 
print(num1 < num2)

num1 : int = 10
num2 : int = 10
print(num1 >= num2)

num1 : int =10
num2 : int =10
print(num1 <= num2)

num1 : int = 10
num2 : int = 10
print(num1 != num2)

# logical Operators 
# and, or not

#LIST:
Names= ["ali,okasa,bilal,raza"]
print(Names [0])

L=["mango,banana,cherry"]
print(L[0])

#TUPLE:
t=("mango,banana,cherry")
print(t[0])

#Table of five 
for i in range (1,11):
    print(f'{i}')

#TABLE OF FIVE:
for i in range (1,11): 
    print(f"5*{i}={5*i}")

for num in range (1,11):
    print (f"2x{num}={2*num}")


#if else assignment
num1 : int = 2
num2 : int = 1
if num1 > num2:
    print ("hello")
    uname = "sana"
    print(uname)

# table of six
for i in range (1,11):
    print(f"6x{i}={6*i}")

# table of seven
for i in range (1,11):
  print(f"7x{i}={7*i}")

#table of eight
for i in range (1,11):
  print(f"8x{i}={8*i}")

# table of nine 
for i in range (1,11):
  print(f"9x{i}={9*i}")

# table of ten 
for i in range (1,11):
  print(f"10x{i}={10*i}")

#functions:
def charger():
    print("charge mobile")

charger()

def ramokaka():
    print("ramokaka biryani banao")

ramokaka()
# STATIC FUNCTION
a = 1
b = 4
def add():
    return a+b
sum = add()
print(sum)



#DYNAMIC FUNCTION

#          parameter
def greet(name,age,rollno):
    print("assalam o alaikum sir",name,"your age is ",age,"rollno",rollno)

#      arguement                   #arguement ki value store hojae gi parameter me
greet("bilal",20,1234)


# table 14
for i in range (1,11):
    print(f"14 *{i} = {14*i}")

# table of 15
for i in range (1,11):
    print(f"15*{i} = {15*i}")

#if else
num1 :int=10
num2 :int=20
if num1 < num2
print("my")


#string methods : six methods

# replace ,# find, # lenght, # count # capitilaze # index

# replace :
newname = 'my name is sehar and my nationality is pakistan '
print(newname.replace('pakistan','america'))

#index 
newname = 'my name is sehar and my nationality is pakistan'
print(newname.index('and'))

# find 
newname = 'my name is sehar and my nationality is pakistan'
print(newname.find('fatima'))

# lenght
newname = 'my name is sehar and my nationality is pakistan'
print(newname.len(''))
# capitiliaze 
newname = 'my name is sehar and my nationality is pakistan'
print(newname.capitiliaze('pakistan'))








#there are seven methods of list :
#append  # insert # reverse

# revers




#short hand if else / ternary operators
num: int = 10
if num>10:
    print("number is greater than 10")
else:
    print("number is less than 10")


# enumerated function:
names = ["ali,abdullah ,aamir"]
for name in names :
    print(name)

names =["ali,abdullah,amir"]
for index ,num in enumerate(names):
    print(f"name{index}={name}")


numbers = [1,2,3,4,5]
def square (num:int):
    return num*num
print(square (2))



#map:
numbers = [1,2,3,4,5]
def square (num:int):
    return num * num
new_list = list (map(square,numbers))
print("new_list>>>",new_list)

#filter:
numbers = [1,2,3,4,5]
def filter_function(num:int):
    return num > 3
filtered_list = list (filter(filter_function,numbers))
print("filtered_list",filtered_list)

#reduce:
numbers =[1,2,3,4,5]
def reduce (num:int):
    return num > 4
reduce_list = list (reduce(numbers))
print("reduce_list>>>" ,reduce_list)

names =["ali,abdullah,aamir"]
index =0
for name in names:
    print(f"name{index},names")
    index = index +1

for index ,name in enumerate(names):
    if names [index]=="abdullah":
        print("salam abdullah")
    
print(f"name{index}:{name}")

#first we have to take from "funtool" import "reduce "than ,
from functools import reduce
#make a function nd give two parameter like :(x,y):than,
# return the parameter in your condition like :+, -,*,/, than,
def multi (a,r):
    return a * r
# make a list of numbers than :
numbers = [ 1,2,3,4,5]
# make a varaible = and import than reduce and in arguement call (function ,"and write" list)
new_list = reduce(multi,numbers )
# than print the varaibles
print (new_list)

# REDUCE :
from functools import reduce 
def multi (a,r):
    return a * r
numbers = [1,2,3,4,5]
new_list= reduce(multi,numbers)
print(new_list)


# to use reduce first we import reduce :
from functools import reduce
numbers =[1,2,3,4,5]
def addition (x,y):
    return x+y
result = reduce(addition,numbers)
print("product>>>",result)



#TRIANGKLE PATTERN USING NESTED LOOP
[30]
for a in range (1,8):
    for b in range (1,a+1):
        print(b, end ="  ")
    print()

# PARAMID PATTERN USING NESTED LOOP:
for a in range (1,11):
   for b in range(11-a):
    print(" ", end = " ")
for b in range (1,a):
     print("*", end=" ")
for a in range (a,0,-1):
    print("*",end =" ")
print(" ")'''



'''#try : # except:
try :
    result = num  / num2
    print(result)
except Exception as zerodivisionerror:
    print("there is zero division error")


#add:
names_set = {"sehar,tehreem,zuriyat,samrah,ali"}
names_set.add("syed")
print(names_set)

#import qrcode as qr
img = qr.make("https://github.com/syedasehar")
img.save("SYEDA SEHAR_Github.png")
print(img)


#DOC STRING:
def add(num1:int,num2:int)->int:
    return num1 +num2
result =add (5,7)
print(add.__doc__)
print(result)

# INTERSECTION:
num_set_1 = {1,2,3,4}
num_set_2 = {2,4,5,6,7}
result= num_set_1.intersection(num_set_2)
print("result>>>", result)

# UNION:
num_set_1 = {1,2,3,4}
num_set_2 = {2,4,5,6,7}
result = num_set_1.union(num_set_2)
print("result>>>",result)

#POP:
num_set = {"ali,abdullah,zain"}
num_set.pop
print("print update name", num_set)


# SHORT HAND IF ELSE / TERNARY OPERATORS:

num : int = 9
if num>10:
    print("number is greater than ")
    num = num + 10
    print("num>>>",num)
else:
    print("number is less than ")

# reduce:
def add(a,b):
    return a+b
from functools import reduce
numbers = [1,2,3,4,5,6]
sum = reduce(add,numbers)
print(sum)

def mul(b,a):
    return a*b
from functools import reduce
numbers =[1,2,3,4,5,6]
sub = reduce(mul,numbers)
print(mul)



#GENERAL ERRRORS:
#ZeroDivisionError
#index error
# value error
#import error'''






















