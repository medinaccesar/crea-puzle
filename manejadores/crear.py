import random
from datetime import datetime
from Constantes import Configuracion as conf
from manejadores.motores.MotorSecuencial import MotorSecuencial


class Fabrica():

    def __init__(self, dimension):
        self._dimension = dimension
        self._tapiz = []
        self._piezas = []
        self._numeros = []
        self._nUmMaxFormas = conf.NUMERO_MAXIMO_FORMAS
        self._pm = MotorSecuencial()

    def _crearNumeros(self):
        dim = self._dimension
        long = dim * dim
        # Consigue una lista de números entre 1 y long incluido.
        self._numeros = list(range(1, long + 1))
        # Desordena los números
        self._numeros = random.sample(self._numeros, long)
        if conf.COMENTARIOS:
            print('Números', self._numeros)

    def crearPuzle(self):
        # Se crean los números según las dimensiones (dim*dim) y se desordenan
        self._crearNumeros()
        # Rellenar tapiz
        self._rellenarTapiz()
        if conf.COMENTARIOS: self.dibujarTapiz()
        # Marca temporal
        fecha = datetime.now()
        # Guardar archivo solución
        self._guardarArchivoSolucion(fecha)
        # Desordenar piezas
        self._desordenarPiezas()
        # Guardar archivo fuente
        self._guardarArchivoFuente(fecha)

    def _guardarArchivoSolucion(self, fecha):
        dim = str(self._dimension)
        nombreFichero = str("{}.txt".format(fecha.strftime("%Y%m%d_%H%M%S")))
        ruta = conf.RECURSOS+'s_'+dim+'x'+dim+'_'+nombreFichero
        if conf.COMENTARIOS:
            print('\nArchivo solución',ruta)
        with open(ruta, "w") as file:
            for i in range(0, self._dimension):
                # Se convierte lista de enteros a cadena
                file.write(' '.join(str(x) for x in self._tapiz[i])+'\n')

    def _guardarArchivoFuente(self, fecha):
        dim = str(self._dimension)
        nombreFichero = str("{}.txt".format(fecha.strftime("%Y%m%d_%H%M%S")))
        ruta = conf.RECURSOS+'f_'+dim+'x'+dim+'_'+nombreFichero
        if conf.COMENTARIOS:            
            print('\nArchivo fuente',ruta)
        with open(ruta, "w") as file:
            for i in range(0, len(self._piezas)):
                if i == 0:
                    file.write(dim+' '+dim+'\n')
                indice = self._getIndicePiezaTapiz(i+1)
                # Se convierte lista de enteros a cadena
                file.write(' '.join(str(x) for x in self._piezas[indice])+'\n')

    def _rellenarTapiz(self):
        dim = self._dimension
        self._pm.dimensiones = [dim, dim]
        for i in range(0, dim):
            fila = []
            for j in range(0, dim):
                p = self._crearPieza(i, j)
                fila.append(self._numeros.pop(0))

                self._piezas.append(p)

            self._tapiz.append(fila)

    def _desordenarPiezas(self):
        piezas = []
        for i in range(0, len(self._piezas)):
            piezas.append(self._pm.girarPieza(self._piezas[i]))
        self._piezas = piezas

    def _crearPieza(self, x, y):
        pieza = []
        izda, encima = self._getFormasDondeEncajar(x, y)
        if self._pm.esEsquinaSuperiorIzda(x, y):

            pieza = [0, 0, random.randint(
                1, self._nUmMaxFormas+1), random.randint(1, self._nUmMaxFormas+1)]

        elif self._pm.esEsquinaSuperiorDcha(x, y):

            pieza = [izda, 0, 0, self._nUmMaxFormas+1]

        elif self._pm.esEsquinaInferiorIzda(x, y):

            pieza = [0, encima, random.randint(1, self._nUmMaxFormas+1), 0]

        elif self._pm.esEsquinaInferiorDcha(x, y):

            pieza = [izda, encima, 0, 0]

        elif self._pm.esMarcoSuperior(x):

            pieza = [izda, 0, random.randint(
                1, self._nUmMaxFormas+1), random.randint(1, self._nUmMaxFormas+1)]

        elif self._pm.esMarcoIzquierdo(y):
            pieza = [0, encima, random.randint(
                1, self._nUmMaxFormas+1), random.randint(1, self._nUmMaxFormas+1)]

        elif self._pm.esMarcoDerecho(y):
            pieza = [izda, encima, 0, random.randint(1, self._nUmMaxFormas+1)]
        elif self._pm.esMarcoInferior(x):
            pieza = [izda, encima, random.randint(1, self._nUmMaxFormas+1), 0]
        else:
            pieza = [izda, encima, random.randint(
                1, self._nUmMaxFormas+1), random.randint(1, self._nUmMaxFormas+1)]

        return pieza

    def _getFormasDondeEncajar(self, x, y):

        if x == 0:
            encima = 0
        else:
            xAux = x-1
            indice = self._getIndicePieza(xAux, y)
            encima = self._piezas[indice][3]
        if y == 0:
            izda = 0
        else:
            yAux = y-1
            indice = self._getIndicePieza(x, yAux)
            izda = self._piezas[indice][2]

        return izda, encima

    def _getIndicePieza(self, x, y):

        dim = self._dimension
        indice = x * dim + y
        return indice

    def _getIndicePiezaTapiz(self, valor):

        for x, e in enumerate(self._tapiz):
            try:
                y = e.index(valor)
                indice = self._getIndicePieza(x, y)
                return indice
            except ValueError:
                pass
        raise ValueError("{!r} no está en el tapiz".format(valor))

    def _desordenarPieza(self, pieza):

        nVeces = random.randint(0, 3)
        for i in range(0, nVeces):
            pieza = self._pm.girarPieza(pieza)

        return pieza

    def dibujarTapiz(self, dibujarPiezas = True):
        dim = self._dimension
        
        if conf.COMENTARIOS:
            print()
            print('Piezas:', self._piezas)
            print('Tapiz:', self._tapiz)
        print()
        for i in range(0, dim):
            fila = ''
            for j in range(0, dim):
                fila = fila + ' ' + str(f"{self._tapiz[i][j]:02d}")
            print(fila)
        if dibujarPiezas:
            indice = 0
            for i in range(0, dim):
                fila = []
                for j in range(0, dim):
                    p = self._piezas[indice]
                    fila.append(p)
                    indice += 1
                print(fila)
