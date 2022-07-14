import turtle
from turtle import *
from random import random, randint

screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.pendown()

def my_firework(turn_degree = 10): 
    length= randint(1,100)
    x = randint(-683+2*length, 683-2*length)  
    y = randint(-382+2*length, 384-2*length)  
    t.goto(x,y)
    
    red= randint(0,255)
    green= randint(0,255)
    blue= randint(0,255)
    t.color(red, green, blue)

    for x in range(int(360/turn_degree)): 
        t.pendown()
        t.forward(length)
        t.backward(length)
        t.rt(turn_degree)
        t.penup()
    
for x in range (20, 40):
    my_firework()
turtle.done()