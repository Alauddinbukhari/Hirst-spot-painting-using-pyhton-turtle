import colorgram #using colorgram library to extract images colors

colors = colorgram.extract("image.jpg", 15)#extract colors object with attributes such as rgb code
print(len(colors))
colors_tuple = []


def turn_to_tuple(rgb_tuple):
    red = rgb_tuple.r
    green = rgb_tuple.g
    blue = rgb_tuple.b
    return colors_tuple.append((red, green, blue))


def imgs_to_tuple(colors):
    for i in range(len(colors)):
        color = colors[i]
        rgb_tuple = color.rgb
        turn_to_tuple(rgb_tuple)



imgs_to_tuple(colors)
print(colors_tuple)


import random as r
from turtle import Turtle, Screen
colors=["yellow","red","orange","blue","brown","purple","seagreen"]
screen = Screen()
screen.colormode(255)

colors_list = [(233, 234, 236), (233, 232, 230), (235, 231, 233), (223, 234, 229), (44, 95, 148), (179, 46, 75), (227, 208, 100), (209, 156, 88), (179, 169, 33), (137, 88, 63), (115, 179, 209), (201, 74, 121), (214, 130, 174), (229, 70, 50), (90, 104, 191)]

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")
timmy_the_turtle.penup()
timmy_the_turtle.speed("fastest")

def draw_dots():
    x_cor = -200
    timmy_the_turtle.setx(x_cor)
    y_cor = -200
    timmy_the_turtle.sety(y_cor)

    for _ in range(10):

        for _ in range(10):
            timmy_the_turtle.dot(20,r.choice(colors_list))
            timmy_the_turtle.forward(50)

        y_cor += 50
        timmy_the_turtle.goto(x_cor,y_cor)

draw_dots()
screen.exitonclick()
