from helper import *
from number import draw_numbers

def task1():
    for i in range(50):
        r,g,b = get_random_color()
        glColor3f(r,g,b)
        randX = get_random_point(0,windowX)
        randY = get_random_point(0,windowY)
        draw_point(randX,randY)

def task2():
    hollowX = 50
    hollowY = 30
    triangleGap = 190
    # A --> Lower Left Corner  --> ( hollowX,hollowY )
    Ax,Ay = hollowX,hollowY 
    # B --> Lower Right Corner --> ( windowX-hollowX,hollowY )
    Bx,By = windowX-hollowX,Ay
    # C --> Upper Right Corner --> ( windowX-hollowX,windowY-hollowY-triangleGap )
    Cx,Cy = windowX-hollowX,windowY-hollowY-triangleGap
    # D --> Upper Right Corner --> ( hollowX,windowY-hollowY-triangleGap )
    Dx,Dy = Ax,windowY-hollowY-triangleGap

    midpointX = (windowX-hollowX*2)//2
    # M --> Mid upper point    --> ( hollowX+midpointX,windowY-hollowY )
    Mx,My = hollowX+midpointX,windowY-hollowY
    
    
    # Midline 
    # draw_line( hollowX+midpointX,hollowY,  Mx,My )

    # A --> B
    draw_line( Ax,Ay,  Bx,By )
    # A --> D
    draw_line( Ax,Ay,  Dx,Dy)
    # B --> C
    draw_line( Bx,By,  Cx,Cy )

    # # C --> D
    # draw_line( windowX-hollowX, windowY-hollowX-triangleGap, hollowX, windowY-hollowX-triangleGap )

    # M --> D , D --> C , C --> M (Triangle)
    draw_triangle_hollow( Mx,My,   Dx,Dy,   Cx,Cy)

    # left side window
    gapXSide = 20
    gapYSide = 40
    lengthSide = 100
    # upper left corner --> Dx+gapXSide, Dy-gapYSide
    lwindowUx,lwindowUy = Dx+gapXSide, Dy-gapYSide
    draw_quad_hollow( lwindowUx,lwindowUy,   lwindowUx+lengthSide,lwindowUy,   lwindowUx+lengthSide,lwindowUy-lengthSide,   lwindowUx,lwindowUy-lengthSide )
    
    # upper right corner --> Cx-gapXSide, Cy-gapYSide
    RwindowUx,RwindowUy = Cx-gapXSide, Cy-gapYSide
    draw_quad_hollow( RwindowUx,RwindowUy,   RwindowUx-lengthSide,RwindowUy,   RwindowUx-lengthSide,RwindowUy-lengthSide,   RwindowUx,RwindowUy-lengthSide )

    # door
    doorGap = lengthSide//2.5
    doorLength = lengthSide*1.3

    draw_quad_hollow( Mx-doorGap,Ay,   Mx-doorGap,Ay+doorLength, Mx+doorGap,Ay+doorLength, Mx+doorGap,Ay)

    draw_line(Mx-doorGap,Ay+doorLength, Mx*1.09, Ay+doorLength*.9)
    draw_line(Mx*1.09, Ay+doorLength*.9, Mx*1.09, Ay+doorLength*.1)
    draw_line(Mx*1.09, Ay+doorLength*.1, Mx-doorGap,Ay)

    # door nob
    draw_point(Mx*1.06, Ay+doorLength*.5)

def task3():
    x = 130
    if(args.stdId):
        stdId = args.stdId
    else:
        stdId = "20101534"
    
    for i in stdId:
        r,g,b = get_random_color()
        glColor3f(r,g,b)
        x = draw_numbers(int(i), x)
    glutSwapBuffers()