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