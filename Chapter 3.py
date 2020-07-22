#Exercise 5.d
#Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#Print the product of all the numbers in the list. (product means all multiplied together)
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
add=1

for f in xs:
    add=add*f
print(add)
#Exercise 6
#Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
#An equilateral triangle
#A square
#A hexagon (six sides)
#An octagon (eight sides)
import turtle
wn = turtle.Screen()
tess=turtle.Turtle()
tess.shape("turtle")
tess.color("gray")

#Triunghi Echilateral
# for i in range(3):
#     tess.forward(200)
#     tess.left(120)
# wn.mainloop()

#Patrat
# for i in range(4):
#     tess.forward(200)
#     tess.left(90)
# wn.mainloop()

#Hexagon
# for i in range(6):
#     tess.forward(200)
#     tess.left(60)
# wn.mainloop()

#Octogon
# for i in range(8):
#     tess.forward(100)
#     tess.left(45)
# wn.mainloop()


#Exercise 7
#A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc. A social science student records the angle of each turn before the next 100 steps are taken. Her experimental data is [160, -43, 270, -97, -43, 200, -940, 17, -86]. (Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend.

# angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

# for i in angles:
#     tess.left(i)
#     tess.forward(100)

# wn.mainloop()


