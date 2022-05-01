from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x = 0, y = 270)
        self.write(f"Score : {self.score}", False, "center", ("courier", 16, "normal"))
        
    def UpdateScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", False, "center", ("courier", 16, "normal"))
        
        
    def GameOver(self):
        self.goto(0 , 0)
        self.write("GAME OVER!", False, "center", ("Arial", 16, "normal"))
        
