import random as r

def divisas(A):
    if A==1:
        D=int(input("cuantos COP desea cambiar: "))
        P=r.uniform(0.10, 0.50)
        V=D*P
        D=D-V
        D=D/4108
        R=D-float(D)
        C=D-int(D)
        C=C*4180

        print("tiene un cambio de:",round(D))
        print("hubo una comision de: ",round(P,2))
        print("tiene una devolucion de: ",round(C))
    elif A==2:
        D=int(input("cuantos COP desea cambiar: "))
        P=r.uniform(0.10, 0.50)
        V=D*P
        D=D-V
        D=D/4454
        R=D-float(D)
        C=D-int(D)
        C=C*4454

        print("tiene un cambio de:",round(D))
        print("hubo una comision de: ",round(P,2))
        print("tiene una devolucion de: ",round(C))
    elif A==3:
        D=int(input("cuantos COP desea cambiar: "))
        P=r.uniform(0.10, 0.50)
        V=D*P
        D=D-V
        D=D/563
        R=D-float(D)
        C=D-int(D)
        C=C*563

        print("tiene un cambio de:",round(D))
        print("hubo una comision de: ",round(P,2))
        print("tiene una devolucion de: ",round(C))
    elif A==4:
        D=int(input("cuantos COP desea cambiar: "))
        P=r.uniform(0.10, 0.50)
        V=D*P
        D=D-V
        D=D/28
        R=D-float(D)
        C=D-int(D)
        C=C*28

        print("tiene un cambio de:",round(D))
        print("hubo una comision de: ",round(P,2))
        print("tiene una devolucion de: ",round(C))
    elif A==5:
        D=int(input("cuantos COP desea cambiar: "))
        P=r.uniform(0.10, 0.50)
        V=D*P
        D=D-V
        D=D/1106
        R=D-float(D)
        C=D-int(D)
        C=C*1106

        print("tiene un cambio de:",round(D))
        print("hubo una comision de: ",round(P,2))
        print("tiene una devolucion de: ",round(C))
    

    else:
        print("seleccion invalida")

if __name__=='__main__':
    while True:
        print("*** Menu de Inicio***")
        print("seleccione que divisa quiere convertir: ")
        print("1.USD, la tasa es de: 4108")
        print("2.EUR, la tasa es de: 4454")
        print("3.CNY, la tasa es de: 563")
        print("4.JPY, la tasa es de: 28")
        print("3.PEN, la tasa es de: 1106")
        A=int(input("ingrese solo el numero de la opcion: "))
        divisas(A)

