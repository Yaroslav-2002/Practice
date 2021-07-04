import random
rand = random.sample(range(-100, 100),30)
print(rand)
print("Max element index:", rand.index(max(rand)), max(rand))
for i in range(0,30,1):
    if rand[i]<0:
        if rand[i+1]<0:
            print(rand[i],rand[i+1])

print("hello world")
