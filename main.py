################################################################################
# Project Name:  Turtle Race Game
# Description:   This project is turtle race game which to guess which turtle color gets to the end line
# Author:        ziqkimi308
# Created:       2024-12-03
# Updated:       2024-12-03
# Version:       1.0
################################################################################

# Import
from turtle import Turtle, Screen
import random

# Screen
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")

# Turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for i in range(6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in all_turtle:
        i.forward(random.randint(0,10))
        if i.xcor() > 230:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost... The {winning_color} turtle is the winner!")


# Last
screen.exitonclick()