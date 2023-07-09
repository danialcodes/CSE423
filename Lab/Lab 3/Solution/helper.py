from argtaker import args
from windowsize import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random,math

def get_random_color():
    return random.random(), random.random(), random.random()

def getInfo():
    return args.radius, [args.centerX, args.centerY], args.innerCircle
    
def drawPoint(x,y,pointSize=1):
    glPointSize(pointSize)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
def drawLines(x,y,x2,y2,pointSize=1):
    glPointSize(pointSize)
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x2, y2)
    glEnd()


def Circlepoints(x,y,cx,cy,pointSize=2):
    glPointSize(pointSize)
    glBegin(GL_POINTS)
    glVertex2f(y+cx,x+cy) #zone 0
    glVertex2f(x+cx,y+cy) #zone 1
    glVertex2f(-x+cx,y+cy) #zone 2
    glVertex2f(-y+cx,x+cy) #zone 3
    glVertex2f(-y+cx,-x+cy) #zone 4
    glVertex2f(-x+cx,-y+cy) #zone 5
    glVertex2f(x+cx,-y+cy) #zone 6
    glVertex2f(y+cx,-x+cy) #zone 7
    glEnd()

def midpointCircle(r,cx=0,cy=0):
    d = 1-r
    x = 0
    y = r

    # center point
    # drawPoint(cx,cy,pointSize=5)
    
    Circlepoints(x,y,cx,cy) 
    while(x<y):
        if(d<0):
            d+=2*x+3
        else:
            d+=2*(x-y)+5
            y-=1
        x+=1
        Circlepoints(x,y,cx,cy) 