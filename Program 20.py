import turtle

screen = turtle.Screen()
screen.bgcolor('lightblue')
screen.title('Program 20')

t = turtle.Turtle()
t.speed(0)
t.pensize(5)

#Circle aka Face
t.penup()
t.goto(0, -200)
t.pendown()
t.color('yellow', 'yellow')
t.begin_fill()
t.circle(200)
t.end_fill()

#Left eye
t.penup()
t.goto(-70, 80)
t.pendown()
t.color('white', 'white')
t.begin_fill()
t.circle(40)
t.end_fill()

#Right eye
t.penup()
t.goto(70, 80)
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()

#Pupils
t.penup()
t.goto(-60, 100)
t.pendown()
t.color('black', 'black')
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(80, 100)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

#Mouth
t.penup()
t.goto(-80, -50)
t.pendown()
t.color('red')
t.pensize(20)
t.goto(100, -50)

#Goatee
t.color('black')
t.pensize(15)
t.penup()
t.goto(-80, -100)
t.pendown()
t.goto(100, -100)

t.penup()
t.goto(-80, -100)
t.pendown()
t.goto(0, -180)

t.penup()
t.goto(100, -100)
t.pendown()
t.goto(0, -180)

#Nostril
t.penup()
t.goto(-20, -20)
t.pendown()
t.color('black', 'black')
t.begin_fill()
t.circle(7)
t.end_fill()

t.penup()
t.goto(20, -20)
t.pendown()
t.color('black', 'black')
t.begin_fill()
t.circle(7)
t.end_fill()

t.penup()
t.goto(-100, 220)
t.pendown()
t.color('black')
t.write('Pac-Man!', font=("Courier", 32, "bold"))

t.hideturtle()
turtle.done()
