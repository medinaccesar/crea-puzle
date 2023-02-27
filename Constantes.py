import os

class Configuracion:

    __slots__ = ()
    NOMBRE_AP = 'Creador de un rompecabezas numérico.'
    VERSION = 1.0
    CREDITOS = 'César Medina'
    
    NUMERO_MAXIMO_FORMAS = 10

    # Estrategias de resolución:
    ESTRATEGIA_SECUENCIAL = 'Secuencial'

    # Tipo de estrategia de resolución utilizada
    ESTRATEGIA = ESTRATEGIA_SECUENCIAL

    # Los recursos están en la carpeta rec
    RECURSOS = 'rec'+os.path.sep
    
    # Se muestran los comentarios
    COMENTARIOS = False
