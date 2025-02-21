age = 18

if age > 18:
    print("You are an adult.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are a minor.")


age = 23
 
if age >= 23:
    
    print("you can apply for driving license.");
elif age == 23:
    print("you're not eligible");
else:
    print("you're minor")



age = 18 

if(True):
    print("you can vote");


userInput = input("traffic light color")
if(userInput == "red"):
    print("stop.")
elif(userInput == "yellow"):
    print("start.")
elif(userInput == "green"):
    print("go.")
else:
    print("error")





num = -5

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



num = 7

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")



num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")




a = 10
b = 20
c = 15

if a > b and a > c:
    print("A is the largest number.")
elif b > a and b > c:
    print("B is the largest number.")
else:
    print("C is the largest number.")




marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")



num = 25

if 10 <= num <= 50:
    print("The number is within the range.")
else:
    print("The number is out of range.")






age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")



marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# nesting

yourAge = int(input("Enter your age: "))

if yourAge >= 18:
    nationality = input("Are you a citizen? (yes/no): ")
    
    if nationality.lower() == "yes":
        print("You are eligible to vote.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You are not eligible to vote.")






# practice questions

# write a program to check if a number entered by user is odd or even

num = int(input("enter number to check"))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# write a program to find the greatest of 3 numbers entered by the user


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("The largest number is:", a)
elif b > a and b > c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)


# write a program to check if the num is multiple to 7


num = int(input("Enter a number: "))

if num % 7 == 0:
    print(num, "is a multiple of 7.")
else:
    print(num, "is not a multiple of 7.")
