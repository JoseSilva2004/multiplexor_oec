##Simulador de un multiplexor simple con las funciones OR, AND, XOR, y NOT
import os;

def funcion_OR():   ##Funcion OR: Para que su salida sea verdadera(1) por lo menos una de sus entradas deben serla
    suma = int
    print("*****OR*****")
    a = int(input("Ingrese el valor de A: "))
    b = int(input("Ingrese el valor de B: "))

    if (a == 0 and b == 1 or b == 0 and a == 1 or a == 0 and b == 0):
        suma = a + b
        print("Salida OR: ", suma)
    else:
        if (a == 1 and b == 1):
            suma = 1
            print("Salida OR: ",suma)
        else:
            print("Error, el rango de numeros debe ser binario (0 o 1)")


def funcion_AND():  ##Funcion AND: Para que su salida sea verdadera(1) todas sus entradas deben serla
    multiplicacion = int
    print("*****AND*****")
    a = int(input("Ingrese el valor de A: "))
    b = int(input("Ingrese el valor de B: "))

    if (a >= 0 and a <=1 and b >=0 and b <= 1):
        multiplicacion = a * b
        print("Salida AND: ", multiplicacion)
    else:
        print("Error, el rango de numeros debe ser binario (0 o 1)")

def funcion_XOR():  ##Funcion XOR: Para que su salida sea verdadera(1) por lo menos una de sus entradas deben serla, en caso contrario (0) las entradas deben ser iguales
    suma = int
    print("*****XOR*****")
    a = int(input("Ingrese el valor de A: "))
    b = int(input("Ingrese el valor de B: "))

    if (a == 0 and b == 1 or b == 0 and a == 1):
        suma = a + b
        print("Salida XOR: ", suma)
    else:
        if (a == 1 and b == 1 or a == 0 and b == 0):
            suma = 0
            print("Salida XOR: ", suma)
        else:
            print("Error, el rango de numeros debe de ser binario (0 o 1)")

def funcion_NOT():  ##Funcion NOT: La salida será la inversa de los valores de entrada
    print("*****NOT*****")
    a = int(input("Ingrese el valor de A: "))

    if (a == 0 ):
        a = 1
        print("Salida NOT: ", "A:", a)
    else:
        if(a == 1):
            a = 0
            print("Salida NOT: ", "A:", a)
        else:
            print("Error, el rango debe estar en valores binario (0 o 1)")


##Funcion Principal
def main():
    opc = str

    ##S1(Selector 1), S2(Selector2)
    s1 = int
    s2 = int

    while(opc != 'S'):
        os.system("pause")
        os.system("cls")
        print("************MULTIPLEXOR SIMPLE**************")
        print("S1 = 0, S2 = 0 ---> Funcion OR")
        print("S1 = 0, S2 = 1 ---> Funcion XOR")
        print("S1 = 1, S2 = 0 ---> Funcion AND")
        print("S1 = 1, S2 = 1 ---> Funcion NOT")
        print("\n")
        s1 = int(input("Ingrese el valor de S1(Selector 1): "))
        s2 = int(input("Ingrese el valor de S2(Selector 2): "))

        if (s1 == 0 and s2 == 0):
            print("\n")
            funcion_OR()
        else:
            if (s1 == 0 and s2 == 1):
                print("\n")
                funcion_XOR()
            else:
                if (s1 == 1 and s2 == 0):
                    print("\n")
                    funcion_AND()
                else:
                    if (s1 == 1 and s2 == 1):
                        print("\n")
                        funcion_NOT()
                    else:
                        print("\n")
                        print("Error, debes de ingresar valores binarios(0 o 1)")
                        opc = str(input("¿Desea Salir del Programa?(S/N): "))
main()
    