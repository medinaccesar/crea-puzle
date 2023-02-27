from Constantes import Configuracion as conf
from manejadores.PuzzleManager import PuzzleManager

class MotorSecuencial(PuzzleManager):

    def __init__(self):
        super().__init__()
        self._tipoEstrategia = conf.ESTRATEGIA_SECUENCIAL

    def resolver(self):
        # TODO: resolver de forma secuencial
        pass
