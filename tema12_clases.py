class OperasBas:
    # declaracion de variables
    num1 = 0  # _ privado
    num2 = 0
    res = 0  # __ protegido

    # declaracion de contructor de la clase
    # metodo que permite la inicializacion de los metodos de la clase
    def __init__(self, a, b):  # this = self hace referencia a la propiedad de la clase
        self.num1 = a
        self.num2 = b

    # declaracion de metodos de la clase

    def suma(self):
        self.res = self.num1 + self.num2
        print("la suma es: {}".format(self.res))


def main():
    obj = OperasBas(3, 5)
    obj.suma()


if __name__ == "__main__":
    main()
