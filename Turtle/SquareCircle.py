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

def colour():
    red= randint(0,255)
    green= randint(0,255)
    blue= randint(0,255)
    t.color(red, green, blue)

def draw_square(length):
    t.pendown()
    for i in range(4): 
        t.forward(length)
        t.left(90)

def rotate_square(turn_degree, length): 
    for i in range(int(360/turn_degree)+1): 
        draw_square(length)
        t.rt(turn_degree)
    
def location(length):
    x = randint(-683+2*length, 683-2*length)  
    y = randint(-382+2*length, 384-2*length)  
    t.goto(x,y)

for x in range (20, 50):
    length= randint(1,100)
    turn_degree=60
    location(length)
    colour()
    rotate_square(turn_degree, length)
    t.penup()
turtle.done()