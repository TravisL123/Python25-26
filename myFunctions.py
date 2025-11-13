import turtle
bob = turtle.Turtle()
turtle.bgcolor("black")
def comet(c, distance, angle):
  bob.color(c)
  for times in range(10):
    bob.pensize(times / 2)
    bob.forward(distance)
    bob.left(angle)

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()

