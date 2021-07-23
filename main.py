import turtle as t
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard
import time

screen = t.Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game 🐍")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun = snake.up, key = "Up")
screen.onkey(fun = snake.down, key = "Down")
screen.onkey(fun= snake.left, key = "Left")
screen.onkey(fun= snake.right, key = "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # DETECT FOOD COLLISION
    if snake.snake_head.distance(food) < 15:
        food.new_food()
        snake.extend()
        scoreboard.increase_score()

    #DETECT WALL COLLISION
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    #DETECT TAIL COLLISION
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10 :
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()
