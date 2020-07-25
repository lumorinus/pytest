import random
import time



def min(param1_list):
    asd = param1_list[0]
    for num in param1_list[1:]:

        if num < asd:
            asd = num
    return asd

for _ in range(0,10):
    numlist = []
    for x in range(0,10):
        numGen = random.randint(0,10)
        numlist.append(numGen)

    print(numlist)
    ans = min(numlist)
    print("MIN NUMBE :" , ans)
