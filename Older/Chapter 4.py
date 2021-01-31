import turtle

def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()      # Create tess and set some attributes
tess.pensize(3)

size = 20                   # Size of the smallest square
for i in range(15):
    draw_multicolor_square(tess, size)
    size = size + 10        # Increase the size for next time
    tess.forward(10)        # Move tess along a little
    tess.right(18)          #    and give her some turn

wn.mainloop()

#Exercise 1############################

import turtle

def draw_square(t,d):
    """This function will draw a square"""
    for i in range(4):
        t.forward(d)
        t.left(90)



wn = turtle.Screen()
wn.bgcolor("lightgreen")


tess = turtle.Turtle()
tess.color("pink")
tess.pensize(3)

for i in range(5):
    draw_square(tess,20)
    tess.penup()
    tess.forward(40)
    tess.pendown()

wn.mainloop()

#Exercise 2#######################

import turtle

def draw_square(t,d):
    """This function will draw a square"""
    for i in range(4):
        t.forward(d)
        t.left(90)

def draw_shape(t):
    """This function will draw the shape"""
    t.penup()
    t.right(135)
    t.forward(15)
    t.pendown()
    t.left(135)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

size = 0
for i in range(5):
    size = size + 20
    draw_square(tess,size)
    draw_shape(tess)
    

wn.mainloop()

#Exercise 3##################################

import turtle

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(45)    

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

for i in range(1):
    draw_poly(tess, 8, 50)

wn.mainloop()

#Exercise 4###################################

import turtle


def draw_square(t,d):
    """This function will draw a square"""
    for i in range(5):
        t.forward(d)
        t.left(90)
        

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(2)
tess.speed(100)

angle = 0

def squarethingy():
    for i in range(4):
        tess.forward(100)
        tess.left(90)

def squarev2():
    squarethingy()
    tess.left(18)

for i in range(20):
    squarev2()
    
def shapezilla(t,n):
    for i in range(4):
        draw_square(t,n)
        tess.forward(n)


for i in range(10):
    shapezilla(tess,200)
    tess.home()
    tess.left(36)
    

wn.mainloop()

#Exercise 5##############################

def path(t,l):
    t.forward(l)
    t.right(90)

length = 0
tess.right(90)
for i in range(100):
    length = length + 3
    path(tess,length)
    tess.left(1)

wn.mainloop()

#Exercise 6##########################

def draw_poly(t, n, sz):
    t.forward(sz)
    t.left(360/n)


def draw_equitriangle(t,sz):
    for i in range(3):
        draw_poly(t,3,sz)
        t.forward(sz)

draw_equitriangle(tess,100)



def draw_equitriangle(t, sz):
    draw_poly(tess, 3, 100)

wn.mainloop()


#Exercise 7#######################



def sum_to(n):
    sum=0
    for i in range(n+1):
        sum = sum + i
    return sum

print(sum_to(10))

#Exercise 8##################

def area_of_circle(r):
    A = 3.14185 * r**2
    return A

print(area_of_circle(5))

#Exercise 9###################

def star(t):
    for i in range(5): 
        t.right(144)
        t.forward(100)

for i in range(5):
    star(tess)
    tess.penup()
    tess.right(144)
    tess.forward(350)
    tess.pendown()

wn.mainloop()
