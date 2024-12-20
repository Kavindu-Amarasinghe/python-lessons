import random

a = random.randint(1,100)
print(a)

b = random.randrange(1,100)
print(b)

c = random.random()
print(c)

d = random.uniform(1,9)
print(d)

l = [2,3,4,5,6,7,8,9]
e = random.choice(l)
print(e)

f = random.shuffle(l)
print(f)