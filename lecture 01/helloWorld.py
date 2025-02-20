print("hello world");
print ("my name is Amna", "i'm 18 years old")
print(18)
print (23 + 8)
print(4 * 5)


# variables

name = "Amna";
age = 18
birthday = 20

print (name , age , birthday)

print ("my name is:" , name) 
print ("my age is: " , age )

# data types

print(type(name))
print(type(age))
print(type(birthday))

name1 = 'amna';
name2 = "amna"
name3 = '''amna'''

print(name1)
print(name2)
print(name3)

boolean = True
none = None
numberFloat = 0.54
number = 44

print(boolean)
print(none)
print(numberFloat)
print(number)

print(type(boolean))
print(type(none))
print(type(numberFloat))
print(type(number))


# printing sums

num1 = 8
num2 = 6
diff = num1 + num2
print(diff)
print(num1 + num2 )
print(num1 -num2)
print(num1 % num2)
print(num1 / num2)
print(num1 * num2)

# operators


# arithmetic operator
a = 5
b = 4
print(a + b )
print(a - b)
print(a % b)
print(a / b)
print(a * b) #remainder
print(a ** b ) #a^b 


# relational operator

a = 50
b = 60

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)



# assignment operator
a = 9
# a = a + 44 
a+= 44
print(a)

# logical operator
print(not False)
print(not True)
print(not(a > b))

value1 = True
value2 = False
print("value AND:",value1 and value2)
print("value OR:",value1 or value2)
print("values are:", (a == b) and (a != b))
print("values are:", (a == b) or (a != b))



# type conversion
a = float(5)
d = str(5)
c = int("5")
b = 5.25
sum = a + b
print(type(a))
print(type(d))
print(type(c))

print(sum)


num = 3.66
num = str(3.66)
print(type(num))

# inputs

input("enter your name: ")

name = input("enter your name: ")
print("welcome" , name)

# always return str
val = input("enter value")
print("enterd value:" ,  type(val) , val)

# if want another type 

numInput = int(input("enter num"));
print("entered num" , type(numInput) , numInput)

FloatInput = float(input("enter num"));
print("entered num" , type(FloatInput) , FloatInput)


# small exercise

name = str(input("enter name"))
age = int(input("enter age"))
marks = float(input("enter marks"))

print(type(name) , "welcome" "your name is: " , name)
print(type(age) , "your age is: " , age)
print(type(marks) , "your marks are: " , marks)


# practice questions :
# write a program to input 2 numbers & print their sums

input1 = input("enter number one")
input2 = input("enter number two")

print("result:" , input1 + input2)

input1 = int(input("enter number one"))
input2 = int(input("enter number two"))

print("result:" , input1 - input2)
print("result:" , input1 / input2)
print("result:" , input1 * input2)


# write a program to input a side of square & print its area


side = float(input("enter square side"))

print("area of sqaure is:" , side * side)



# write a program of 2 floating numbers and print their average

x= float(input("enter number one"))
y = float(input("enter number two"))

print("answer: " , (x+y)/2 )


# write a program of 2 int numbers a and b 
# print true if eqaul than or greater than b , if not print false




int1 = int(input("enter number one"))
int2 = int(input("enter number two"))
print(a>=b)