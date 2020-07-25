# 최소값 구하기
# numberlist 에서 최소값을 구하는데
# min() 사용 x

import random

def minAnswer(param1_list):
    asd = param1_list[0]
    for num in param1_list[1:]:

        if num < asd:
            asd = num
    return asd

for _ in range(0,10):
    numlist = []

    for x in range(0,10):
        numberGen = random.randint(0,10)
        numlist.append(numberGen)

    print(numlist)
    ans = minAnswer(numlist)
    print("MIN NUMBE :" , ans)
    del numlist
