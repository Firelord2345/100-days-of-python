from turtle import Turtle,Screen
import random
tur=Turtle()
tur.shape("arrow")
tur.penup()
tur.setheading(200)
tur.forward(100)
tur.setheading(0)
no_doubts=100
for _ in range (1,no_doubts+1):
    tur.dot(20,"red")
    
    tur.forward(50)
    if _ % 10 ==0:
        tur.setheading(90)
        tur.forward(50)
        tur.left(90)
        tur.forward(500)
        tur.setheading(0)

        
       
      
      

# tur.shape("turtle")
# for i in range(0,4):
    
#   tur.forward(100)
#   tur.left(90)
screen=Screen()
screen.exitonclick()
