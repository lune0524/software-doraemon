import turtle

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
# 1. 과방문
draw_rectangle(-350, 180, 50, 50, "brown")

# 2. 칠판/화이트보드
draw_rectangle(-100, 200, 200, 50, "lightgray")

# 3. 1조~3조 책상
for i in range(3):  # 세로로 3개
    draw_rectangle(-300, 30 - i * 100, 80, 60, "blue")
    
for i in range(3):  # 세로로 3개
    draw_rectangle(-330, 42 - i * 100, 30, 40, "gray")

# 4. 4조~6조 책상
for i in range(3):  # 세로로 3개
    draw_rectangle(200, 30 - i * 100, 80, 60, "green")
    
for i in range(3):  # 세로로 3개
    draw_rectangle(280, 42 - i * 100, 30, 40, "gray")

# 5. 컴퓨터 자리
draw_rectangle(150, 130, 100, 50, "yellow")

# 6. TV
draw_rectangle(-180, 200, 80, 40, "black")  # 서쪽
draw_rectangle(100, 200, 80, 40, "black")  # 동쪽

# 터틀 숨기기
drawer.hideturtle()

# 화면 유지
turtle.done()
