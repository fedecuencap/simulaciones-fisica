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

def FuerzaY(k, Ymas1, Ymenos1, Y):
	f = (-k * (Y - Ymenos1)) - (k * (Y - Ymas1))
	return f

def PosicionY(t, signo):
	if t <= (2 * pi)/(8 * pi):
		return signo * 2 * DeltaX * (1 - cos(8 * pi * t))
	else:
		return 0

def main():
	
	file = open("C:/Users/fcuenca/Documents/fisica1/SimulacionPool/Simulacion4Datos.txt","w") 

	WIN_SIZE_X = 1200
	WIN_SIZE_Y = 300
	win = GraphWin("Simulación 4", WIN_SIZE_X, WIN_SIZE_Y)

	RADIO = 5
	lstC = []
	lstV = []
	lstY = []
	
	for x in range(0, CountNodes):
		circle = Circle(Point(X0 + x*DeltaX,Y0),RADIO)
		circle.draw(win)
		lstC.append(circle)
		lstV.append(0)
		lstY.append(Y0)

	win.getMouse()

	t0 = time.time()
	t = 0

	DeltaT = 1/120
	n = 0

	signo = 1

	while(t < T):

		t = time.time() - t0

		if(t >= n * DeltaT):


			D0y = PosicionY(t, signo)
			lstC[0].move(0, D0y)
			lstY[0] = lstY[0] + D0y
			signo = signo * (-1)

			file.write("{x: " + str(0) + ", D0y: " + str(D0y) + ", lstY[0]: " + str(lstY[0]) + ", t: " + str(t) + "}\n")

			for x in range(1, CountNodes - 1):
				
				Vy = lstV[x] + DeltaT * FuerzaY(0.7, lstY[x + 1], lstY[x - 1], lstY[x])/M
				Dy = Vy * DeltaT

				file.write("{x: " + str(x) + ", Vy: " + str(Vy) + ", Dy: " + str(Dy) + ", t: " + str(t)  + ", lstV[x]: " + str(lstV[x])  + ", lstY[x + 1]: " + str(lstY[x + 1]) + ", lstY[x - 1]: " + str(lstY[x - 1]) + ", lstY[x]: " + str(lstY[x]) + "}\n")
				lstC[x].move(0,Dy)

				Py = lstC[x].getCenter().getY()

				lstY[x] = Py

				lstV[x] = Vy
			
			n = n + 1

	file.close()

	win.close()

main()