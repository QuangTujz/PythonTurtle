from turtle import *
import colorsys

speed(0)
bgcolor('black')
hue=0.0
hideturtle()
pensize(3)

for i in range(300):
	color=colorsys.hsv_to_rgb(hue,1,1)
	pencolor(color)
	fd(i)
	rt(98)
	hue+=0.005

done()