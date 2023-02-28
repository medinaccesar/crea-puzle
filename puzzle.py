import argparse
import sys

from manejadores.motores.MotorSecuencial import MotorSecuencial
from manejadores.crear import Fabrica
from Constantes import Configuracion as conf


class Puzzle():
    def __init__(self):

        self.pManager = MotorSecuencial()

    def mostrarAyuda(self):
        print('Ayuda')
        print('uso: puzzle.py [-h] [-d DIM] [--version]')
        print()

    def creditos(self):
        print()
        print(conf.NOMBRE_AP, ' Versión', conf.VERSION)
        print('Por', conf.CREDITOS)
        print()

    # TODO: dividir el parser del main para dejarlo más legible
    def parseArgs(args=sys.argv[1:]):
        parser = argparse.ArgumentParser(
            description=conf.NOMBRE_AP+" "+str(conf.VERSION))
        subparsers = parser.add_subparsers(help='sub-command help')

        return parser.parse_args(args)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=conf.NOMBRE_AP+" "+str(conf.VERSION))
    parser.add_argument("-d", "--dim", type=int, required=True,
                        help=" Dimensiones del rompecabezas a crear, por ejemplo:  python puzzle.py -d 5 ")
    parser.version = str(conf.VERSION)
    parser.add_argument('--version', action='version')

    args = parser.parse_args()
    if args.dim:
        fabrica = Fabrica(args.dim)
        print('Se crean los ficheros fuente y solución para un puzle de',
              args.dim, 'x', args.dim, 'en la carpeta',conf.RECURSOS)
        fabrica.crearPuzle()
        if not conf.COMENTARIOS:
            fabrica.dibujarTapiz(False)            
        print()
    else:
        p = Puzzle()
        p.creditos()
        p.mostrarAyuda()
