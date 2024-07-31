import turtle
t = turtle.Turtle()

t.pensize(1)
t.shape('turtle')
t.lt(50)
t.color('#FED049')
t.fillcolor('#B73E3E')
t.begin_fill()
t.circle(150,50)
t.rt(45)
t.fd(40)
t.lt(150)
t.fd(40)
t.lt(10)
t.circle(150,50)
t.lt(60)
t.end_fill()
t.penup()
t.fd(53)
t.pendown()
t.lt(120)
t.begin_fill()
t.circle(150,75)
t.lt(140)
t.fd(40)
t.rt(40)
t.circle(150,50)
t.lt(22)
t.circle(40,100)
t.lt(10)
t.end_fill()
t.penup()
t.fd(125)
t.pendown()
t.lt(25)
t.begin_fill()
t.circle(50,60)
t.rt(30)
t.fd(20)
t.lt(90)
t.fd(20)
t.rt(35)
t.circle(50,60)
t.lt(80)
t.circle(80,60)
t.end_fill()
t.lt(100)
t.fd(25)
t.circle(10,180)
t.circle(5)
t.penup()
t.lt(20)
t.fd(40)
t.pendown()
t.lt(140)
t.fd(20)
t.lt(150)
t.penup()
t.fd(160)
t.pendown()
t.fillcolor('#5F8D4E')
t.begin_fill()
t.rt(84)
t.fd(60)
t.lt(170)
t.fd(50)
t.rt(78)
t.fd(280)
t.lt(90)
t.fd(10)
t.lt(90)
t.fd(280)
t.rt(82)
t.fd(50)
t.lt(165)
t.fd(45)
t.end_fill()
t.penup()
t.rt(62)
t.fd(158)
t.pendown()
t.color('#FED049')
t.fillcolor('#B73E3E')
t.rt(110)
t.penup()
t.fd(70)
t.pendown()
t.fd(30)
t.begin_fill()
t.rt(140)
t.fd(55)
t.lt(24)
t.fd(18)
t.rt(110)
t.fd(70)
t.end_fill()
t.rt(160)
t.circle(80,60)
t.penup()
t.rt(130)
t.fd(320)
t.lt(90)
t.pendown()

def leaf():
    t.pensize(1)
    t.fillcolor('#5F8D4E')
    t.begin_fill()
    t.circle(100,100)
    t.lt(79)
    t.circle(100,100)
    t.end_fill()
    t.color('#222222')
    t.lt(130)
    t.fd(150)
    t.penup()
    t.lt(180)
    t.fd(140)
    t.pendown()
    t.rt(140)
    t.fd(45)
    t.lt(180)
    t.fd(45)
    t.lt(95)
    t.fd(43)
    t.lt(180)
    t.fd(45)
    t.rt(135)
    t.fd(40)
    t.rt(45)
    t.fd(50)
    t.lt(180)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.lt(180)
    t.fd(50)
    t.lt(135)
    t.fd(50)
    t.lt(50)
    t.fd(30)
    t.lt(180)
    t.fd(33)
    t.lt(90)
    t.fd(35)
leaf()
t.color('#FED049')
t.penup()
t.rt(150)
t.fd(140)
t.pendown()
t.rt(120)
leaf()
t.color('white')
t.rt(13)
t.penup()
t.fd(340)
t.rt(90)
t.pendown()
t.hideturtle()
t.write(" I Love You<3 ",font=('Arial',28,'normal'))
t.done()