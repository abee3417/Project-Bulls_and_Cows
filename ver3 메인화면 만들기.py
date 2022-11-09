import random
import turtle
t = turtle.Turtle()
s = turtle.Screen()
num = [] # 랜덤 4자리 숫자를 담는 리스트
user_num = [] # 사용자 선택 4자리 숫자를 담는 리스트
integer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#윤성
def intro(): # 시작화면을 나타내는 함수
    t.speed(0)
    t.penup()
    t.goto(-300, 200)
    t.write("숫자야구 게임", font=('Consolas', 48, 'bold'))
    t.goto(-300, 0)
    t.write("1번키 : 게임시작", font=('Consolas', 24, 'bold'))
    t.goto(-300, -100)
    t.write("2번키 : 기록실", font=('Consolas', 24, 'bold'))
    t.goto(-300, -200)
    t.write("3번키 : 규칙설명", font=('Consolas', 24, 'bold'))
    t.hideturtle()

#윤성
def start(): # 게임진행을 해주는 함수
    t.reset()
    produceNum()
    location = 300
    while True:
        t.hideturtle()
        inputNum()
        result = judgment()
        drawing(result, location)
        location -= 80

#윤성
def produceNum(): # 게임에 사용될 무작위 숫자 4자리를 생성해주는 함수
    num.append(random.randint(1, 9)) # 첫째 자리는 0을 제외한 나머지 숫자중 랜덤으로 선택
    tempcount = 10
    for i in range (tempcount):
        if (num[0] == integer[i]): # 중복되는 숫자는 제거
            integer.remove(integer[i])
            break
    for a in range(1, 4, 1):
        num.append(random.choice(integer)) # 나머지 자리를 0 ~ 9 중 랜덤으로 선택
        for i in range (tempcount):
            if (num[a] == integer[i]):# 중복되는 숫자는 제거
                integer.remove(integer[i])
                tempcount -= 1
                break
    answer = int((num[0] * 1000) + (num[1] * 100) + (num[2] * 10) + (num[3] * 1))
    print("정답 : %s" %answer)

#윤성
def inputNum(): # 사용자에게 4자리 숫자를 입력받는 함수
    user = int(turtle.textinput("", "4자리 정수를 입력하세요 : "))
    user_num.append(user // 1000)
    user_num.append(user % 1000 // 100)
    user_num.append(user % 1000 % 100 // 10)
    user_num.append(user % 1000 % 100 % 10)
    if (user_num[0] == 0):
        t.write("ERROR : 4자리 정수만 입력해주세요", font=('Consolas', 20, 'bold'))
    else:
        print("입력값 : %s" %user)

#형철
def judgment(): # 사용자가 입력한 답이 일치하는지 과정을 판단하는 함수
    
    strike = 0
    ball = 0
    for i in range (0,4):
        for j in range (0,4):
            if(num[i] == user_num[j]):
                if i == j:
                    strike = strike + 1
                else :
                    ball = ball + 1
    return [strike, ball]   #스트라이크랑 볼 수를 리턴

#형철
def drawing(result, location):# 게임진행시 UI를 구성하는 함수
    t.penup()
    t.goto(-200, location)
    t.write("사용자가 입력한 숫자 : %s " %user_num[0:4], font=('Consolas', 15, 'bold'))
    t.goto(-200, location - 30)
    if(result == [0, 0]):
        t.write("아웃입니다.", font = ('Consolas', 15, 'bold'))
    else:
        t.write("스트라이크 수 : %s, 볼 수 : %s" %(result[0], result[1]), font = ('Consolas', 15, 'bold'))
    user_num.clear() # 사용자의 4자리 숫자를 초기화하여 다시 입력할 수 있게끔 한다.

#준호
def explain(): # 규칙설명 UI를 구성하는 함수
    t.reset()
    t.hideturtle()
    t.penup()
    t.goto(-300,300)
    t.write("규칙:",font=('Consolas',24,'bold'))
    t.goto(-300,200)
    t.write("사용되는 숫자는 0에서 9까지 서로 다른 숫자이다.",font=('Consolas',24,'bold'))
    t.goto(-300,100)
    t.write("숫자는 맞지만 위치가 틀렸을 때는 볼.",font=('Consolas',24,'bold'))
    t.goto(-300,0)
    t.write("숫자와 위치가 전부 맞으면 스트라이크.",font=('Consolas',24,'bold'))
    t.goto(-300,-100)
    t.write("숫자와 위치가 전부 틀리면 아웃. 틀렸다는 게 중요하다.",font=('Consolas',24,'bold'))
    t.goto(-300,-200)
    t.write("물론 무엇이 볼이고 스트라이크인지는 알려주지 않는다.",font=('Consolas',24,'bold'))


intro()
s.onkey(start, "1")
s.onkey(explain, "3")

s.listen()
s.mainloop()
