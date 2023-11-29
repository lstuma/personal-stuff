import math
import time
import os
from chafa import *
from random import choice


height = 50
width = 230

config = CanvasConfig()
config.width = width
config.height = height
pixels = [[0]*width]*height
canvas = Canvas(config)


def set(x,y,rgb, marker='block'):
	match(marker):
		case 'block':
			canvas[y,x].bg_color = rgb
		case 'point':
			canvas[y,x].char = '·'
			canvas[y,x].fg_color = rgb
		case 'x':
			canvas[y,x].char = 'x'
			canvas[y,x].fg_color = rgb
		case 'circle':
			marker = '⚫'
			set(x,y,rgb,marker)
		case 'star':
			marker = '★'
			set(x,y,rgb,marker)
		case 'star2':
			marker = '✪'
			set(x,y,rgb,marker)
		case 'bits':
			marker = choice(('0','1'))
			set(x,y,rgb,marker)
		case 'flower':
			marker = '✿'
			set(x,y,rgb,marker)
		case _:
			canvas[y,x].char = marker
			canvas[y,x].fg_color = rgb


def flush():
	canvas.draw_all_pixels(
    chafa.PixelType.CHAFA_PIXEL_RGBA8_UNASSOCIATED,
    [],
    1, 1, 1
	)

def render():
	os.system('clear')
	print(canvas.print().decode())

def setup():
	flush()

def sin(x):
	y = int(height/2+math.sin(x)*(height/4))
	return y


if __name__ == '__main__':
	setup()

	color = (0,0,255)
	color_change = (1,0,-1)

	i = 0
	x = 0
	while True:
		y = sin(i)
		set(x, y, color, 'block')
		color = (color[0]+color_change[0], 
				 color[1]+color_change[1],
				 color[2]+color_change[2])
		if color[0] > 250:
			color_change = (-1,1,0)
		elif color[1] > 250:
			color_change = (0,-1,1)
		elif color[2] > 250:
			color_change = (1,0,-1)
		print(i)
		i += .035
		x += 1
		if x >= width:
			x = 0
			flush()

		render()
		time.sleep(.005)
