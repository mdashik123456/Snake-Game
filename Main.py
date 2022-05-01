from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
        
snake = Snake()
food = Food()
screen = Screen()
score_board = ScoreBoard()

screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

snake.createSnake()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detcet food eat or not
    
    if snake.segments[0].distance(food) < 20:
        food.EatFood()
        snake.ExtendSnake()
        score_board.UpdateScore()
        
    # Game over when Bite into Wall 
    if snake.segments[0].xcor() > 300 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300 :
        score_board.GameOver()
        is_game_on = False
    
    # Game Over when Bite It Self
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            score_board.GameOver()
            is_game_on = False

screen.exitonclick()