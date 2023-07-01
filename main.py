from turtle import Turtle, Screen
import random

my_t = Turtle()
screen = Screen()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color


screen.colormode(255)
my_t.speed("fastest")

def draw_spirograph(size_gap):
    for _ in range(int(360 / size_gap)):
        my_t.color(random_color())
        my_t.circle(100)
        my_t.setheading(my_t.heading() + size_gap)


# gap = int(input("How many size of gap you want for you spirograph :? "))
draw_spirograph(5)
screen.exitonclick()