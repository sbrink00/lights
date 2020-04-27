from display import *
from draw import *
from parser import *
from matrix import *
import math

# lighting values
view = [0, 0, 1];
ambient = [50, 50, 50]
light = [[0.5, .75, 1], [0, 255, 255]]
areflect = [0.1, 0.1, 0.1]
dreflect = [0.5, 0.5, 0.5]
sreflect = [200, 200, 200]

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]

parse_file( 'script', edges, polygons, csystems, screen, zbuffer, color, view, ambient, light, areflect, dreflect, sreflect)

# def ef(x):
#   return int(round((-0.00749 * x * x) + (3.22875 * x) + 93.54545))
#
# startX = 450
# endX = 12
# numImages = 100
# dx = ((endX - startX) * 1.0 / numImages)
# x = startX - dx
# for i in range(1, numImages + 2):
#   print(i)
#   screen = new_screen()
#   zbuffer = new_zbuffer()
#   color = [ 0, 255, 0 ]
#   edges = []
#   polygons = []
#   t = new_matrix()
#   ident(t)
#   csystems = [ t ]
#   x += dx
#   x = int(round(x))
#   y = ef(x)
#   with open("script6", "r") as f:
#     lines = f.readlines()
#   for j in range(len(lines)):
#     if lines[j].strip() == "save":
#       lines[j + 1] = "pic" + str(i) + ".png\n"
#     if lines[j].strip() == "sphere":
#       lines[j + 1] = str(x) + " " + str(y) + " -10 25\n"
#   with open("script6", "w") as f: f.writelines(lines)
#   parse_file( 'script6', edges, polygons, csystems, screen, zbuffer, color, view, ambient, light, areflect, dreflect, sreflect)
