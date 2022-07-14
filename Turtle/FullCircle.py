import turtle #* Import turtle module
from random import random, randint

screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.width(2)

def circle_function(turn_degree = 60): 
    radius = randint(1,100)
    x = randint(-683+2*radius, 683-2*radius)  
    y = randint(-382+2*radius, 384-2*radius)  
    t.goto(x,y)
    
    for x in range(int(360/turn_degree)): # Start: 0, End: <36, Step: 1, 0 ~ 35
        red= randint(0,255)
        green= randint(0,255)
        blue= randint(0,255)
        t.pendown()
        t.color(red, green, blue)
        t.circle (radius)
        t.penup()
        t.rt (turn_degree)
  
    
for x in range(100) :
    #size= randint(10,70)
    circle_function ()
turtle.done