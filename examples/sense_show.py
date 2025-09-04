#!/usr/bin/env python3
"""
This module is an example of driving the sense hat with blue dot.

It shows an array of dots on the ui each corresponding to a pixel on the 16x16 array on the sense hat.

Tapping on a dot toggles that pixel, it is very satisfying.
"""

from sense_hat import SenseHat
from time import sleep
from bluedot import BlueDot
from signal import pause

sense = SenseHat()
bd=BlueDot(cols=8, rows=8)
for x in range(8):
    for y in range(8):
        bd[x,y].color=(50,50,50)

def pressed(pos):
    "handler for bd.when_pressed that toggles a pixel"
    print("button {}.{} pressed".format(pos.col, pos.row))
    pixel = sense.get_pixel(pos.col, pos.row)
    if(pixel[2]): # is there blue in the pixel?
        sense.set_pixel(pos.col, pos.row, 0,0,0)
        bd[pos.col, pos.row].color = (50,50,50)
    else:
        sense.set_pixel(pos.col, pos.row, 0,0,255)
        bd[pos.col, pos.row].color = (0,0,255)

    
bd.when_pressed = pressed

sense.clear(0,0,255)
sleep(1)
# sense.show_message("PotatoGirl!")

sense.show_message("BlueDot!")
sense.clear(0,0,0)
pause()


