lista1 = []
lista2 = [1, 2, 3, 4, 5]
lista3 = [1, 2, 3, 4, 5]
lista4 = ["Mario", "pedro", "Dario"]
lista5 = [1, 3, 4.3, 2.3, "veronica"]
print(type(lista1))

print(lista2[3])
print(len(lista2))
print(lista2)
# cambio un elemnto asignando la pocision del elemento que quieres cambiar
lista2[2] = 7
print(lista2)

# agrega elementos a una lista
lista1.append(10)
lista1.append(1)
lista1.append(11)
print(lista1)

lista1.pop()
print(lista1)

print(lista2)
# ordena los elemtos de la lista
lista2.sort()
print(lista2)
