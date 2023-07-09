from helper import *
from number import draw_numbers

def iterate():
    glViewport(0, 0, windowX, windowY)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, windowX, 0.0, windowY, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    

def showScreen(n):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    x = windowX//2-40

    for num in n:
        x = draw_numbers(int(num), x)
    glutSwapBuffers()   
    
    glutSwapBuffers()



n = getStudentId()
windowName = f"Student Id: {n}.Let's draw: {n[-2:]}"

glutInit()
glutInitDisplayMode(GLUT_RGBA)

# windowsize, window position and window title
glutInitWindowSize(windowX, windowY)
glutInitWindowPosition(windowPosX, windowPosY)

wind= glutCreateWindow(bytes(windowName, "utf-8"))

# display function
glutDisplayFunc(lambda: showScreen(n[-2:]))

glutMainLoop()