import random
import turtle
t = turtle.Turtle()
t.shape("turtle")

def produceNum():
    for i in range (5): # 랜덤4자리출력 테스트용 반복문
        num = []
        num.append(random.randint(1, 9))
        for i in range (3):
            num.append(random.randint(0, 9))
        answer = int((num[0] * 1000) + (num[1] * 100) + (num[2] * 10) + (num[3] * 1))
        print(answer)

def inputNum():
    user = int(input("4자리 정수를 입력하세요 : "))
    user_num = []
    user_num.append(user // 1000)
    user_num.append(user % 1000 // 100)
    user_num.append(user % 1000 % 100 // 10)
    user_num.append(user % 1000 % 100 % 10)
    if (user_num[0] == 0):
        print("ERROR : 4자리 정수만 입력해주세요")
    else:
        print(user_num)
    t.write(user, font=('Consolas', 16, 'bold'))

produceNum()
inputNum()

