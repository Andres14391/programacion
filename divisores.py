def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def numero_perfecto(numero):
    divisores = calcular_divisores(numero)
    suma_divisores = sum(divisores)
    return suma_divisores == numero

cantidad_perfectos_solicitados = int(input("Ingrese la cantidad de números perfectos que desea encontrar (hasta 10): "))
cantidad_encontrados = 0
numero_actual = 2

print(f"Los primeros {cantidad_perfectos_solicitados} números perfectos son:")

while cantidad_encontrados < cantidad_perfectos_solicitados and numero_actual < 10000:
    if numero_perfecto(numero_actual):
        print(numero_actual)
        cantidad_encontrados += 1
    numero_actual += 1

if cantidad_encontrados < cantidad_perfectos_solicitados:
    print("No se pudieron encontrar más números perfectos.")
