from graphics import *
from math import *
import sys
import time

CountNodes = 118
DeltaX = 10

T = 10

M = 5
X0 = 10
Y0 = 150

def FuerzaY(M, v, k, Ymas1, Ymenos1, Y):
	return -k * (Y - Ymenos1) - k * ( Y - Ymas1)

def PosicionY(w, t, A):
	if t <= (2 * pi)/w:
		return A *(1 - cos(w*t))
	else:
		return 0

def main():
	
	WIN_SIZE_X = 1200
	WIN_SIZE_Y = 300
	win = GraphWin("Simulación 4", WIN_SIZE_X, WIN_SIZE_Y)

	RADIO = 5
	lstC = []
	lstV = []
	lstY = []
	
	for x in range(CountNodes):
		circle = Circle(Point(X0 + x*DeltaX,Y0),RADIO)
		circle.draw(win)
		lstC.append(circle)
		lstV.append(0)
		lstY.append(Y0)

	lstC[0].move(0, - 10)
	lstY[0] = lstY[0] - 10 
	win.getMouse()

	t0 = time.time()
	t = 0

	DeltaT = 1/120
	n = 0

	while(t < T):

		t = time.time() - t0

		if(t >= n * DeltaT):

			D0y = lstY[0] - PosicionY(2,t,2)
			lstC[0].move(0, D0y)
			lstY[0] = lstY[0] + D0y

			for x in range(1, CountNodes - 1):
				
				Vy = lstV[x] + DeltaT * FuerzaY(M, lstV[x], 0.7, lstY[x + 1], lstY[x - 1], lstY[x])/M
			
				Dy = Vy * DeltaT

				lstC[x].move(0,Dy)

				Py = lstC[x].getCenter().getY()

				lstY[x] = Py

				lstV[x] = Vy
			
			n = n + 1

	win.close()

main()