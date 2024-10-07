from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
scoreboard = Scoreboard()

while game_is_on:
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        print(f"score : {scoreboard.score}")
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    # detect collision with tail
    i = 0
    for segment in snake.segments:
        if snake.head.distance(segment) < 10 and i > 0:
            game_is_on = False
            scoreboard.game_over()

        i += 1


screen.exitonclick()
