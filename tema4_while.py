x = input("Agrega un numero: ")


x = int(x)

resultado = 0


a = 0

while a <= 10:

    a = a + 1

    if a <= 10:
        resultado = x * a
        print("{} x {} = {}".format(x, a, resultado))
