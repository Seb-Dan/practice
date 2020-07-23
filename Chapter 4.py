# import turtle

# def draw_multicolor_square(t, sz):
#     """Make turtle t draw a multi-color square of sz."""
#     for i in ["red", "purple", "hotpink", "blue"]:
#         t.color(i)
#         t.forward(sz)
#         t.left(90)

# wn = turtle.Screen()        # Set up the window and its attributes
# wn.bgcolor("lightgreen")

# tess = turtle.Turtle()      # Create tess and set some attributes
# tess.pensize(3)

# size = 20                   # Size of the smallest square
# for i in range(15):
#     draw_multicolor_square(tess, size)
#     size = size + 10        # Increase the size for next time
#     tess.forward(10)        # Move tess along a little
#     tess.right(18)          #    and give her some turn

# wn.mainloop()

#Exercise 1

# import turtle

# def draw_square(t,d):
#     """This function will draw a square"""
#     for i in range(4):
#         t.forward(d)
#         t.left(90)



# wn = turtle.Screen()
# wn.bgcolor("lightgreen")


# tess = turtle.Turtle()
# tess.color("pink")
# tess.pensize(3)

# for i in range(5):
#     draw_square(tess,20)
#     tess.penup()
#     tess.forward(40)
#     tess.pendown()

# wn.mainloop()
