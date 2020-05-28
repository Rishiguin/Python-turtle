import turtle

turtle.bgcolor('black')
tim=turtle.Turtle()
tim.pensize(1)
tim.shape('turtle')
tim.color('green')
tim.speed(0)
colors = ['red','green','blue','yellow','magenta','cyan']

for i in range (6):
    for j in range (6) :
        tim.color(colors[j])
        tim.left(10)
        tim.circle(150)
        
turtle.done()
