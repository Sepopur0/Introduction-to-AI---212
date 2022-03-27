import pygame
import math
from pygame.constants import *
import sys
import random
pygame.init()
screen_width=1300
screen_height=650
gamezone_size= 490 #square
button_width=150
button_height=50  
#buttoncoordinate(left,right,top,bot)
startbutton_coor=[(575,725,300,350),(575,725,375,425),(575,725,450,525)]
gamebutton_coor=[(1000,1150,100,150),(1000,1150,175,225),(1000,1150,250,300),(1000,1150,325,375),(1000,1150,400,450),(1000,1150,475,525)]
cheatbutton_coor=[(1000,1150,150,225),(1000,1150,225,275),(1000,1150,300,375),(1000,1150,375,425),(1000,1150,450,500)]
#font
font = pygame.font.SysFont('calibri', 25,True,False) 
font_number=pygame.font.SysFont('calibri',30,True,False) 
#colors
black=(0,0,0)
white=(255,255,255)
neon_dark_green=(0,132,67)
red_1=(255,0,17)
yellow=(255,255,0)
gray=(128,128,128)
