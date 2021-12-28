class Nodo():
    def __init__(self, padre, casilla, g, h):
        self.padre = padre
        self.casilla = casilla
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def getPadre (self):
        return self.padre

    def getCasilla (self):
        return self.casilla

    def getG (self):
        return self.g

    def getH (self):
        return self.h

    def getF (self):
        return self.f

    def setPadre(self, nodo):
        self.padre = nodo

    def setG(self, g):
        self.g = g

    def setF(self, f):
        self.f = f

    def setH(self, h):
        self.h = h