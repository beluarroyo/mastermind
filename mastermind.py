#!/usr/bin/env python3

"""
Este es módulo de nuestro jueguito Mastermind

"""


# agregar tu funcion acà
def ingresar_numero():
    pass


def crear_numero():
    pass


def evaluar(numero, numero_objetivo):
    plenos = 0
    parciales = 0
    intentos = 0
    cant_digitos = 4

    for i in range(cant_digitos):
        if numero[i] == numero_objetivo [i]:
            plenos = plenos + 1
        elif numero[i] in numero_objetivo:
            parciales = parciales + 1
    return (plenos, parciales)




def verificar(numero):
    pass


def reportar(numero, plenos, parciales):
    pass


def principal():
    pass


if __name__ == '__main__':
    principal()
