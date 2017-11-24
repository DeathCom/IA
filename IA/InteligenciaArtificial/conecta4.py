#conecta 4 con poda alfa-beta
import sys
import copy
MAX=1
MIN=-1
MAX_PROFUNDIDAD=4

def negamax(tablero, jugador, profundidad, alfa, beta):
	max_puntuacion= -sys.maxint-1
	alfa_local=alfa
	for jugada in range(7):
		#columana totalmente llena?
		if tablero[0][jugada] ==0:
			tableroaux=copy.deepcopy(tablero)
			insertar_ficha(tableroaux, jugada, jugador)
			if game_over(tableroaux) or profundidad ==0:
				return [evalua_jugada(tableroaux, jugador), jugada]
			else:
				puntuacion== -negamax(tableroaux, jugador*(-1), \
					profundidad-1, -beta, -alfa_local)[0]
			if profundidad>max_puntuacion:
				max_puntuacion=puntuacion
				jugada_max=jugada

			#poda alfa-beta
			if max_puntuacion>=beta:
				break
			if max_puntuacion>alfa_local:
				alfa_local=max_puntuacion
	return [max_puntuacion, jugada_max]

def evalua_jugada(tablero, jugador):
	n2=comprueba_linea(tablero, 2 ,jugador)[1]
	n3=comprueba_linea(tablero, 3, jugador)[1]
	n4=comprueba_linea(tablero, 3, jugador)[1]
	valor_jugada=4*n2+9*n3+1000*n4
	return valor_jugada

def game_over(tablero):
	#hay tablas?
	no_tablas=False
	for i in range(7):
		for j in range(7):
			if tablero[i][j]==0:
				no_tablas=True
	#hay ganador?
	if ganador(tablero)[0]==0 and no_tablas:
		return False
	else:
		return True

def comprueba_linea(tablero, n, jugador):
	#comprueba si hay una linea en n filas
	ganador=0
	num_lineas=0
	lineas_posibles=8-n
	pass