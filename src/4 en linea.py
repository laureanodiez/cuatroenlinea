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


def contenidoColumna(nro_columna, tablero):
    columna=[]
    for fila in tablero:
        celda = fila[nro_columna-1]
        columna.append(celda)
    return columna

def contenidoFila(nro_fila, tablero):
    fila=[]
    for columna in tablero:
        celda = columna[nro_fila-1]
        fila.append(celda)
    return fila

def todoContenido(opcion, tablero):
    contador=0
    if opcion == 1:
        fila=[]
        for columna in tablero:
            for celda in columna:
                contador=columna[celda]
                fila.append(contador)
        return fila
    else:
        if opcion == 2:
            columna=[]
            for fila in tablero:
                for celda in fila:
                    contador=fila[celda]
                    columna.append(contador)
            return columna
        else:
            print("El valor elegido no es válido. Por favor elija el valor correspondiente: ")
            contador=9
            return contador


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
    print(f' {Fore.GREEN}+-- -- -- -- -- -- -- --+{Style.RESET_ALL} ', end='')
    print('')
    for fila in tablero:
        print(f' {Fore.GREEN}|{Style.RESET_ALL} ', end='')
        for celda in fila:
            if celda == 0:
                print(f' {Fore.RED}0{Style.RESET_ALL} ', end='')
            else:
                if celda == 1:
                    print(f' {Fore.YELLOW}%s{Style.RESET_ALL} ' %celda, end='')
                else:
                    print(f' {Fore.BLUE}%s{Style.RESET_ALL} ' %celda, end='')
        print(f' {Fore.GREEN}|{Style.RESET_ALL} ', end='')
        print('')
    print(f' {Fore.GREEN}+-----------------------+{Style.RESET_ALL} ', end='')
    print('')


def maxColumnas(secuencia):
    for columna in secuencia:
        if columna>7:
            print('La cantidad de columnas es 7. Ingrese una posición del 1 al 7.')
            return False
    return True


secuencia = [1, 2, 3, 1, 4, 6, 9]
tablero = []



print("Presione (1) si desea mostrar el tablero completo, (2) si desea mostrar SOLO las columnas y (3) si desea mostrar SOLO las filas: ", end='')
opcion=input()
if opcion == 1:
    if maxColumnas(secuencia):
        tablero = dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio()))
    else:
        input('Presione cualquier tecla para continuar.')
        system('cls')
else:
    print(todoContenido(opcion, completarTableroEnOrden(secuencia, tableroVacio())))

'''print(contenidoColumna(1, tablero))
print(contenidoFila(1, tablero))'''

