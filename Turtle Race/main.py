from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


# tim = Turtle("turtle")
# tom = Turtle("turtle")
# tam=Turtle("turtle")
# tay = Turtle("turtle")
# tess = Turtle("turtle")
# trey = Turtle("turtle")

all_turtles = []
y_cord=-130
is_race_on = False


for turtle_index in range(0,len(colors)):
    new_turtle = Turtle("turtle")

    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    y_cord += 30
    new_turtle.goto(x=-230, y=y_cord)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle wins!")
            else:
                print(f"You lose! The {winning_color} turtle wins!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

#spacing of 50

screen.exitonclick()



