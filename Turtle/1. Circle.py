import turtle #* Import turtle module

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()

t.width(2)
t.color("red")
t.penup()
t.goto(100,100)
t.pendown()
t.circle(25)

t.color("orange")
t.penup()
t.goto(50,100)
t.pendown()
t.circle(25)

t.color("yellow")
t.penup()
t.goto(0,100)
t.pendown()
t.circle(25)

t.color("green")
t.penup()
t.goto(0,50)
t.pendown()
t.circle(25)

t.color("blue")
t.penup()
t.goto(50,50)
t.pendown()
t.circle(25)

t.color("purple")
t.penup()
t.goto(100,50)
t.pendown()
t.circle(25)

turtle.done()