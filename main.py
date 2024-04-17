from turtle import *
import random

######## Class and Function Definitions ##########
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(2)
        self.direction = "right"
        
        self.penup()
        self.screen = screen
        self.screen.onkeypress(self.move_up, "Up")
        self.screen.onkeypress(self.move_right, "Right")
        self.screen.onkeypress(self.move_down, "Down")
        self.screen.onkeypress(self.move_left, "Left")

    def move_up(self):
        self.direction = "up"
        self.sety(self.ycor()+5)

    def move_right(self):
        self.direction = "right"
        self.setx(self.xcor()+5)

    def move_down(self):
        self.direction = "down"
        self.sety(self.ycor()-5)

    def move_left(self):
        self.direction = "left"
        self.setx(self.xcor()-5)

    def touch(self, box):
        # Player sides
        pTop = self.ycor()+20
        pRight = self.xcor()+20
        pBottom = self.ycor()-20
        pLeft = self.xcor()-20

        # Box sides
        bTop = box.ycor()+20
        bRight = box.xcor()+20
        bBottom = box.ycor()-20
        bLeft = box.xcor()-20

       # pushing right
        if (pRight > bLeft) and (pTop>bBottom) and (pBottom<bTop) and (pLeft<bLeft):
            return True
       # pushing left
        elif (pLeft < bRight) and (pTop>bBottom) and (pBottom<bTop) and (pRight>bRight):
            return True
       # pushing up
        elif (pTop>bBottom) and (pRight>bLeft) and (pLeft<bRight) and (pBottom<bBottom):
            return True
       # pushing down
        elif (pBottom<bTop) and (pRight>bLeft) and (pLeft<bRight) and (pTop>bTop):
            return True
        else:
            return False
        
    def push(self,box):
        if self.direction == "up":
            box.sety(self.ycor()+40)
        if self.direction == "down":
            box.sety(self.ycor()-40)
        if self.direction == "right":
            box.setx(self.xcor()+40)
        if self.direction == "left":
            box.setx(self.xcor()-40)


class Box(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color("red")
        self.shape("square")
        self.shapesize(2)
        self.goto(random.randint(-200,200),random.randint(-200,200))
        self.showturtle()



######## Driver Code ##########
screen = Screen()
screen.bgcolor('black')
screen.screensize(150,150)
screen.listen()

#Create Player
player = Player()

# Create four boxes and place them in a list
boxes = []
for count in range(4):
    boxes.append(Box())

while True:
    for box in boxes:
        if player.touch(box):
            box.color("white")
            player.push(box)
        else:
            box.color("red")

screen.mainloop()