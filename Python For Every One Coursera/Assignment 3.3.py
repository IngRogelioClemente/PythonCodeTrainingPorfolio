score = input("Enter score between 0.0 and 1.0: ")
s = float(score)

if s > 1.0:
    print("Error, please enter a score between 0.0 and 1.0")
    quit()
elif s < 0.0: 
    print("Error, please enter a score between 0.0 and 1.0")
    quit()
elif s >=.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s < 0.6:
    print("F")
