import random
from argtaker import args
from windowsize import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Random
def get_random_color():
    return random.random(), random.random(), random.random()
def get_random_point(start,end):
    return random.randint(start,end)

def getTaskNumber():
    if(args.task):
        return args.task
    else:
        return int(input("Please enter task number: "))

# Draw Functions
def draw_line(x1, y1,x2,y2,pixel_size=5):
    # glPointSize(pixel_size)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()
def draw_point(x, y,pixel_size=5):
    glPointSize(pixel_size) 
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
def draw_triangle_hollow(x1, y1,x2,y2,x3,y3,pixel_size=5):
    # glPointSize(pixel_size)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)

    glVertex2f(x2,y2)
    glVertex2f(x3,y3)

    glVertex2f(x3,y3)
    glVertex2f(x1,y1)

    glEnd()

def draw_quad_hollow(x1, y1,x2,y2,x3,y3,x4,y4,pixel_size=5):
    # glPointSize(pixel_size)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)

    glVertex2f(x2,y2)
    glVertex2f(x3,y3)

    glVertex2f(x3,y3)
    glVertex2f(x4,y4)

    glVertex2f(x4,y4)
    glVertex2f(x1,y1)

    glEnd()    

