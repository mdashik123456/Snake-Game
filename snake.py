from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360

class Snake:
    
    def __init__(self):
        self.segments = []
        
    def createSnake(self):
        x_position = 0
        for _ in range(3):
            s = Turtle("square")
            s.penup()
            s.color("white")
            s.goto(x = x_position, y = 0)
            self.segments.append(s)
            x_position -= 20
            
    def ExtendSnake(self):
        s = Turtle("square")
        s.penup()
        s.color("white")
        s.goto(self.segments[-1].pos())
        self.segments.append(s)
        
        
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
            
        self.segments[0].forward(20)
        
        
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
            
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
            
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
            
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)