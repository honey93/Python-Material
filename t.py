import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    for j in range(1,37):
        for i in range(1,5):
            brad.forward(100)
            brad.right(90)
        brad.right(10)
    window.exitonclick()
draw_square()
    
