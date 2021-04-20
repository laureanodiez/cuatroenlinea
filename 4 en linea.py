from colorama import Fore
from colorama import Style
from os import system

def tableroVacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def soltarFichaEnColumna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
           tablero[fila - 1][columna - 1] = ficha
           return

def completarTableroEnOrden(secuencia, tablero):
    for indice, columna in enumerate(secuencia):
        fichaNumero = 1 + (indice%2)
        soltarFichaEnColumna(fichaNumero, columna, tablero)
    return tablero

def dibujarTablero(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == 0:
                print(f' {Fore.RED}0{Style.RESET_ALL} ', end='')
            else:
                if celda == 1:
                    print(f' {Fore.YELLOW}%s{Style.RESET_ALL} ' %celda, end='')
                else:
                    print(f' {Fore.BLUE}%s{Style.RESET_ALL} ' %celda, end='')
        print('')

def maxColumnas(secuencia):
    for columna in secuencia:
        if columna>7:
            print('La cantidad de columnas es 7. Ingrese una posición del 1 al 7.')
            return False
    return True


secuencia = [1, 2, 3, 1, 4]

if maxColumnas(secuencia):
    dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio()))
else:
    input('Presione cualquier tecla para continuar.')
    system('cls')