# EX 1
# 🚨 Don't change the code below 👇
from typing import final


number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num = float(number)

#Even number:
if num % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

#EX 2  BMI 2.0
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / (height * height) 
BMI_ROUND = round(BMI)
if BMI < 18.5:
    print(f"Your BMI is {BMI_ROUND}, you are underweight.")
elif 18.5 < BMI < 25:
    print(f"Your BMI is {BMI_ROUND}, you have a normal weight.")
elif 25 < BMI < 30:
    print(f"Your BMI is {BMI_ROUND}, you are slightly overweight.")
elif 30 < BMI < 35:
    print(f"Your BMI is {BMI_ROUND}, you are obese.")
else:
    print(f"Your BMI is {BMI_ROUND}, you are clinically obese.")

#EX 3 Leap year or Not leap year

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    print("Leap year.")
elif year % 400 == 0:
        print("Leap year.")
elif year % 100 != 0:
        print("Not leap year.")
else:
    print("Not leap year.")

# EX 4

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
size_bill = 0
extra_pepperoni_bill = 0
extra_cheese_bill = 1
final_bill = 0

if size == "S":
    size_bill = 15
    if add_pepperoni == "Y":
        extra_pepperoni_bill = 2
        if extra_cheese == "Y":
            final_bill = size_bill + extra_pepperoni_bill + extra_cheese_bill
            print(f"Your final bill is: ${final_bill}")
        else:
            final_bill = size_bill + extra_pepperoni_bill 
            print(f"Your final bill is: ${final_bill}")

    else:
        if extra_cheese == "Y":
            final_bill = size_bill + extra_cheese_bill
            print(f"Your final bill is: ${final_bill}")
        else:
            print(f"Your final bill is: ${size_bill}")

if size == "M":
    size_bill = 20
    if add_pepperoni == "Y":
        extra_pepperoni_bill = 3
        if extra_cheese == "Y":
            final_bill = size_bill + extra_pepperoni_bill + extra_cheese_bill
            print(f"Your final bill is: ${final_bill}")
        else:
            final_bill = size_bill + extra_pepperoni_bill 
            print(f"Your final bill is: ${final_bill}")

    else:
        if extra_cheese == "Y":
            final_bill = size_bill + extra_cheese_bill
            print(f"Your final bill is: ${final_bill}")
        else:
            print(f"Your final bill is: ${size_bill}")

if size == "L":
    size_bill = 25
    if add_pepperoni == "Y":
        extra_pepperoni_bill = 3
        if extra_cheese == "Y":
            final_bill = size_bill + extra_pepperoni_bill + extra_cheese_bill
            print(f"Your final bill is: ${final_bill}")
        else:
            final_bill = size_bill + extra_pepperoni_bill 
            print(f"Your final bill is: ${final_bill}")

    else:
        if extra_cheese == "Y":
            final_bill = size_bill + extra_cheese_bill
            print(f"Your final bill is: ${final_bill}")
        else:
            print(f"Your final bill is: ${size_bill}")


# EX 5 Love Calculator 

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_strings = name1 + name2
lower_case_string = combined_strings.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
TRUE = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
LOVE = l + o + v + e

love_score = int(str(TRUE) + str(LOVE))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")