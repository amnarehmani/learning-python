# strings
str1 = 'one'
str2= "two"
str3= '''three'''


# using escape sequence character

str1= "hello, welcome. \n my name is Amna";
str2="hello, welcome. \t my name is Amna";
str3= "hello \rworld "
str4= "this is backslash \\"
str5 = "He said, \"Python is great!\"";
str6 = "He said, \'Python is great!\'";
str7= "Oops! Typo\b.";
str8= "Hello World!\rPython";
str9= "Hello\vWorld";
str10="Unicode heart: \u2764";
str11="Hexadecimal A: \x41";

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)
print(str8)
print(str9)
print(str10)
print(str11)


# concatination
name1 = "amna"
name2= "rehmani"
final = name1 + " "  + name2

# lenght 
lenght1 = "lenghtofstring"
print(len(lenght1))
print(len(final))


# indexding 
index = "Amna Rehmani";
ch = index[0]
print(ch)
print(index[5])

# slicing

slicing = "amna rehmani";
print(slicing[1:5])
print(slicing[5:12]) 
# or
print(slicing[5:len(slicing)])
print(slicing[0:len(slicing)])

# negative index
negative="apple";
print(negative[-4:-1])


# sting functions

# lenght
string = "python"
print(len(string)) 

# lowercase
string2 = "PYTHON"
print(string2.lower())

# uppercase
string3 = "python"
print(string3.upper())

#strip
string4 = " python "
print(string.strip())

# replace
string5 = "Hello World"
print(string5.replace("World", "Python")) 


# split
string6 = "apple,banana,mango"
print(string6.split(",")) 

# join
words = ["Hello", "Python"]
print(" ".join(words))  

# find
find = "Hello Python"
print(find.find("Python")) 

# count
count = "mango"
print(count.count("a"))  

# starts with & ends with
print("Python".startswith("Py"))  
print("Python".endswith("on"))    





# practice questions

# write a program to input's users name and print its lenght
firstName = input("enter your first name");
print("your name lenght is:" , len(firstName))


# write a program to find the occurrence of "$" in string
dollarString = "$ is the dollar. and the $78.99 and $98.99"
print("dollar lenght is:" , dollarString.count("$"))

