import turtle as t


t.setup(600, 500, 600, 300)
t.penup()
t.fd(-100)
t.pendown()
t.pensize(25)
t.pencolor("blue")
t.seth(-45)
for i in range(8):
    t.circle(36, 90)
    t.circle(-36, 45)
t.circle(-36, 90 / 2)
t.fd(40)
t.circle(16, 180)
t.fd(36)
t.done()