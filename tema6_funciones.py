import os


def funcion1():
    os.system('cls')
    print("Dame los numeros")
    num1 = int(input("Primer numero: "))
    num2 = int(input("Dame el segundo numero"))
    print("La suma de los dos numeros es: ", num1 + num2)


def funcion2():
    os.system('cls')
    num1 = int(input("Primer numero: "))
    num2 = int(input("Dame el segundo numero: "))
    print("La resta de los dos numeros es: ", num1 - num2)


def funcion3():
    os.system('cls')
    num1 = int(input("Primer numero: "))
    num2 = int(input("Dame el segundo numero: "))
    print("La multiplicacion de los dos numeros es: ", num1 * num2)


def funcion4():
    os.system('cls')
    num1 = int(input("Primer numero: "))
    num2 = int(input("Dame el segundo numero: "))
    print("La divicion de los dos numeros es: ", num1 / num2)


def run():
    os.system('cls')
    while True:

        print("Menu de opciones")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicar")
        print("4.- Dividir")
        print("5.- salir")

        opcion = int(input("Dame una opcion: "))
        if opcion == 1:
            funcion1()
        if opcion == 2:
            funcion2()
        if opcion == 3:
            funcion3()
        if opcion == 4:
            funcion4()
        if opcion == 5:
            print("Saliste de la aplicacion")
            break


# indica el comienzo de la app
if __name__ == "__main__":
    run()
