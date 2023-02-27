# crea-puzle
Crea el archivo fuente y una posible solución para un rompecabezas numérico.

Las piezas del rompecabezas tienen cuatro lados, son las formas del mismo y están representadas por un número entero positivo. Las formas con igual número encajan entre ellas. Una pieza puede rotarse para encajar, pero no voltearse, las piezas tienen una cara válida. El número cero representa el borde del rompecabezas. Una pieza podría ser 0 2 8 4. El primer número es el lado izquierdo, el segundo es el lado de arriba, el tercero es el lado derecho y por último el cuarto es el lado de abajo.                                      
                                       
Por ejemplo la pieza 0 2 8 4  sería 
```
  2  
0 ◻ 8
  4
 ```   

El archivo fuente del rompecabezas es un archivo de texto. La primera línea del archivo representa la altura y la anchura del rompecabezas, el resto de líneas son las piezas del mismo. La altura y la anchura así como cada forma del piezal están separadas por un espacio, es decir el archivo fuente de un rompezabezas de 4 por 4 debería tener este formato:
```
4 4
1 1 3 2
0 4 1 5
10 11 0 8
6 8 0 0
10 7 10 1
11 0 0 1
0 0 11 5
11 0 11 7
11 0 11 4
0 5 10 4
0 5 6 0
5 7 6 0
10 4 10 4
3 4 10 7
10 1 0 11
6 2 5 0
```
La primera pieza es la múmero 1, el resto según corresponda secuencialmente.

El archivo solución usa los números de las piezas para representar el rompecabezas completado, por ejemplo:
```
11 02 10 07
16 01 05 08
12 14 13 09
04 03 15 06
```

Un rompecabezas puede tener más de una solución, no se consideran soluciones la rotación del mismo 90º o 180º o bien 270º.


