from turtle import *
import colorsys

speed(0)  
bgcolor("black")
h = 0  


for i in range(36):  
    for j in range(6):  
        c = colorsys.hsv_to_rgb(h, 1, 1)  
        color(c)  
        h += 0.005  
        circle(100 + j * 10, 60)  
        lt(60)  
    rt(10)  

for i in range(36):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.005
    circle(50, 120)  
    rt(10)  

done()  