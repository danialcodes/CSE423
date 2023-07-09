from helper import *

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

    

def showScreen(r,cx,cy,circleCount):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    
    centerX,centerY = cx+windowX//2,cy+windowY//2

    # drawLines(centerX,0,centerY,windowY,pointSize=5)
    # drawLines(0,centerY,windowX,centerY,pointSize=5)
    # drawLines(0,0,windowX,windowY,pointSize=5)
    # drawLines(0,windowY,windowX,0,pointSize=5)

    midpointCircle(r,centerX,centerY)
    degree = 360/circleCount
    for i in range(circleCount):
        x = (r/2) * math.cos(degree*(math.pi/180))
        y = (r/2)* math.sin(degree*(math.pi/180))
        degree += 360/circleCount
        midpointCircle(r//2,centerX+x,centerY+y)
    glutSwapBuffers()   



r,(cx,cy),circleCount = getInfo()

glutInit()
glutInitDisplayMode(GLUT_RGBA)

# windowsize, window position and window title
glutInitWindowSize(windowX, windowY)
glutInitWindowPosition(windowPosX, windowPosY)

wind= glutCreateWindow(bytes(windowName, "utf-8"))

# display function
glutDisplayFunc(lambda: showScreen(r,cx,cy,circleCount))

glutMainLoop()