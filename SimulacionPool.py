from graphics import *
from math import *
import sys
import time

L1 = 200.0
Lroz = 10.0

T = 150

M = 5
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

def moverBlanca(blanca, click, negra):
	t0 = time.time()
	t = 0
	DeltaT = 1/60
	n = 0
	dist = ((blanca.getCenter().getX() - click.getX())**2 + (blanca.getCenter().getY() - click.getY())**2)**0.5
	print("Dist: " + str(dist))
	V = dist / M
	print("V: " + str(V))
	angulo = degrees(atan2(blanca.getCenter().getY() - click.getY(), blanca.getCenter().getX() - click.getX()))
	print("angulo: " + str(angulo))
	while (V > 0):
		t = time.time() - t0
		if(t >= n * DeltaT):
			if(V > 0):
				VTemp = V + DeltaT * Fuerza(V, 0.1) /M
				Dx = VTemp * DeltaT * cos(radians(angulo))
				Dy = VTemp * DeltaT * sin(radians(angulo))
				V = VTemp
				if(blanca.getCenter().getX() < 1000 - RADIO and blanca.getCenter().getX() > 0 + RADIO  and blanca.getCenter().getY() < 500 - RADIO and blanca.getCenter().getY() > 0 + RADIO):
					blanca.move(Dx,Dy)
				else:
					angulo = degrees(radians(angulo) + radians(90))
				if(choque(blanca, negra)):
					moverNegra(negra, V, angulo, blanca)
					V = 0
			n = n + 1
				
def moverNegra(negra, V, angulo, blanca):
	t0 = time.time()
	t = 0
	DeltaT = 1/60
	n = 0
	angulo = degrees(atan2(negra.getCenter().getY() - blanca.getCenter().getY(), negra.getCenter().getX() - blanca.getCenter().getX()))
	print("angulo: " + str(angulo))
	while (V > 0):
		t = time.time() - t0
		if(t >= n * DeltaT):
			if(V > 0):
				VTemp = V + DeltaT * Fuerza(V, 0.1) /M
				Dx = VTemp * DeltaT * cos(radians(angulo))
				Dy = VTemp * DeltaT * sin(radians(angulo))
				V = VTemp
				if(negra.getCenter().getX() < 1000 - RADIO and negra.getCenter().getX() > 0 + RADIO  and negra.getCenter().getY() < 500 - RADIO and negra.getCenter().getY() > 0 + RADIO):
					negra.move(Dx,Dy)
				else:
					angulo = degrees(radians(angulo) + radians(90))
					print("Cambio angulo: " + str(angulo))
					V = 0
			n = n + 1


def main():
	WIN_SIZE_X = 1000
	WIN_SIZE_Y = 500
	win = GraphWin("Simulación 2", WIN_SIZE_X, WIN_SIZE_Y)
	win.setBackground("green")
	blanca = Circle(Point(X0 + 200,Y0),RADIO)
	blanca.setFill("white")
	blanca.setOutline("white")
	blanca.draw(win)

	negra = Circle(Point(X0 + 800, Y0), RADIO)
	negra.setFill("black")
	negra.draw(win)

	while (not win.closed):
		click = win.getMouse()
		print("x: " + str(click.getX()))
		print("y: " + str(click.getY()))
		moverBlanca(blanca, click, negra)

main()