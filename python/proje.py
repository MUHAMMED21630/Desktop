# import turtle

# pen = turtle.Turtle()

# def cruve():
#   for i in range(200):    
#      pen.right(1)
#      pen.forward(1)

#      def heart():
#         pen.fillclor("blue")
#         pen.begin_fill()
#         pen.left(140)
#         pen.forward(113)
#         cruve()
#         pen.left(120)
#         cruve()
#         pen.forward(112)
#         pen.end_fill()
        
#         heart()
#         turtle.done()

# sadece  kalp doğru olan kod

# import turtle

# pen = turtle.Turtle()

# def cruve():
#     for i in range(200):
#         pen.right(1)
#         pen.forward(1)

# def heart():
#     pen.fillcolor("blue")
#     pen.begin_fill()
#     pen.left(140)
#     pen.forward(113)
#     cruve()
#     pen.left(120)
#     cruve()
#     pen.forward(112)
#     pen.end_fill()

# heart()
# turtle.done()


import turtle

# Kalp çizen turtle
pen = turtle.Turtle()
pen.speed(1)

def cruve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor("blue")
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    cruve()
    pen.left(120)
    cruve()
    pen.forward(112)
    pen.end_fill()

# Kalbi çiz
heart()

# Oku çizen turtle
arrow = turtle.Turtle()
arrow.color("red")
arrow.pensize(3)
arrow.penup()
arrow.goto(-70, -20)  # Kalbin altından geçmesi için konum ayarı
arrow.setheading(30)
arrow.pendown()
arrow.forward(200)

# Ok ucu
arrow.right(150)
arrow.forward(20)
arrow.back(20)
arrow.left(300)
arrow.forward(20)

# Yazı yazan turtle
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("red")

# Sol tarafa isim
writer.goto(-160, 60)
writer.write("Muhammed", align="center", font=("Arial", 16, "bold"))

# Sağ tarafa isim
writer.goto(160, 60)
writer.write("dostum", align="center", font=("Arial", 16, "bold"))

# Pencerenin açık kalması için
turtle.done()
