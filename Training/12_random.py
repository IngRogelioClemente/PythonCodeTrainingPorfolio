import random

r = ["Heads","Tails"]
for i in range(1):
    print(random.choice(r))

coin_size = random.randint(0, 1)

if (coin_size == 1):
    print("Heads")
else:
    print("Tails")