#EX 1
# 🚨 Don't change the code below 👇
from gettext import find


two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])
sum = num1 + num2
print(sum)

#EX 2
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
h = float(height)
w = float(weight)
BMI = w / (h*h) 
print(BMI) 

#EX 3 
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_actual = int(age)
age_left = 90 - age_actual

z = age_left * 12 # 1 year = 12 months
y = age_left * 52 # 1 year = 52 weeks
x = age_left * 365 # 1 year = 365 days, 

print("You have ", x, " days, ", y, " weeks, and ", z, " months left.")