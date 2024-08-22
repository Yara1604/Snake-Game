from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600, startx=325, starty=10)
screen.bgcolor("#422C73")
screen.title("Ultimate Snake Game")
screen.tracer(0) # Turns animation on/off

mySnake = Snake()
myFood = Food()
myScoreboard = Scoreboard()

screen.listen()  
screen.onkey(mySnake.up,"Up") # (Function to call, Key)
screen.onkey(mySnake.down,"Down")
screen.onkey(mySnake.right,"Right")
screen.onkey(mySnake.left,"Left")


def start_game():
    gameIsOn = True
    while gameIsOn:
        screen.update() # Shows the snake's current position
        time.sleep(0.1) # Sets the speed of the snake
        mySnake.move()

        # Detect Collision with Food
        if mySnake.head.distance(myFood) < 17:
            myFood.refresh()
            myScoreboard.increase_score()
            mySnake.extend()

        # Detect Collision with Wall
        if mySnake.head.xcor() > 285 or mySnake.head.xcor() < -285 or mySnake.head.ycor() > 285 or mySnake.head.ycor() < -285:
            gameIsOn = False
            myScoreboard.game_over()

        # Detect Collision with snake tail
        for segment in mySnake.segments[1:len(mySnake.segments)]:
            if mySnake.head.distance(segment) < 5:
                gameIsOn = False
                myScoreboard.game_over()

start_game()

# Function to restart it all
def restart():
    mySnake.restart()
    myScoreboard.restart()
    myFood.refresh()
    start_game()


screen.onkey(restart,"r")




screen.exitonclick()