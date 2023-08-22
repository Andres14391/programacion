while True:
    print("*** Menu de Inicio***")
    print("1.vocales y consonantes")
    print("2.ticked de parking")
    print("3.identificador de triangulos \n")
    A=input("ingrese una opcion: ")
    if A =="1" or A=="vocales y consonantes":
        q=input("\ningrese una letra ")
        if (q=="a") or (q=="e") or (q=="i") or (q=="o") or (q=="u"):
            print("la letra -",q,"- es una vocal \n")
        else:
            if q in ("qwrtypsdfghjklñzxcvbnm"):
                print("la letra -",q,"- es una consonante \n")
            else:
                print("el valor ingresado no es una letra \n")
                
    elif A=="2" or A=="ticked de parking":
             T=int(input("\n ingrese el tiempo demorado: "))
             PT=T*139
             VI=PT*0.19
             CT=((PT+49)//50)*50
             R=CT-PT
             print("el precio por minuto con el iva incluido es de: 139 pesos\n"
             "por los",T,"minutos demorados el precio es de:",PT,"pesos""\n"
             "donde el iva del precio es de",VI,"pesos""\n"
             "y el precio total es de:",CT,"pesos""\n"
             "el redondeo es de:",R,"pesos \n")
    elif A=="3" or A=="identificador de triangulos":
        a=int(input("\n ingrese el valor del lado a: "))
        b=int(input("ingrese el valor del lado b: "))
        c=int(input("ingrese el valor del lado c: "))
        if (a==b)&(a==c)or(b==a)&(b==c)or(c==a)&(c==b):
            print("es un triangulo equilatero \n")
        elif(a==b)&(b==a)&(c!=a)&(c!=b)or(c==a)&(a==c)&(b!=a)&(b!=c)or(b==c)&(c==b)&(a!=c)&(a!=b):
            print("es un triangulo isosceles \n")
        elif(a!=b)&(a!=c)or(b!=a)&(b!=c)or(c!=a)&(c!=b):
            print("es in triangulo escaleno \n")