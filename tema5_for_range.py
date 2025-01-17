#  nos permite generar una serie de numeros

x = range(10)

print(x)

print(list(x))
print(list(range(1, 10)))
print(list(range(1, 20, 2)))  # va del uno al 20 y hace iteraciones de 2

for i in range(10):
    print(i)

nombres = ["Mario", "juan", "Dario", "veronica"]

for nombre in nombres:
    print(nombre)
