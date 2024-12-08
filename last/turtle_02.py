import turtle
import time

# 초기 설정
screen = turtle.Screen()
screen.title("과방 구조")
screen.setup(width=800, height=600)

# 터틀 생성
drawer = turtle.Turtle()
drawer.speed(0)

# 함수: 사각형 그리기 (책상, 칠판 등 표현)
def draw_rectangle(x, y, width, height, color="white"):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.fillcolor(color)
    drawer.begin_fill()
    for _ in range(2):
        drawer.forward(width)
        drawer.left(90)
        drawer.forward(height)
        drawer.left(90)
    drawer.end_fill()

# 과방 구성 그리기
def draw_room():
    # 1. 과방문
    draw_rectangle(-350, 180, 50, 50, "brown")

    # 2. 칠판/화이트보드
    draw_rectangle(-100, 200, 200, 50, "lightgray")

    # 3. 1조~3조 책상
    for i in range(3):  # 세로로 3개
        draw_rectangle(-300, 30 - i * 100, 80, 60, "blue")
        draw_rectangle(-330, 42 - i * 100, 30, 40, "gray")  # 의자

    # 4. 4조~6조 책상
    for i in range(3):  # 세로로 3개
        draw_rectangle(200, 30 - i * 100, 80, 60, "green")
        draw_rectangle(280, 42 - i * 100, 30, 40, "gray")  # 의자

    # 5. 컴퓨터 자리
    draw_rectangle(150, 130, 100, 50, "yellow")

    # 6. TV
    draw_rectangle(-180, 200, 80, 40, "black")  # 서쪽
    draw_rectangle(100, 200, 80, 40, "black")  # 동쪽

# 문 열기 애니메이션
def open_door():
    door = turtle.Turtle()
    door.speed(1)
    door.penup()
    door.goto(-350, 180)
    door.fillcolor("brown")
    door.begin_fill()
    for _ in range(2):
        door.forward(50)
        door.left(90)
        door.forward(50)
        door.left(90)
    door.end_fill()
    for _ in range(50):  # 문 열기 애니메이션
        door.setx(door.xcor() - 1)
        time.sleep(0.01)
    door.hideturtle()

# TV 켜기 애니메이션
def turn_on_tv(x, y):
    tv = turtle.Turtle()
    tv.speed(0)
    tv.penup()
    tv.goto(x, y)
    tv.fillcolor("black")
    tv.begin_fill()
    for _ in range(2):
        tv.forward(80)
        tv.left(90)
        tv.forward(40)
        tv.left(90)
    tv.end_fill()

    time.sleep(0.5)
    tv.fillcolor("blue")  # TV 켜짐 표시
    tv.begin_fill()
    for _ in range(2):
        tv.forward(80)
        tv.left(90)
        tv.forward(40)
        tv.left(90)
    tv.end_fill()
    tv.hideturtle()

# 자리에 앉기 애니메이션
def sit_down(x, y):
    person = turtle.Turtle()
    person.shape("circle")
    person.color("red")
    person.penup()
    person.goto(0, 250)  # 시작 위치
    person.showturtle()

    # 자리로 이동
    while person.ycor() > y:
        person.sety(person.ycor() - 5)
        time.sleep(0.05)
    while person.xcor() > x:
        person.setx(person.xcor() - 5)
        time.sleep(0.05)
    
    person.hideturtle()

# 실행
draw_room()
open_door()
turn_on_tv(-180, 200)  # 서쪽 TV
sit_down(-300, -20)  # 1조 자리

# 화면 유지
screen.mainloop()
