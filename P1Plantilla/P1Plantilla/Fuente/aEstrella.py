# aEstrella(mapi, origen, destino, camino)
from mapa import *
from nodo import *
from casilla import *
import numpy as np
import scipy.spatial.distance as dist

# Construye la matriz para guardar el camino
def inic(mapi):
    cam = []
    for i in range(mapi.alto):
        cam.append([])
        for j in range(mapi.ancho):
            cam[i].append(-1)

    return cam



def adyacentes (casilla):
    adya = []
    adya.append(Casilla(casilla.getFila() - 1,casilla.getCol()))
    adya.append(Casilla(casilla.getFila() - 1, casilla.getCol() + 1))
    adya.append(Casilla(casilla.getFila(), casilla.getCol() + 1))
    adya.append(Casilla(casilla.getFila() + 1, casilla.getCol() + 1))
    adya.append(Casilla(casilla.getFila() + 1, casilla.getCol()))
    adya.append(Casilla(casilla.getFila() + 1, casilla.getCol() - 1))
    adya.append(Casilla(casilla.getFila(), casilla.getCol() - 1))
    adya.append(Casilla(casilla.getFila() - 1, casilla.getCol() - 1))

    return adya


def exploracion(mapa, casilla, destino, nodoBest, lInterior, lFrontera):
    coste = 0
    pos = -1
    g = 0
    h = 0
    esta = False

    if mapa.getCelda(casilla.getFila(),casilla.getCol()) != 1:
        for i in lInterior:
            if i.casilla.getFila() == casilla.getFila() and i.casilla.getCol() == casilla.getCol():
                esta = True
            if esta:
                break
        if not esta:
            if casilla.getFila() - 1 == nodoBest.getCasilla().getFila() and casilla.getCol() + 1 == nodoBest.getCasilla().getCol():
                coste = 1.5
            elif casilla.getFila() + 1 == nodoBest.getCasilla().getFila() and casilla.getCol() + 1 == nodoBest.getCasilla().getCol():
                coste = 1.5
            elif casilla.getFila() + 1 == nodoBest.getCasilla().getFila() and casilla.getCol() - 1 == nodoBest.getCasilla().getCol():
                coste = 1.5
            elif casilla.getFila() - 1 == nodoBest.getCasilla().getFila() and casilla.getCol() - 1 == nodoBest.getCasilla().getCol():
                coste = 1.5
            else:
                coste = 1

            g = nodoBest.getG() + coste
            i = 0
            while pos == -1:
                if len(lFrontera) == 0 or i >= len(lFrontera):
                    break
                if lFrontera[i].casilla.getFila() == casilla.getFila() and lFrontera[i].casilla.getCol() == casilla.getCol():
                    pos = i
                i = i + 1

            if pos == -1:
                h = 0
                #h = manhattan(casilla, destino)
                #h = euclidea(casilla, destino)
                #h = chebyshev(casilla, destino)
                #h = coseno(casilla, destino)

                lFrontera.append(Nodo(nodoBest, casilla, g, h))
            else:
                if g < lFrontera[pos].getG():
                    lFrontera[pos].setPadre(nodoBest)
                    lFrontera[pos].setG(g)
                    lFrontera[pos].setF(g + lFrontera[pos].getH())

def mostrarExpandidos(caminoExpandido):
    for i in range(len(caminoExpandido)):
        for j in range(len(caminoExpandido[i])):
            if caminoExpandido[i][j]>-1 and caminoExpandido[i][j]<10:
                print(" ",end="")
            print(caminoExpandido[i][j], end=" ")
        print('\n')


def manhattan(origen, destino):
    return abs(destino.getFila() - origen.getFila()) + abs(destino.getCol() - origen.getCol())

def euclidea(origen, destino):
  return pow(pow(abs(destino.getFila() - origen.getFila()), 2) + pow(abs(destino.getCol() - origen.getCol()), 2), 0.5)


def chebyshev(origen, destino):
    vector1 = np.array([origen.getFila(), origen.getCol()])
    vector2 = np.array([destino.getFila(), destino.getCol()])

    op2=np.linalg.norm(vector1-vector2,ord=np.inf)
    return op2


def coseno(origen, destino):
    vector1 = np.array([origen.getFila(), origen.getCol()])
    vector2 = np.array([destino.getFila(), destino.getCol()])

    op7 = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * (np.linalg.norm(vector2)))

    return op7


def aEstrella(mapa, origen, destino, camino):
    expandidos = 0
    camino_expandido = inic(mapa)
    coste_total = 0
    lInterior = []
    lFrontera = []
    adya = []
    encontrado = False
    resultado = 0

    h = 0
    #h = manhattan(origen, destino)
    #h = euclidea(origen, destino)
    #h = chebyshev(origen, destino)
    #h = coseno(origen, destino)
    nodoInicial = Nodo(None, origen, 0, h)
    lFrontera.append(nodoInicial)

    while len(lFrontera) != 0 and encontrado == False:
        best = lFrontera[0] #Nodo con el que comprobaremos

        for i in lFrontera:
            if i.getF() < best.getF():
                best = i

        lFrontera.remove(best)
        lInterior.append(best) #Nodo evaluado

        camino_expandido[best.getCasilla().getFila()][best.getCasilla().getCol()] = expandidos
        expandidos = expandidos + 1

        if best.getCasilla().getFila() == destino.getFila() and best.getCasilla().getCol() == destino.getCol():
            coste_total = best.getG()
            resultado = coste_total
            encontrado = True

            while best != None:
                if best.padre != None:
                    camino[best.getCasilla().getFila()][best.getCasilla().getCol()] = 'X'

                best = best.padre
        else:
            adya = adyacentes(best.getCasilla())

            for i in adya:
                exploracion(mapa, i, destino, best, lInterior, lFrontera)

    mostrarExpandidos(camino_expandido)
    return resultado