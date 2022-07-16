#Enter input values
#The program will output the maximum and minimum value
#If there is a wrong (non valid number) the program will ignore con continue

largest = None
smallest = None

#WHILE LOOP
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try: 
        inum = int(num)
    except:
        print("Invalid input")
        continue

#IF LOOP
    if largest is None or inum > largest:
        largest = inum

    if smallest is None or inum < smallest:
        smallest = inum


#PRINT STATEMENT 
print("Maximum is", largest)
print("Minimum is", smallest)

#By Rogelio Clemente Balderas IMTC

#CLOSE ON WINDOW
input("Press enter to exit")
