#Letter Counter.
#This is just an example of the "looping and counting"

print("This Py code output the amount of a letters in banana word")
word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count = count + 1
print(count)

input("Press enter button to close on window.")