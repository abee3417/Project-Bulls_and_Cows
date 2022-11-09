import random
for i in range (10):
    num = []
    num.append(random.randint(1, 9))
    for i in range (3):
        num.append(random.randint(0, 9))
    answer = int((num[0] * 1000) + (num[1] * 100) + (num[2] * 10) + (num[3] * 1))
    print(answer)
