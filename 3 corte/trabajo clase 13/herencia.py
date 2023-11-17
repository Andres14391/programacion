class Ciudadano():
    def __init__(self,nombre:str,edad:int):
        self.__nombre=nombre
        self.__edad=edad
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setEdad(self,edad:int):
        self.__edad=edad

    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def AñosProfecion(self):
        return f'{self.getNombre()} no tiene una profecion'

class Ingeniero(Ciudadano):
    def __init__(self, nombre:str,edad:int,carrera:str,lugargrado:str):
        super().__init__(nombre, edad)
        self.carrera=carrera
        self.lugargrado=lugargrado
    
    def setCarrera(self,carrera:str):
        self.carrera=carrera

    def setLugarDeGraduacion(self,lugargrado:str):
        self.lugargrado=lugargrado
    
    def getCarrera(self):
        return self.carrera

    def getLugarDeGraduacion(self):
        return self.lugargrado
    
    def proyectos(self):
        proyecto=input('ingrese el nombre del proyecto a realizar: ')
        return f'El ingeniero {self.getNombre()} acaba de concluir su proyecto de {proyecto}'
    
    def AñosProfesion(self):
        años=int(input(f'ingrese los años de experienca para el ingeniero {self.getNombre()}: '))
        return f'{self.getNombre()} tiene {self.getEdad()} años de edad,\nse graduo en la universidad de {self.getLugarDeGraduacion()},\nlleva {años} años ejerciendo su profecion.'

class Medico(Ciudadano):
    def __init__(self,nombre:str,edad:int,pacientes:int,especialista:str):
        super().__init__(nombre, edad)
        self.especialista=especialista
        self.pacientes=pacientes

    def setPacientes(self,pacientes:int):
        self.pacientes=pacientes

    def setespecialista(self,especialista:str):
        self.especialista=especialista
    
    
    def getPacientes(self):
        return self.pacientes

    def getEspecialista(self):
        return self.especialista
    
    def Curar(self):
        problema=input(f'ingrese un problema de salud a tratar segun la profesion de {self.getEspecialista()}: ')
        return f'{self.getNombre()} acaba de curar a una persona con {problema}'
    
    def AñosProfecion(self):
        años=int(input(f'ingrese los años de experienca para el medico {self.getNombre()}: '))
        return f'{self.getNombre()} tiene {self.getEdad()} años de edad,\ntiene titulo de {self.getEspecialista()},\nlleva {años} ejerciendo su profecion.'
        
class Artista(Ciudadano):
    def __init__(self,nombre:str,edad:int,estilodibujo:str,dibujos:int):
        super().__init__(nombre, edad)
        self.estilodibujo=estilodibujo
        self.dibujos=dibujos

    def setEstiloDibujo(self,estilodibujo:str):
        self.estilodibujo=estilodibujo

    def setDibujos(self,dibujos:int):
        self.dibujos=dibujos
    
    def getEstiloDibujo(self):
        return self.estilodibujo

    def getDibujos(self):
        return self.dibujos
    
    def Dibujar(self):
        dibujo=input('ingrese que va a dibujar: ')
        return f' {self.getNombre()} acaba de terminar su dibujo de: {dibujo}, utilizando {self.getEstiloDibujo()}'
    
    def AñosProfecion(self):
        años=int(input(f'ingrese los años de experienca para el artista {self.getNombre()}: '))
        return f'{self.getNombre()} tiene {self.getEdad()} años de edad,\nsu metodo de dibujo es: {self.getEstiloDibujo()},\nlleva {años} años ejerciendo su profecion.'

def main():

    ciudadano1=Ingeniero('Radamel Falcao García',35,'mecatronica','bogota')
    ciudadano2=Medico('Roger Federer',42,6,'medico general')
    ciudadano3=Ciudadano('Magnus Carlsen',32)
    ciudadano4=Artista('Mack',40,'cubismo',10)

    print(ciudadano2.AñosProfecion())
    print('------------------')
    print(ciudadano2.Curar())
    print('------------------')
    print(ciudadano1.AñosProfecion())
    print('------------------')
    print(ciudadano1.proyectos())
    print('------------------')
    print(ciudadano3.AñosProfecion())
    print('-------------------')
    print(ciudadano4.AñosProfecion())
    print('------------------')
    print(ciudadano4.Dibujar())

if __name__=="__main__":
    main()