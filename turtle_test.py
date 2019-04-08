import turtle
import time

# input ('엔터를 치면 거북이를 소개합니다.')
#
# turtle.shape('turtle')
#
# time.sleep(1)
# turtle.forward(100)
#
# time.sleep(1)
# turtle.forward(100)
#
# time.sleep(1)
# turtle.left(90)
# turtle.forward(100)
#
# time.sleep(1)
# turtle.right(90)
# turtle.forward(100)
#
# turtle.done()
############################################
# turtle.pensize(10)
#
# input('엔터를 치면 사각형을 그립니다.')
#
# turtle.color("red")
# turtle.forward(200)
#
# turtle.left(90)
# turtle.forward(200)
#
# turtle.left(90)
# turtle.forward(200)
#
# turtle.left(90)
# turtle.forward(200)
#
# turtle.done()
##############################################
# input('엔터를 치면 빨간색 삼각형을 그립니다.')
#
# turtle.color("green")
#
# turtle.right(30)
# turtle.forward(300)
#
# turtle.left(120)
# turtle.forward(300)
#
# turtle.left(120)
# turtle.forward(300)
#
# turtle.done()
###############################################
# input('엔터를 치면 파란색 굵은 원을 그립니다.')
#
# turtle.right(30)
# turtle.color("blue")
# turtle.circle(200)
#
# turtle.done()
################################################

turtle.shape('turtle')

size = input('사각형의 크기를 입력하세요.[100~300] ')
color = input('선의 색깔을 입력하세요.[red / green / blue] ')
thick = input('펜의 굵기를 입력하세요.[1~30]    ')

angle = 90
thick = int(thick)
size = int(size)

turtle.color(color)
turtle.pensize(thick)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.done()
