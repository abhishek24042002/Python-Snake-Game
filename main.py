import turtle
from turtle import Screen
import time
from Snake import Snake
from food import Food
from score import Scoreboard


scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)

Snake1 = Snake()
food = Food()
score = Scoreboard()

scr.listen()
scr.onkey(Snake1.up, "Up")
scr.onkey(Snake1.down, "Down")
scr.onkey(Snake1.right, "Right")
scr.onkey(Snake1.left, "Left")

Game_on = True
while Game_on:
    scr.update()
    time.sleep(0.1)
    Snake1.move()

    #Detect Collision with food
    if Snake1.snake_head.distance(food) < 15:
        food.refresh()
        score.add_score()
        Snake1.extend()

    # Detect collision with wall
    if Snake1.snake_head.xcor() >= 300 or Snake1.snake_head.xcor() <= -300 or Snake1.snake_head.ycor() >= 300 or Snake1.snake_head.ycor() <= -300:
        Game_on = False
        score.game_over()

    #Detect collision with tail
    for segment in Snake1.all_turtle:
        if Snake1.snake_head == segment:
            pass
        elif Snake1.snake_head.distance(segment) < 10:
            Game_on = False
            score.game_over()



scr.exitonclick()
