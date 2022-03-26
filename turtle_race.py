# Project done using python graphics
from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
window = Screen()
window.title("Turtle Race")
window.setup(width=0.9, height=0.9)
player_bet = window.textinput("Make your bet", "Select the color of turtle you want to bet on ?")
y_coord = 350
racers = []
race_start = False

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)  # set the color
    new_turtle.penup()
    y_coord -= 100  # setting the y-coordinate
    new_turtle.goto(x=-540, y=y_coord)
    racers.append(new_turtle)

if player_bet in colors:  # Race starts only when user enters the bet i.e in this case non-empty string
    race_start = True
else:
    print("Sorry your input was invalid")

while race_start:
    for racer in racers:
        if racer.xcor() > 600:
            race_start = False
            winner = racer.pencolor()
            if winner == player_bet:
                print(f"HURRAY !!!!You won with {winner} turtle.")
            else:
                print(f"Sorry. {winner} turtle won the race.")

        random_sprint = random.randint(1, 5)
        racer.forward(random_sprint)


window.exitonclick()
