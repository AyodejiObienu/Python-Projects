import turtle as t
from turtle import Screen
import colorgram as c
import random

t.colormode(255)
t.ht()



# def color_detector(image_name, number_of_colors):
#     rgb_color = c.extract(image_name, number_of_colors)

#     colors = []

#     # return rgb_color[0].rgb

#     for color in rgb_color:

#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         new_color = (r, g, b)
#         colors.append(new_color)

#     return colors

# 10x10 20 in size spaced at 50
# print(color_detector("image.jpg", 100))

# t.setheading(0)
color_list = [(200, 162, 98), (62, 89, 127), (139, 90, 47), (135, 170, 191), (218, 206, 117), (29, 39, 65), (132, 27, 52), (149, 62, 86), (76, 15, 33), (167, 153, 49), (130, 181, 144), (186, 141, 161), (43, 57, 100),
              (184, 94, 107), (53, 37, 25), (61, 123, 107), (92, 116, 175), (80, 76, 31), (89, 151, 100), (80, 147, 159), (194, 87, 73), (220, 174, 186), (166, 207, 161), (163, 201, 215), (31, 55, 52), (145, 35, 22)]
color_list_upgrade = [(236, 234, 230), (230, 233, 238), (238, 232, 235), (229, 236, 231), (200, 162, 98), (62, 89, 127), (139, 90, 47), (135, 170, 191), (218, 206, 117), (29, 39, 65), (132, 27, 52), (149, 62, 86), (76, 15, 33), (167, 153, 49), (130, 181, 144), (186, 141, 161), (
    43, 57, 100), (184, 94, 107), (53, 37, 25), (61, 123, 107), (92, 116, 175), (80, 76, 31), (89, 151, 100), (80, 147, 159), (194, 87, 73), (220, 174, 186), (166, 207, 161), (163, 201, 215), (31, 55, 52), (145, 35, 22), (219, 180, 174), (178, 188, 212), (47, 73, 69), (42, 71, 78)]
t.up()
t.setposition(-200, -200)
positive = True
angle = 0
x = -200
y = -150

for j in range(10):

    for i in range(9):
        t.dot(20, random.choice(color_list_upgrade))
        t.forward(50)

    # while positive:

    # angle += 90
    # t.setheading(angle)
    # t.teleport(-150, -150)
    t.setposition(-200, y)
    y += 50


    # while positive:
    #     angle += 90
    #     t.setheading(angle)

    # t.forward(50)
    # t.dot(20, random.choice(color_list_upgrade))
    # t.setheading(angle + 90)


# for i in range(10):
#     for j in color_list:
#         t.dot(20, j)
#         t.forward(50)


# t.dot(20, (200, 162, 98))
# t.forward(50)
# t.dot(20, (62, 89, 127))


Screen = Screen()
Screen.exitonclick()

# tim = t.Turtle()


# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rand_color = (r, g, b)
#     return rand_color

# for i in range(4):

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)


# download pycharm virtual enviroments help you install modules and packages and keep them in each project seperately from others
# no_of_sides = 2
# len_of_sides = 100
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGrey", "SeaGreen"]
# move_right = timmy_the_turtle.right(90)
# move_left = timmy_the_turtle.left(90)
# movements = [move_left, move_right]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
# def draw_spirograph(size_of_gap):
#     for i in range (int(360 / size_of_gap)):

#       tim.color(random_color())
#       tim.circle(100)
#       tim.setheading(tim.heading() + size_of_gap)


# draw_spirograph(5)
# screen = Screen()
# screen.exitonclick()

# for i in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
# print(random_color())


# for i in range(8 ):
#     no_of_sides += 1
#     angle = 360 / no_of_sides
#     timmy_the_turtle.color(random.choice(colors))
#     for i in range(no_of_sides):


#         timmy_the_turtle.forward(len_of_sides)
#         timmy_the_turtle.right(angle)
# def random_walk(distance, steps):
#     track = 0
#     while track <= steps:
#         track += 1
#         timmy_the_turtle.forward(distance)
#         random.choice(movements)


# random_walk(20, 20)

# def draw_shape(no_of_sides):
#     angle = 360 / no_of_sides
#     for i in range(no_of_sides):
#         timmy_the_turtle.forward(len_of_sides)
#         timmy_the_turtle.right(angle)

# for i in range(3,11):
#     timmy_the_turtle.color(random.choice(colors))

#     draw_shape(i)


# timmy_the_turtle.forward(len_of_sides)
# timmy_the_turtle.right(angle)
# timmy_the_turtle.forward(len_of_sides)

# timmy_the_turtle.right(angle)


# for i in range(15):
# timmy_the_turtle.forward(10)
# timmy_the_turtle.penup()
# timmy_the_turtle.forward(10)
# timmy_the_turtle.pendown()
