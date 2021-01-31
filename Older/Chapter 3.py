#Exercise 5.d
#Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#Print the product of all the numbers in the list. (product means all multiplied together)
# xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# add=1

# for f in xs:
#     add=add*f
# print(add)
#Exercise 6
#Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
#An equilateral triangle
#A square
#A hexagon (six sides)
#An octagon (eight sides)
# import turtle
# wn = turtle.Screen()
# tess=turtle.Turtle()
# tess.shape("turtle")
# tess.color("gray")

# Triunghi Echilateral
# for i in range(3):
#     tess.forward(200)
#     tess.left(120)
# wn.mainloop()

# Patrat
# for i in range(4):
#     tess.forward(200)
#     tess.left(90)
# wn.mainloop()

# Hexagon
# for i in range(6):
#     tess.forward(200)
#     tess.left(60)
# wn.mainloop()

# Octogon
# for i in range(8):
#     tess.forward(100)
#     tess.left(45)
# wn.mainloop()


# Exercise 7
# A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc. A social science student records the angle of each turn before the next 100 steps are taken. Her experimental data is [160, -43, 270, -97, -43, 200, -940, 17, -86]. (Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend.

# angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

# for i in angles:
#     tess.left(i)
#     tess.forward(100)

# wn.mainloop()

# Exercise 8
# Enhance your program above to also tell us what the drunk pirate’s heading is after he has finished stumbling around. (Assume he begins at heading 0).
# angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

# for i in angles:
#     tess.left(i)
#     tess.forward(100)
# int(print(tess.heading()))
# wn.mainloop()

# import turtle
# wn = turtle.Screen()
# tess = turtle.Turtle()
# tess.right(90)
# tess.left(3600)
# tess.right(-90)
# tess.speed(10)
# tess.left(3600)
# tess.speed(0)
# tess.left(3645)
# tess.forward(-100)

# wm.mainloop()


#Exercise 11
#Draw a star

import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
tess = turtle.Turtle()


# angles = [36,144,144,144,144]

# for i in angles:
#     tess.left(i)
#     tess.forward(100)

# for i in range(5):
#     tess.left(144)
#     tess.forward(100)

# wn.mainloop()


#Exercise 12
#Write a program to draw a face of a clock that looks something like this:

# tess.speed(1)
# tess.color("Blue")
# tess.shape("turtle")
# tess.stamp()
# tess.penup()
# tess.speed(20)

# position=0
# for i in range(12):
#     tess.forward(100)
#     tess.stamp()
#     tess.home()
#     position=position+30
#     tess.left(position)
    
    
# wn.mainloop()

#Exercise 13

# print(type(tess))