from helper import *
from tasks import *


def iterate():
    glViewport(0, 0, windowX, windowY)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, windowX, 0.0, windowY, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen(n):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    task = [task1,task2,task3]
    task[n-1]()



    
    glutSwapBuffers()



n = getTaskNumber()

glutInit()
glutInitDisplayMode(GLUT_RGBA)

# windowsize, window position and window title
glutInitWindowSize(windowX, windowY)
glutInitWindowPosition(windowPosX, windowPosY)

wind= glutCreateWindow(bytes(windowName, "utf-8"))

# display function
glutDisplayFunc(lambda: showScreen(n))

glutMainLoop()
