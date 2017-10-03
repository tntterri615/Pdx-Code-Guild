'''
this draws a stick figure using turtle
'''

from turtle import *


#make arms

forward(100)
left(180)
forward(50)
right(90)
forward(20)
left(90)

fillcolor('blue')
begin_fill()

#make head

edge_length = 50
n_sides = 25

i = 0
while i < n_sides:
	forward(edge_length * 2/n_sides)
	right(360/n_sides)
	i = i + 1

end_fill()

#make body and legs

left(90)
forward(120)
left(65)
forward(55)
left(180)
forward(55)
left(50)
forward(55)

done()

