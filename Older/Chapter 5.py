

# import turtle


# def draw_bar(t, height):
#     """ Get turtle t to draw one bar, of height. """
#     t.begin_fill()           # Added this line
#     t.left(90)
#     t.forward(height)
#     t.write("  "+ str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()             # Added this line
#     t.penup()
#     t.forward(10)
#     t.pendown()

# wn = turtle.Screen()         # Set up the window and its attributes
# wn.bgcolor("lightgreen")

# tess = turtle.Turtle()       # Create tess and set some attributes
# tess.color("blue", "red")
# tess.pensize(3)

# xs = [48,117,200,240,160,260,220]

# for a in xs:
#     draw_bar(tess, a)

# wn.mainloop()


#Exercise 1

# dotw = int(input("Which day of the week?"))
# if (dotw == 0):
#     print("Sunday")
# elif (dotw == 1):
#     print("Monday")
# elif (dotw == 2):
#     print("Tuesday")
# elif (dotw == 3):
#     print("Wednesday")
# elif (dotw == 4):
#     print("Thursday")
# elif (dotw == 5):
#     print("Friday")
# elif (dotw == 6):
#     print("Saturday")
# else:
#     print("Wrong number")


# # num = int(input("Write the number here "))

# # days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

# # def _printday(n, d):
# #     print(d[n])
    


#Exercise 2

# start_day = int(input("When did you go to jail? "))
# days_spent = int(input("How many days did you spend inside? "))

# def jailed_day(sd, ds):
#     f_d = (sd+ds)%7
#     days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
#     print(days[(f_d)])

# jailed_day(start_day, days_spent)

#Exercise 3

print(2+2)