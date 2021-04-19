def tableroVacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def completarTableroEnOrden(secuencia, tablero):
    for indice, columna in enumerate(secuencia):
        fichaNumero = 1 + (indice%2)
        soltarFichaEnColumna(fichaNumero, columna, tablero)
    return tablero

def soltarFichaEnColumna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] == ficha

def dibujarTablero(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == 0:
                print('   ', end='')
            else:
                print(' %s ' %celda, end='')
        print('')

secuencia = [1, 2, 3, 1]
dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio()))