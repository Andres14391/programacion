class Ciudadano:
    def __init__(self):
        self.__nombre=None
        self.__edad=0
        self.__cedula=None

    def setNombre(self,nombre:str):
        self.__nombre=nombre
        
    def getNombre(self):
        return self.__nombre

    def setEdad(self,edad:int):
        if edad< 0:
            print("Edad incorrecta, ingrese un numero positivo")
        else:
            self.__edad=edad

        
    def getEdad(self):
        return self.__edad
    
    def setCedula(self,cedula:int):
        self.__cedula=cedula
    
    def getCedula(self):
        return self.__cedula
    
   


def main():
    ciudadano=[]
    opc='n'
    while 1:
        est=Ciudadano()
        est.setNombre(input('Ingrese su Nombre: '))
        cedula1=input("ingrese su Cedula: ")
        if len(cedula1)>=8 and len(cedula1)<=10:
            est.setCedula(cedula1)
    
        else:
            print("el numero de identificacion no es valida")
        
        est.setEdad(int(input("ingrese su Edad: ")))
        edadobtenida=est.getEdad()
        

        ciudadano.append(est)
        opc=input('Desea salir? (y/n)')
        if opc=='y':
            break
        else:
            print('Invalido')
    
    print(f'-------Clase 2023-II -----\n')
    for i in ciudadano:
        print(f'\n\
        Nombre: {i.getNombre()}\n\
        cedula: {i.getCedula()}\n\
        Edad: {i.getEdad()}\n')
    if edadobtenida <18:
        print("Es menor de Edad")
    else:
        print("Es mayor de Edad")
        
if __name__=="__main__":
    main()