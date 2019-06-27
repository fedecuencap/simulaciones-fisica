from graphics import *
from math import *
from multiprocessing  import Process

import sys
import time

L1 = 200.0
Lroz = 10.0

T = 150

M = 2
X0 = 100
Y0 = 250
V0 = 20

Ptope = X0 + (L1*2) + Lroz

RADIO = 30

def choque(ball1, ball2):
    dist = ((ball1.getCenter().getX() - ball2.getCenter().getX())**2 + (ball1.getCenter().getY() - ball2.getCenter().getY())**2)**0.5
    if dist <= RADIO*2:
        return True
    else:
        return False


def Fuerza(v, b):
	return - b*v 

def mover(blanca, click, roja):
	t0 = time.time()
	t = 0
	DeltaT = 1/60
	n = 0
	dist = ((blanca.getCenter().getX() - click.getX())**2 + (blanca.getCenter().getY() - click.getY())**2)**0.5
	V = dist / M
	angBlanca = degrees(atan2(blanca.getCenter().getY() - click.getY(), blanca.getCenter().getX() - click.getX()))
	VxBlanca = V * cos(radians(angBlanca))
	VyBlanca = V * sin(radians(angBlanca))
	VxRoja = 0
	VyRoja = 0
	while ( (abs(VxBlanca) >= 0.5 and abs(VyBlanca) >= 0.5) or (abs(VxRoja) >= 0.5 and abs(VyRoja) >= 0.5) ):
		t = time.time() - t0
		if(t >= n * DeltaT):
			if(abs(VxBlanca) >= 0.5 and abs(VyBlanca) >= 0.5):
				VxBlancaTemp = VxBlanca + DeltaT * (Fuerza(VxBlanca, 0.1)/M)
				VyBlancaTemp = VyBlanca + DeltaT * (Fuerza(VyBlanca, 0.1)/M)
				DxBlanca = VxBlancaTemp * DeltaT
				DyBlanca = VyBlancaTemp * DeltaT
				VxBlanca = VxBlancaTemp
				VyBlanca = VyBlancaTemp
				blanca.move(DxBlanca,DyBlanca)
				if(abs(blanca.getCenter().getX() - 1000) <= RADIO or blanca.getCenter().getX() <= RADIO):
					VxBlanca = - VxBlanca
				if(abs(blanca.getCenter().getY() - 500) <= RADIO or blanca.getCenter().getY() <= RADIO):
					VyBlanca = - VyBlanca
			if(choque(blanca, roja)):
				angChoque = degrees(atan2(roja.getCenter().getY() - blanca.getCenter().getY(), roja.getCenter().getX() - blanca.getCenter().getX()))
				print("angChoque: " + str(angChoque))
				VBlanca = (((VxBlanca)**2 + (VyBlanca)**2)**0.5)*sin(angChoque)
				print("VBlanca: " + str(VBlanca))
				VRoja = (((VxBlanca)**2 + (VyBlanca)**2)**0.5)*cos(angChoque)
				print("VRoja: " + str(VRoja))
				VxRoja = VRoja * cos(radians(angChoque))
				print("VxRoja: " + str(VxRoja))
				VyRoja = VRoja * sin(radians(angChoque))
				print("VyRoja: " + str(VyRoja))
				VxBlanca = VBlanca * sin(radians(90 - angChoque))
				print("VxBlanca: " + str(VxBlanca))
				VyBlanca = VBlanca * cos(radians(90 - angChoque))
				print("VyBlanca: " + str(VyBlanca))
			if(abs(VxRoja) >= 0.5 and abs(VyRoja) >= 0.5):
				VxRojaTemp = VxRoja + DeltaT * (Fuerza(VxRoja, 0.1)/M)
				VyRojaTemp = VyRoja + DeltaT * (Fuerza(VyRoja, 0.1)/M)
				DxRoja = VxRojaTemp * DeltaT
				DyRoja = VyRojaTemp * DeltaT
				VxRoja = VxRojaTemp
				VyRoja = VyRojaTemp
				roja.move(DxRoja,DyRoja)
				if(abs(roja.getCenter().getX() - 1000) <= RADIO or roja.getCenter().getX() <= RADIO):
					VxRoja = - VxRoja
				if(abs(roja.getCenter().getY() - 500) <= RADIO or roja.getCenter().getY() <= RADIO):
					VyRoja = - VyRoja
			n = n + 1

def main():
	WIN_SIZE_X = 1000
	WIN_SIZE_Y = 500
	win = GraphWin("Simulación 2", WIN_SIZE_X, WIN_SIZE_Y)
	win.setBackground("green")
	angChoque
	blanca = Circle(Point(X0 + 200,Y0),RADIO)
	blanca.setFill("white")
	blanca.setOutline("white")
	blanca.draw(win)

	roja = Circle(Point(X0 + 800, Y0), RADIO)
	roja.setFill("red")
	roja.setOutline("red")
	roja.draw(win)

	while (not win.closed):
		click = win.getMouse()
		mover(blanca, click, roja)

main()