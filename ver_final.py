import random
import turtle
t = turtle.Turtle()
s = turtle.Screen()
num = [] # 랜덤 4가지 숫자를 담는 리스트
user_num = [] # 사용자 선택 4가지 숫자를 담는 리스트
integer = [] # 정수 리스트 (게임 시작 시 리스트를 1 ~ 9로 채워준다.)
image = "numbaseball.gif" # 로비화면 아이콘
s.addshape(image)


# 시작화면을 나타내는 함수 (윤성 + 준호)
def intro():
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(-300, 200)
    t.write("숫자야구 게임", font=('Consolas', 48, 'bold'))
    t.goto(230, 230)
    t.shape(image)
    t.stamp()
    t.shape("turtle")
    t.goto(-300, 0)
    t.write("1 : 게임시작", font=('Consolas', 24, 'bold')) # 키보드 1입력시
    t.goto(-300, -60)
    t.write("2 : 기록실", font=('Consolas', 24, 'bold')) # 키보드 2입력시
    t.goto(-300, -120)
    t.write("3 : 규칙설명", font=('Consolas', 24, 'bold')) # 키보드 3입력시
    t.goto(-300, -180)
    t.write("X : 게임종료", font=('Consolas', 24, 'bold')) # 키보드 X입력시

    
# 게임진행화면을 나타내는 함수 (윤성 + 형철)
def start():
    t.reset()
    t.hideturtle()
    produceNum()
    location = 0 # 개행 맞추기용 변수
    x_axis = -300 # 기본 가로 시작점
    y_axis = 100 # 기본 세로 시작점
    trial = 0 # 시도 횟수
    while True:
        t.hideturtle()
        # 게임 진행 상황을 보여주는 표를 생성
        # location은 사용자가 숫자를 한번 입력할때마다 +1이 된다.
        if (location >= 1 and location <= 5): # 5가 될때까지 옆으로만 그린다.
            x_axis += 100
        elif (location >= 6): # 6이 되면 x축을 초기화시키고 다음 줄로 넘어가서 그린다.
            location = 0
            x_axis = -300
            y_axis -= 50
        elif (location == -1): # 게임 종료 = location이 -1이 되는 경우로 설정
            gameOver(trial)
            num.clear()
            integer.clear()
            break
            
        errjudge = inputNum(x_axis, y_axis, location)
        if (errjudge == 'no error'): # 에러가 없을 경우
            result = judgment() # 스트라이크와 볼을 판단
            location = drawing(result, x_axis, y_axis, location) # 표를 그릴 위치를 보내줘서 그린다.
            trial += 1 # 시도 횟수 +1
        else: # 에러가 있을 경우
            user_num.clear() # 숫자를 계속 받아야 하므로 사용자 숫자를 초기화
            location = errjudge
    s.listen()

    
# 임의의 4가지 숫자를 뽑는 함수 (윤성)
def produceNum():
    for i in range(1, 10, 1): # 정수 리스트에 1 ~ 9를 채워준다.
        integer.append(i)
    tempcount = 10 # 중복숫자 제거 판단 반복문용 변수
    for a in range(0, 4, 1):
        num.append(random.choice(integer)) # 나머지 자리를 0 ~ 9 중 랜덤으로 선택
        for i in range (tempcount):
            if (num[a] == integer[i]): # 중복되는 숫자는 제거
                integer.remove(integer[i])
                tempcount -= 1
                break
    print("정답 : %s" %num)


# 사용자에게 4가지 숫자를 받는 함수 (윤성)
def inputNum(x_axis, y_axis, location):
    user = int(turtle.textinput("숫자야구", "4자리 정수를 입력하세요"))
    err1 = error1(user, x_axis, y_axis, location) # 에러1 판단
    if (err1 == 'no error'):
        user_num.append(user // 1000)
        user_num.append(user % 1000 // 100)
        user_num.append(user % 1000 % 100 // 10)
        user_num.append(user % 1000 % 100 % 10)
        err2 = error2(user_num, x_axis, y_axis, location) # 에러2 판단
        if (err2 == 'no error'):
            return 'no error'
        else:
            return err2
    else:
        return err1


# 사용자가 입력한 답이 일치하는지 판단하는 함수 (형철)
def judgment():
    
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


# 게임진행 UI를 그리는 함수 (형철)
def drawing(result, x_axis, y_axis, location):
    t.penup()
    t.goto(x_axis, y_axis)
    square()
    answer = int((user_num[0] * 1000) + (user_num[1] * 100) + (user_num[2] * 10) + (user_num[3] * 1))
    t.pencolor("blue")
    t.write(" %s\n" %answer, font=('Consolas', 15, 'bold'))
    t.pencolor("black")
    t.write(" %sS %sB" %(result[0], result[1]), font=('Consolas', 15, 'bold'))
    location += 1 # 입력결과를 출력한 칸을 그리기 위해 location값을 +1
    print("입력값 : %s" %user_num)
    if (result[0] == 4 and result[1] == 0):
        location = -1
    user_num.clear() # 사용자의 4자리 숫자를 초기화하여 다시 입력할 수 있게끔 한다.
    return location # 개행을 맞추기 위해 리턴


# 숫자 갯수 미달/초과 에러 판별 함수 (윤성)
def error1(num, x_axis, y_axis, location):
    t.penup()
    if (num < 1000): # 4자리 미만 오류 처리
        t.goto(x_axis, y_axis)
        square()
        t.pencolor("red")
        t.write(" ERROR\n", font=('Consolas', 15, 'bold'))
        t.pencolor("black")
        t.write(" 숫자부족", font=('Consolas', 15, 'bold'))
        location += 1
        return location # location을 리턴
    elif (num >= 10000): # 4자리 초과 오류 처리
        t.goto(x_axis, y_axis)
        square()
        t.pencolor("red")
        t.write(" ERROR\n", font=('Consolas', 15, 'bold'))
        t.pencolor("black")
        t.write(" 숫자초과", font=('Consolas', 15, 'bold'))
        location += 1
        return location
    return 'no error' # 에러가 없을 경우 에러메세지 칸을 그릴 필요가 없으므로 'no error' 리턴


# 중복 숫자/0사용 에러 판별 함수 (윤성)
def error2(user_num, x_axis, y_axis, location):
    for i in range(4):
        if (user_num[i] == 0): # 0 오류 처리
            t.goto(x_axis, y_axis)
            square()
            t.pencolor("red")
            t.write(" ERROR\n", font=('Consolas', 15, 'bold'))
            t.pencolor("black")
            t.write(" 0사용", font=('Consolas', 15, 'bold'))
            location += 1
            return location
        elif (user_num[i] in user_num[i+1:]): # 중복 오류 처리
            t.goto(x_axis, y_axis)
            square()
            t.pencolor("red")
            t.write(" ERROR\n", font=('Consolas', 15, 'bold'))
            t.pencolor("black")
            t.write(" 숫자중복", font=('Consolas', 15, 'bold'))
            location += 1
            return location
    return 'no error'


# UI칸을 그려주는 함수 (준호)
def square():
    t.speed(0)
    t.pendown()
    for i in range(2):
        t.fd(100)
        t.lt(90)
        t.fd(50)
        t.lt(90)
    t.penup()


# 게임종료를 담당하는 함수 (윤성 + 형철)
def gameOver(trial):
    t.penup()
    t.goto(-300, 290)
    t.pendown()
    t.pencolor("blue")
    t.pensize(3)
    for i in range(2):
        t.fd(200)
        t.lt(90)
        t.fd(50)
        t.lt(90)
    t.penup()
    t.goto(-300, 300)
    t.write(" %s번만에 성공!" %trial, font=('Consolas', 20, 'bold'))
    if (trial == 1):
        t.goto(0, 300)
        t.pencolor("orange")
        t.write("LUCKY!!!", font=('Consolas', 24, 'bold'))
    elif (trial <= 6):
        t.goto(0, 300)
        t.pencolor("purple")
        t.write("Excellent!", font=('Consolas', 24, 'bold'))
    elif (trial <= 12):
        t.goto(0, 300)
        t.pencolor("green")
        t.write("Good!", font=('Consolas', 24, 'roman'))
    t.goto(-300, 200)
    t.pencolor("black")
    # 기록을 남기기 위해 rank.txt에 기록한다.
    name = turtle.textinput("기록", "이름을 입력하세요")
    rank = open("rank.txt", "a")
    rank.write("%s\t   %s번\n" %(name, trial))
    rank.close()
    t.write("메인화면 : 0번 / 다시시작 : 1번 / 기록확인 : 2번 / 게임종료 : X ", font=('Consolas', 18, 'bold'))

    
# 기록을 출력하는 함수 (윤성)
def register():
    t.reset()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-300, 200)
    t.write("이름\t시도횟수", font=('Consolas', 30, 'bold'))
    t.goto(-300, 0)
    rank = open("rank.txt", "r")
    text = rank.read()
    t.write(text, font=('Consolas',24,'bold'))
    rank.close()
    t.goto(-150, -300)
    t.write("메인화면 : 0번 / 게임시작 : 1번 / 기록 초기화 : Delete", font=('Consolas', 15, 'bold'))


# 기록을 초기화하는 함수 (윤성)
def delete():
    rank = open("rank.txt", "w")
    rank.close()
    t.reset()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-300, 100)
    t.write("초기화를 완료했습니다.", font=('Consolas',24,'bold'))
    t.goto(-150, -300)
    t.write("메인화면 : 0번 / 게임시작 : 1번 / 초기화 확인 : 2번", font=('Consolas', 15, 'bold'))

    
# 게임규칙을 출력하는 함수 (준호)
def explain():
    t.reset()
    t.hideturtle()
    t.penup()
    t.goto(-300, 300)
    t.write("< 규칙 >",font=('Consolas',24,'bold'))
    t.goto(-300, 240)
    t.write("임의로 정해진 숫자 4자리를 맞히는 게임입니다.",font=('Consolas',24,'bold'))
    t.goto(-300, 180)
    t.write("사용되는 숫자는 1부터 9까지 입니다.",font=('Consolas',24,'bold'))
    t.goto(-300, 120)
    t.write("숫자는 맞지만 위치가 틀렸을 때는 '볼',",font=('Consolas',24,'bold'))
    t.goto(-300, 60)
    t.write("숫자와 위치가 전부 맞으면 '스트라이크' 입니다.",font=('Consolas',24,'bold'))
    t.goto(-300, 0)
    t.write("예시 : 정답이 5437 일 경우",font=('Consolas',24,'bold'))
    t.goto(-300, -200)
    t.write("4517 -> 1S 2B\n5428 -> 2S 0B\n5473 -> 2S 2B\n5437 -> 4S 0B",font=('Consolas',24,'bold'))
    t.goto(100, -300)
    t.write("메인화면 : 0번 / 게임시작 : 1번", font=('Consolas', 15, 'bold'))


# 게임 종료 함수 (준호)
def off():
    turtle.bye()


intro()
s.onkey(intro, "0")
s.onkey(start, "1")
s.onkey(register, "2")
s.onkey(explain, "3")
s.onkey(off, "x")
s.onkey(delete, "Delete")
s.listen()
s.mainloop()
