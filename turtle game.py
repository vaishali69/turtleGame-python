from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)

is_race_on=False
all_turtles=[]
user_bet=screen.textinput(title="Make your Bet",prompt="Can u Guess,Choose color:")
colors=['peachpuff1','coral','green','blue','purple','cyan4']
y_coordinates=[-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240,y=y_coordinates[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True
    while is_race_on:
       for turtle in all_turtles:
        rand_distance=random.randint(0,10) 
        turtle.fd(rand_distance)
        if turtle.xcor()>230:
           is_race_on=False
           winning_color=turtle.pencolor()
           if winning_color==user_bet:
              print(f"you've Won! The winner is {winning_color} turtle")
           else:
            print(f"you've lost, The winner is {winning_color} turtle")



screen.exitonclick()