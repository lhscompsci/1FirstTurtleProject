import turtle

sue = turtle

sue.shape("turtle")
sue.forward(100)
sue.color("green")
sue.right(73)
sue.backward(85)
sue.penup()
sue.left(35)
sue.forward(50)
sue.pendown()
sue.color("red")
sue.circle(100)


sue.color("gold")

numOfSides = 12
angle = 360/numOfSides
size = 75
for i in range(numOfSides):
    sue.right(angle)
    sue.forward(size)

sue.penup()
sue.goto(-100, -100)
sue.pendown()
sue.speed(0.5)

def square(sidelength, col):
    sue.color(col)
    for i in range(1, 50):
        sue.forward(i)
        sue.right(90)


def circleofsquares(howMany):
    for num in range(howMany):
        square(num, "blue")
    sue.right(5)


sue.goto(250, -100)

square(50, "red")
square(100, "black")
circleofsquares(60)


sue.exitonclick()
