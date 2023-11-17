#indice de masa corporal

class Estudiante:
    def __init__(self):
        self.nombre=None
        self.peso=None
        self.altura=None
        self.IMC=None
        self.salud=None

def main():
    paciente=[]
    
    per1=Estudiante()
    per1.nombre='Pedro Caceres'
    per1.peso=97
    per1.altura=float(188/100)
    IMC1=float(per1.peso)/(per1.altura)**2
    if IMC1 < 18.5:
        per1.salud='Su peso esta por debajo'
    elif IMC1 >= 18.5 and IMC1 <= 24.9:
        per1.salud='Su peso es saludable'
    elif IMC1 >=25 and IMC1 <= 29.9:
         per1.salud='Tiene sobrepeso'
    elif IMC1 >=30 and IMC1 <= 34.9:
         per1.salud='Tiene Obesidad I'
    elif IMC1 >=35 and IMC1 <= 39.9:
         per1.salud='Tiene Obesidad II'
    else:
        per1.salud='Tiene Obesidad III'
    per1.IMC=round(IMC1,2)
    paciente.append(per1)


    per2=Estudiante()
    per2.nombre='Maria Perez'
    per2.peso=47
    per2.altura=float(160/100)
    IMC2=float(per2.peso)/(per2.altura)**2
    if IMC2 < 18.5:
        per2.salud='Su peso esta por debajo'
    elif IMC2 >= 18.5 and IMC2 <= 24.9:
        per2.salud='Su peso es saludable'
    elif IMC2 >=25 and IMC2 <= 29.9:
         per2.salud='Tiene sobrepeso'
    elif IMC2 >=30 and IMC2 <= 34.9:
         per2.salud='Tiene Obesidad I'
    elif IMC2 >=35 and IMC2 <= 39.9:
         per2.salud='Tiene Obesidad II'
    else:
        per2.salud='Tiene Obesidad III'
    per2.IMC=round(IMC2,2)
    paciente.append(per2)

    per3=Estudiante()
    per3.nombre='Julian Dominguez'
    per3.peso=58
    per3.altura=float(158/100)
    IMC3=float(per3.peso)/(per3.altura)**2
    if IMC3 < 18.5:
        per3.salud='Su peso esta por debajo'
    elif IMC3 >= 18.5 and IMC3 <= 24.9:
        per3.salud='Su peso es saludable'
    elif IMC3 >=25 and IMC3 <= 29.9:
         per3.salud='Tiene sobrepeso'
    elif IMC3 >=30 and IMC3 <= 34.9:
         per3.salud='Tiene Obesidad I'
    elif IMC3 >=35 and IMC3 <= 39.9:
         per3.salud='Tiene Obesidad II'
    else:
        per3.salud='Tiene Obesidad III'
    per3.IMC=round(IMC3,2)
    paciente.append(per3)

    per4=Estudiante()
    per4.nombre='Jessica Fuentes'
    per4.peso=73
    per4.altura=float(170/100)
    IMC4=float(per4.peso)/(per4.altura)**2
    if IMC4 < 18.5:
        per4.salud='Su peso esta por debajo'
    elif IMC4 >= 18.5 and IMC4 <= 24.9:
        per4.salud='Su peso es saludable'
    elif IMC4 >=25 and IMC4 <= 29.9:
         per4.salud='Tiene sobrepeso'
    elif IMC4 >=30 and IMC4 <= 34.9:
         per4.salud='Tiene Obesidad I'
    elif IMC4 >=35 and IMC4 <= 39.9:
         per4.salud='Tiene Obesidad II'
    else:
        per3.salud='Tiene Obesidad III'
    per4.IMC=round(IMC4,2)
    paciente.append(per4)

    


       

    print(f'-------Indice de Masa Corporal -----\n')
    for i in paciente:
        print(f'Nombre: {i.nombre} \n\
        Peso:{i.peso}\n\
        Altura: {i.altura}\n\
        IMC: {i.IMC}\n\
        {i.salud} \n')
        
if __name__=="__main__":
    main()