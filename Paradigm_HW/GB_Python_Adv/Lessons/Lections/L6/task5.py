import random as rnd


START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]
print(rnd.random())
#rnd.seed(42)     # Все будет повторяться.
state = rnd.getstate()
print(rnd.random())
rnd.setstate(state)
print(rnd.random())
print(rnd.randint(START, STOP))
print(rnd.uniform(START, STOP))
print(rnd.choice(data))
print(rnd.randrange(START, STOP, STEP))
print(data, id(data))
rnd.shuffle(data)
print(data, id(data))
print(rnd.sample(data, 2))
print(rnd.sample(data, 7, counts=[1, 1, 10, 1, 1, 100]))   # даем вес

