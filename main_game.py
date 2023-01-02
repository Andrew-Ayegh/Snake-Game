from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time



screen = Screen()


# setting up the size of the screen
screen.setup(width=600, height=600)

# screen background color
screen.bgcolor('black')

screen.title("Snake Game")
# turning of the animation of how the screen objects are created: jump to "update()" 
screen.tracer(0)



game_is_on = True

snake = Snake()
score = ScoreBoard()
food = Food()

# Taking record of user control movement and assigning them to a movement method in the snake method
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.new_position()
        score.add_score()
        snake.extend()
    
    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < - 290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
    
    # detect collision with tail
    for segment in snake.segments:
        if segment != snake.head:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()
        
screen.exitonclick()
