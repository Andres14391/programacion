def app():
    while True:
        print("*** Menu de Inicio***")
        print('1.divisores positivos')
        print('2.suma sucesiva')
        print('3.suma de fibonacci')
        A=input('ingrese una opcion: ')

        if A=='1' or A=='divisores positivos':
            numero=int(input("Ingrese un número: "))

            if numero == 0:
                print("Ningún número es divisible entre cero")
            else:
                print(f"Los divisores positivos de {numero} son:")
                for i in range(1, abs(numero) + 1):
                    if numero % i == 0:
                        print(i)
        elif A=='2' or A=='suma sucesiva':
                def sumas(num1, num2):
                    producto = 0
    
                    if num1 < 0 and num2 < 0:
                        num1 = abs(num1)
                        num2 = abs(num2)
    
                    for _ in range(num2):
                        producto += num1
    
                    if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
                        producto = -producto
    
                    return producto

                numero1 = int(input("Ingrese el primer número: "))
                numero2 = int(input("Ingrese el segundo número: "))

                resultado = sumas(numero1, numero2)
                print(f"El producto de {numero1} y {numero2} es: {resultado}")
        elif A=='3' or A=='suma de fibonacci':
            def fibonacci_digitos(cantidad_digitos):
                fib_sequence = [0, 1]
    
                while len(str(fib_sequence[-1])) < cantidad_digitos:
                    next_fib = fib_sequence[-1] + fib_sequence[-2]
                    fib_sequence.append(next_fib)
    
                return fib_sequence

            digitos = int(input("Ingrese la cantidad de dígitos para la serie de Fibonacci: "))
            fib_series = fibonacci_digitos(digitos)

            print(f"Serie de Fibonacci con al menos {digitos} dígitos:")
            for num in fib_series:
                print(num)


if __name__ == '__main__':
    app()