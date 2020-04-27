import math
from display import *


# view = [0, 0, 1];
# ambient = [50, 50, 50]
# light = [[0.5, 0.75, 1], [0, 255, 255]]
# areflect = [0.1, 0.1, 0.1]
# dreflect = [0.5, 0.5, 0.5]
# sreflect = [0.5, 0.5, 0.5]

  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 8

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    normalize(normal)
    normalize(view)
    normalize(light[0])
    a = calculate_ambient(ambient, areflect)
    d = calculate_diffuse(light, dreflect, normal)
    s = calculate_specular(light, sreflect, view, normal)
    l = [x + y + z for x,y,z in zip(a, d, s)]
    return limit_color(l)

def calculate_ambient(alight, areflect):
    return [x * y for x,y in zip(alight, areflect)]

def calculate_diffuse(light, dreflect, normal):
    ndotl = dot_product(light[0], normal)
    return [ndotl * x * y for x,y in zip(light[1], dreflect)]

def calculate_specular(light, sreflect, view, normal):
    ndotl = dot_product(light[0], normal)
    v = [2 * ndotl * x for x in normal]
    v = [x - y for x,y in zip(v, light[0])]
    v = dot_product(v, view)
    v = v ** SPECULAR_EXP
    return [v * x * y for x,y in zip(light[0], sreflect)]

def limit_color(color):
    return [255 if x > 255 else 0 if x < 0 else round(int(x)) for x in color]

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = 1.0 * vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
