import turtle
turtle.setup(968,648)
turtle.bgcolor('red')
turtle.fillcolor('yellow')
turtle.color('yellow')
turtle.speed(4)
params=[
    -416,192,192,0,
    -186,276,64,-22.5,
    -108,216,64,-45,
    -126,108,64,0,
    -186,54,64,-22.5
]
i=0;l=len(params)
while i<1:
    drawX=params[i]
    drawY=params[i+1]
    drawL=params[i+2]
    drawH=params[i+3]
    i=i+4
    turtle.begin_fill()
    turtle.up()
    turtle.goto(drawX,drawY)
    turtle.setheading(drawH)
    turtle.down()
    j=0
    while j<5:
        j=j+1
        turtle.forward(drawL)
        turtle.right(144)
    turtle.end_fill()
turtle.hideturtle()
turtle.Screen().exitonclick()