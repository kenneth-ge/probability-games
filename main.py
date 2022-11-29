import random
from user_defined import f

pA = 0.4
pB = 0.6

num_samples = 100000

def gen_from_distribution():
    num = random.random()

    if num < pA:
        return 0

    return 1

print('guessing with a random coin flip')

num_right = 0
num_wrong = 0
for i in range(num_samples):
    item = gen_from_distribution()
    thing = random.choices([0, 1], weights=[1, 1])[0]

    if item == thing:
        num_right += 1
    else:
        num_wrong += 1

print('percent right' , (num_right / (num_right + num_wrong)))

print('guessing with actual probability distribution')

num_right = 0
num_wrong = 0
for i in range(num_samples):
    item = gen_from_distribution()
    thing = random.choices([0, 1], weights=[pA, pB])[0]

    if item == thing:
        num_right += 1
    else:
        num_wrong += 1

print('percent right' , (num_right / (num_right + num_wrong)))
print('calculated probability', pA * pA + pB * pB)

print('guessing based on whichever has a higher probability')

num_right = 0
num_wrong = 0
for i in range(num_samples):
    item = gen_from_distribution()
    thing = random.choices([0, 1], weights=[1 if pA > pB else 0, 1 if pB > pA else 0])[0]

    if item == thing:
        num_right += 1
    else:
        num_wrong += 1

print('percent right' , (num_right / (num_right + num_wrong)))
print('calculated probability', max(pA, pB))

print('guessing based on custom function f(p)')

num_right = 0
num_wrong = 0
for i in range(num_samples):
    item = gen_from_distribution()
    thing = random.choices([0, 1], weights=[1 - f(pB), f(pB)])[0]

    if item == thing:
        num_right += 1
    else:
        num_wrong += 1

print('percent right' , (num_right / (num_right + num_wrong)))
print('calculated probability', pB * f(pB) + pA * (1 - f(pB)))