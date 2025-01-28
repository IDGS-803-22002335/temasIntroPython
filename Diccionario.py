from io import open


class Diccionario:
    palabraEs = ""
    PalabraIn = ""
    idioma = ""

    def __init__(self, español, ingles, idioma):
        self.palabraEs = español
        self.PalabraIn = ingles
        self.idioma = idioma

    def opcion1(self):

        archivo = open("diccionario.txt", "a")

        archivo.write("\n" + self.palabraEs)
        archivo.write(":")
        archivo.write(self.PalabraIn)
        archivo.close()

    def opcion2(self):
        archivo = open("diccionario.txt", "r")
        texto = []
        texto = archivo.readlines()

        if self.idioma == 1:
            palabras = input(
                "Ingrese la palabra a buscar en Español: ").lower()
            for linea in texto:
                partes = linea.strip().split(":")
                if len(partes) == 2:
                    palabra_es, palabra_in = partes
                    if palabras == palabra_es.strip():
                        print(f"La palabra en inglés es: {palabra_in.strip()}")
                        break
            else:
                print(f"No se encontró la palabra '{palabras}' en español.")

        if self.idioma == 2:
            palabras = input("Ingrese la palabra a buscar en Inglés: ").lower()
            for linea in texto:
                partes = linea.strip().split(":")
                if len(partes) == 2:
                    palabra_es, palabra_in = partes
                if palabras == palabra_in.strip():  # Comparar con la palabra en inglés
                    print(f"La palabra en español es: {palabra_es.strip()}")
                    break
            else:
                print(f"No se encontró la palabra '{palabras}' en inglés.")

        archivo.close()


def main():
    while True:
        print("1.- Capturar palabra")
        print("2.- Buscar palabra")
        opcion = input("Ingresa una opcion: ")
        opcion = int(opcion)
        if opcion == 1:
            palabraEs = input("Ingresa la palabra en español: ").lower()
            palabraIn = input("Ingresa la palabra en Ingles: ").lower()

            obj = Diccionario(palabraEs, palabraIn, "")
            obj.opcion1()
        if opcion == 2:
            print("Buscar:")
            print("1.- Español")
            print("2.- Engles")
            idioma = int(input("Ingresa Idioma: "))

            obj = Diccionario("", "", idioma)
            obj.opcion2()


if __name__ == "__main__":
    main()
