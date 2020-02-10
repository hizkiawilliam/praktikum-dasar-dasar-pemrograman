'''
 Created by  : Hizkia William Eben
 NPM         : 1706042806
 
    Turtle Race v4.4
--------------------------------
     [Change Log]
         v4.4
 - Revisi ukuran lapangan
 - Revisi sistem message(tidak pakai tkinter)
 - Revisi random color(mencegah terjadinya warna sama)
 - Hasil message sesuai warna pemenang
 - Kura-kura kembali ke lapangan dengan algoritma baru
         v3.0
 - Membuat hasil lomba menggunakan tkinter
 - Nama dan warna turtle adalah random
 - Format hasil perlombaan sesuai soal
         v2.2
 - Sistem juara
         v2.0
 - Turtle bergerak random
 - Turtle dapat kembali ke dalam arena jika keluar garis
 - Input nama untuk setiap turtle
         v1.0
 - Turtle dapat mencapai finish
 - Arena terbentuk sesuai soal
--------------------------------
'''
from turtle import *
import turtle
from random import randint
import random
import time


#-------------Set awal
length = int(input("Input arena length : "))
screensize()
setup(width = 1.0, height = 1.0)
tur1 = ("Loki", "Thor", "Athena", "Poseidon", "Zeus", "Aphrodite")
tur2 = ("Naruto", "Goku", "Luffi", "Saitama")
tur3 = ("Newton", "Einstein", "Edison", "Tesla", "Elon")
tur4 = ("Trump", "Putin", "Kim Jong Un", "Jokowi")
color1 = ["red", "blue", "green", "yellow"]
color2 = ["orange", "purple", "pink", "magenta"]
color3 = ["black", "brown", "grey",]
color4 = ["cyan", "lime", "violet"]
start = (-length/2)
speed(0)
penup()
goto(start, 75)
finish = length/2-5
counter = 0
move = 0
hideturtle()

#-------------Gambar arena
if 200<=length<=1200:
  pendown()
  forward(length)
  right(90)
  forward(140)
  right(90)
  forward(length-40)
  right(90)
  forward(140)
  right(180)
  forward(140)
  right(90)
  forward(40)
  right(90)
  forward(140)
  penup()

#-------------Inisiasi Awal
  turtle1 = Turtle()
  turtle1.fillcolor(random.choice(color1))
  col1=turtle1.fillcolor()
  turtle1.pencolor(col1)
  turtle1.shape('turtle')

  turtle1.penup()
  turtle1.goto(start+20, 50)
  turtle1.pendown()

  for turn in range(10):
    turtle1.right(36)

  turtle2 = Turtle()
  turtle2.fillcolor(random.choice(color2))
  col2=turtle2.fillcolor()
  turtle2.pencolor(col2)
  turtle2.shape('turtle')

  turtle2.penup()
  turtle2.goto(start+20, 20)
  turtle2.pendown()

  for turn in range(10):
    turtle2.left(36)

  turtle3 = Turtle()
  turtle3.shape('turtle')
  turtle3.fillcolor(random.choice(color3))
  col3=turtle3.fillcolor()
  turtle3.pencolor(col3)

  turtle3.penup()
  turtle3.goto(start+20, -10)
  turtle3.pendown()

  for turn in range(10):
    turtle3.right(36)

  turtle4 = Turtle()
  turtle4.shape('turtle')
  turtle4.fillcolor(random.choice(color4))
  col4=turtle4.fillcolor()
  turtle4.pencolor(col4)

  turtle4.penup()
  turtle4.goto(start+20, -40)
  turtle4.pendown()

  for turn in range(10):
    turtle4.left(36)
  clock_start = time.time()
#-------------Mulai balapan
  while (turtle1.xcor()<=finish) and (turtle2.xcor()<=finish) and (turtle3.xcor()<=finish) and (turtle4.xcor()<=finish):
    counter += 1
    turtle1.forward(randint(1,15))
    turtle1.right(randint(-8,8))
    turtle2.forward(randint(1,15))
    turtle2.right(randint(-8,8))
    turtle3.forward(randint(1,15))
    turtle3.right(randint(-8,8))
    turtle4.forward(randint(1,15))
    turtle4.right(randint(-8,8))
    if -65>=turtle1.ycor():
      if 180<=turtle1.heading()<=330:
        turtle1.right(randint(-90,-80))
        turtle1.forward(randint(5,15))
      elif 180<=turtle1.heading()>=330:
        turtle1.right(randint(-30,-20))
        turtle1.forward(randint(1,15))
    elif turtle1.ycor()>=75:
      if 180>=turtle1.heading()>=60:
        turtle1.right(randint(80,90))
        turtle1.forward(randint(5,15))
      elif 180>=turtle1.heading()<=60:
        turtle1.right(randint(20,30))
        turtle1.forward(randint(1,15))
    if -65>=turtle2.ycor():
      if 180<=turtle2.heading()<=330:
        turtle2.right(randint(-90,-80))
        turtle2.forward(randint(5,15))
      elif 180<=turtle2.heading()>=330:
        turtle2.right(randint(-30,-20))
        turtle2.forward(randint(1,15))
    elif turtle2.ycor()>=75:
      if 180>=turtle2.heading()>=60:
        turtle2.right(randint(80,90))
        turtle2.forward(randint(5,15))
      elif 180>=turtle2.heading()<=60:
        turtle2.right(randint(20,30))
        turtle2.forward(randint(1,15))
    if -65>=turtle3.ycor():
      if 180<=turtle3.heading()<=330:
        turtle3.right(randint(-90,-80))
        turtle3.forward(randint(5,15))
      elif 180<=turtle3.heading()>=330:
        turtle3.right(randint(-30,-20))
        turtle3.forward(randint(1,15))
    elif turtle3.ycor()>=75:
      if 180>=turtle3.heading()>=60:
        turtle3.right(randint(80,90))
        turtle3.forward(randint(5,15))
      elif 180>=turtle3.heading()<=60:
        turtle3.right(randint(20,30))
        turtle3.forward(randint(1,15))
    if -65>=turtle4.ycor():
      if 180<=turtle4.heading()<=330:
        turtle4.right(randint(-90,-80))
        turtle4.forward(randint(5,15))
      elif 180<=turtle4.heading()>=330:
        turtle4.right(randint(-30,-20))
        turtle4.forward(randint(1,15))
    elif turtle4.ycor()>=75:
      if 180>=turtle4.heading()>=60:
        turtle4.right(randint(80,90))
        turtle4.forward(randint(5,15))
      elif 180>=turtle4.heading()<=60:
        turtle4.right(randint(20,30))
        turtle4.forward(randint(1,15))

  clock_end = time.time()
      
#-------------hasil pertandingan
  if (turtle1.xcor()>=finish) or (turtle2.xcor()>=finish) or (turtle3.xcor()>=finish) or (turtle4.xcor()>=finish):      
    if (turtle1.xcor()> turtle2.xcor()) and (turtle1.xcor()> turtle2.xcor()) and (turtle1.xcor()> turtle2.xcor()):
      juara = random.choice(tur1)
      color(turtle1.fillcolor())
    elif (turtle2.xcor()> turtle1.xcor()) and (turtle2.xcor()> turtle3.xcor()) and (turtle2.xcor()> turtle4.xcor()):
      juara = random.choice(tur2)
      color(turtle2.fillcolor())
    elif (turtle3.xcor()> turtle2.xcor()) and (turtle3.xcor()> turtle1.xcor()) and (turtle3.xcor()> turtle4.xcor()):
      juara = random.choice(tur3)
      color(turtle3.fillcolor())
    elif (turtle4.xcor()> turtle2.xcor()) and (turtle4.xcor()> turtle1.xcor()) and (turtle4.xcor()> turtle3.xcor()):
      juara = random.choice(tur4)
      color(turtle4.fillcolor())

  goto(0, -95)
  turtle.write(("The Winner is of the race is "+juara+"!"), align="center",font=("Arial", 12, "bold"))
  goto(0, -115)
  turtle.write(("Elapsed Time: "+str(round((clock_end-clock_start),3))+" seconds"), align="center",font=("Arial", 10, "bold"))
  goto(0, -145)
else:
  goto(0, 0)  
  turtle.write(("Wrong input!"), align="center",font=("Arial", 12, "bold"))
  goto(0, -20)
  turtle.write(("Please input length between 200 and 1200"), align="center",font=("Arial", 12, "bold"))
  goto(0, -40)
  left(90)
