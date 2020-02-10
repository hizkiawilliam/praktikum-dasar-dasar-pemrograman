#Nama : Hizkia William Eben
#NPM : 1706042806
import turtle

#fill = int(input("Masukan Jumlah Pixel "))
fill = 200

shape = turtle.Turtle()

shape.begin_fill()
shape.color("red")
shape.forward(fill)
shape.right(240)

shape.color("yellow")
shape.forward(fill)
shape.right(240)

shape.color("green")
shape.forward(fill)
shape.right(240)

shape.color("blue")
shape.end_fill()

turtle.done()
