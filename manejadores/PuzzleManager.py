from Constantes import Configuracion as conf
from abc import ABCMeta
from abc import abstractmethod


class PuzzleManager(metaclass=ABCMeta):

    def __init__(self):
        self._tipoEstrategia = conf.ESTRATEGIA
        self.dimensiones = ()  # dimensiones del tapiz

    @property
    def tipoEstrategia(self):
        return self._tipoEstrategia

    # Gira la pieza en sentido anti horario y la devuelve

    def girarPieza(self, pieza):
        piezaAux = pieza.pop(0)
        pieza.append(piezaAux)
        return pieza

    @abstractmethod
    def resolver(self):
        pass

    def getAnchoTapiz(self):
        return self.dimensiones[0]

    def getAltoTapiz(self):
        return self.dimensiones[1]

    def esEsquinaSuperiorDcha(self, x, y):
        tope = self.getAltoTapiz()-1
        return x == 0 and y == tope

    def esEsquinaSuperiorIzda(self, x, y):
        return x == 0 and y == 0

    def esEsquinaInferiorDcha(self, x, y):
        tope = self.getAltoTapiz()-1
        return x == tope and y == tope

    def esEsquinaInferiorIzda(self, x, y):
        tope = self.getAltoTapiz()-1
        return x == tope and y == 0

    def esMarcoSuperior(self, x):
        return (x == 0)

    def esMarcoInferior(self, x):
        tope = self.getAltoTapiz()-1
        return (x == tope)

    def esMarcoIzquierdo(self, y):
        return (y == 0)

    def esMarcoDerecho(self, y):
        tope = self.getAltoTapiz()-1
        return (y == tope)
