from email.quoprimime import body_length
from hashlib import new
from re import X
import turtle
import time
import random

delay = 0.1

# 윈도우 세팅을 해야한다.
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)                            # 윈도우 업데이트 끔

#스네이크 머리
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("grey")
head.penup()
head.goto(0,0)
head.direction = "stop"

# 스네이크 몸통
body = []

# 아이템
item = turtle.Turtle()
item.speed(0)
item.shape("circle")
item.color("red")
item.penup()
item.goto(0,100)

# 키 조작에 따른 이동 함수
def goUp():                             # 방향함수
    if head.direction != "down":
        head.direction = "up"

def  goDown():
    if head.direction != "up":
        head.direction = "down"
    
def goLeft():
    if head.direction != "right":
        head.direction = "left"
        
def goRight():
    if head.direction != "left":
        head.direction = "right"

def move():                             # 이동함수
    if head.direction == "up":
        y = head.ycor()                 # ycor는 y 좌표 가져오는 함수이다.
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()                 
        head.sety(y - 20)
    
    if head.direction == "left":
        x = head.xcor()                 
        head.setx(x - 20)
        
    if head.direction == "right":
        x = head.xcor()                 
        head.setx(x + 20)
        
# 키보드 이벤트 처리
wn.listen()                             # 키보드 눌리는지 확인 처리
wn.onkeypress(goUp, 'w')
wn.onkeypress(goDown, 's')
wn.onkeypress(goLeft, 'a')
wn.onkeypress(goRight, 'd')

while True:
    wn.update()
    
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # 몸통을 숨기자
        for b in body:
            b.goto(1000, 1000)
            
        body.clear()
        
        delay = 0.1
    
    # 아이템과 충돌 처리: 아이템을 먹는 경우
    if head.distance(item) < 20:
        # 새로운 아이템 좌표 설정
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        item.goto(x, y)
        
        # 몸통을 늘려 준다.
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("white")
        new_body.penup()
        body.append(new_body)
        
        delay -= 0.001
        
    # 몸통 좌료를 업데이트
    for index in range(len(body) -1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)
        
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)
        
    move()
        
    #몸통 충돌
    for b in body:
        if b.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            for b in body:
                b.goto(1000, 1000)
                
            body.clear()
            
            delay = 0.1
                    
    time.sleep(delay)                   # 딜레이값을 준다.
    
wn.mainloop()