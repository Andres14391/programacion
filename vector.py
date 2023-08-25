import math

def calcular_modulo_vector(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    modulo = math.sqrt(dx**2 + dy**2)
    
    return modulo, dx, dy

x1 = float(input("Ingrese la coordenada x del punto de origen: "))
y1 = float(input("Ingrese la coordenada y del punto de origen: "))
x2 = float(input("Ingrese la coordenada x del punto final: "))
y2 = float(input("Ingrese la coordenada y del punto final: "))

modulo, dx, dy = calcular_modulo_vector(x1, y1, x2, y2)

print("El módulo del vector es:", modulo)
print("Las componentes rectangulares del vector son:")
print("Componente en x:", dx)
print("Componente en y:", dy)