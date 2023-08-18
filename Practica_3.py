
##PROBLEMA 1

try:

    X=int(input("Ingrese un numero entero: "))
    Y =int(input("Ingrese un numero entero: "))

    if 0< X/Y < 0.01:
        print("E")
    elif 1 > X/Y > 0.99:
        print("F")
    elif 0.01<= X/Y <= 0.99:
        print(X/Y*100,"%")
    else:
        print("Ingresa nuevamente el numero- El segundo numero debe ser igual o mayor al primero. ")
except ValueError:
    print("Ingresa nuevamente el numero. Solo numeros enteros: ")
except ZeroDivisionError:
    print("El segundo numero ingresado debe ser diferente de cero: ")

##PROBLEMA 2

def main():
    calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
    calificaciones_lista = calificaciones_str.split(',')

    calificaciones_enteros = []

    for calificacion in calificaciones_lista:
        try:
            calificacion_entero = int(calificacion.strip())
            calificaciones_enteros.append(calificacion_entero)
        except ValueError:
            print(f"Error: '{calificacion.strip()}' no es una calificación válida.")

    print("Calificaciones enteras:", calificaciones_enteros)

if __name__ == "__main__":
    main()

##PROBLEMA 3

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

def main():
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = Circulo(radio)
    area = circulo.calcular_area()
    print(f"El área del círculo con radio {radio} es: {area}")

if __name__ == "__main__":
    main()

##PROBLEMA 4

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

def main():
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    
    rectangulo = Rectangulo(largo, ancho)
    area = rectangulo.calcular_area()
    
    print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area}")

if __name__ == "__main__":
    main()

##PROBLEMA 5
class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.notas = []

    def display(self): 
        print("Nombre:", self.nombre)
        print("Número de Registro:", self.registro)

    def setAge(self, edad):
        self.edad = edad
        print("Edad:", self.edad)

    def setNota(self, *notas):
        self.notas.extend(notas)
        print("Notas:", self.notas)

def main():
    nombre = input("Ingrese el nombre del estudiante: ")
    registro = input("Ingrese el número de registro del estudiante: ")
    
    alumno = Alumno(nombre, registro)

    edad = int(input("Ingrese la edad del estudiante: "))
    alumno.setAge(edad)

    notas = input("Ingrese las notas del estudiante separadas por comas: ").split(',')
    notas = [float(nota.strip()) for nota in notas]
    alumno.setNota(*notas)

    alumno.display()
    alumno.setAge(edad)
    alumno.setNota(*notas)

if __name__ == "__main__":
    main()

##PROBLEMA 6:

import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "Sobre el origen"

    def vector(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return Punto(dx, dy)

    def distancia(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia

def main():
    x1 = float(input("Ingrese la coordenada X del primer punto: "))
    y1 = float(input("Ingrese la coordenada Y del primer punto: "))
    punto1 = Punto(x1, y1)

    x2 = float(input("Ingrese la coordenada X del segundo punto: "))
    y2 = float(input("Ingrese la coordenada Y del segundo punto: "))
    punto2 = Punto(x2, y2)

    print("Punto 1:", punto1)
    print("Punto 2:", punto2)

    print("Cuadrante del Punto 1:", punto1.cuadrante())
    print("Cuadrante del Punto 2:", punto2.cuadrante())

    vector_resultante = punto1.vector(punto2)
    print("Vector resultante:", vector_resultante)

    distancia_entre_puntos = punto1.distancia(punto2)
    print(f"Distancia entre los puntos: {distancia_entre_puntos:.2f}")

if __name__ == "__main__":
    main()

##Problema 7:

from modulopreg7 import generar_numeros_aleatorios
generar_numeros_aleatorios

##PROBLEMA 8:

from modulopreg8 import suma,resta,producto,division
try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        
        print("Resultado de la suma:", suma(a, b))
        print("Resultado de la resta:", resta(a, b))
        print("Resultado del producto:", producto(a, b))
        print("Resultado de la división:", division(a, b))
except ValueError:
        print("Error: Ingrese números válidos.")