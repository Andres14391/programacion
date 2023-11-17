def lectura():
    f=open('wcm.csv','r',encoding="utf8")
    line=f.readlines()
    mundial=[]
    primeralinea=True

    for i in line:
        if primeralinea:
            primeralinea=False
            continue
        datos=i.rstrip('\n').split(',')

    
        LOCAL=datos[0]
        VISIT=datos[1]
        GOLOCAL=int(datos[2])
        PENALOCAL=datos[3]
        GOLVISIT=int(datos[4])
        PENALVISIT=datos[5]
        MANAGERLOCAL=datos[6]
        CAPTAINLOCAL=datos[7]
        MANAGERVISIT=datos[8]
        CAPTAINVISIT=datos[9]
        PUBLIC=datos[10]
        STADIUM=datos[11]
        ROUND=datos[12]
        DATE=datos[13]
        ARBITRO =datos[14]
        HOST=datos[15]
        YEAR=datos[16]
        mundial.append({
            'local': LOCAL,
            'visitante':VISIT,
            'goles local':GOLOCAL,
            'goles visitante':GOLVISIT,
            'penales local':PENALOCAL,
            'penales visitante': PENALVISIT,
            'manager local':MANAGERLOCAL,
            'capitan del equipo local':CAPTAINLOCAL,
            'manager visitante':MANAGERVISIT,
            'capitan equipo visitante': CAPTAINVISIT,
            'publico': PUBLIC,
            'estadio':STADIUM,
            'ronda':ROUND,
            'fecha':DATE,
            'arbitro':ARBITRO,
            'patrocinador':HOST,
            'año':YEAR
        })
    return mundial

def goleadas():
    mundial=lectura()
    goleadas=[]
    while True:
        print('seleccione algunas de las opciones')
        print('1.listado general')
        print('2.busqueda por año')
        print('3.salir')
        respuesta=int(input('ingrese la opcion: '))
        if respuesta==1:
            for partidos in mundial:
                resultado1=partidos['goles local']-partidos['goles visitante']
                resultado2=partidos['goles visitante']-partidos['goles local']
                if resultado1 <4:
                    pass
                elif resultado1 >=4:
                    goleadas.append({
                        'local':partidos['local'],
                        'visitante':partidos['visitante'],
                        'goles local':partidos['goles local'],
                        'goles visitante':partidos['goles visitante'],
                        'ronda':partidos['ronda']
                    })
                    print(f'por {resultado1} goles: {partidos["local"]} | {partidos["goles local"]} vs {partidos["goles visitante"]} | {partidos["visitante"]} ({partidos["ronda"]})')
                    
              
                    
                else:
                    if resultado2 <4:
                        pass
                    elif resultado2 >=4:
                        goleadas.append({
                        'local':partidos['local'],
                        'visitante':partidos['visitante'],
                        'goles local':partidos['goles local'],
                        'goles visitante':partidos['goles visitante'],
                        'ronda':partidos['ronda']
                    })
                    print(f'por {resultado1} goles: {partidos["local"]} | {partidos["goles local"]} vs {partidos["goles visitante"]} | {partidos["visitante"]} ({partidos["ronda"]})')

        elif respuesta ==2:
            respuesta=int(input('Ingrese el año que quiere buscar: '))     
            for partidos in mundial:
                resultado1=partidos['goles local']-partidos['goles visitante']
                resultado2=partidos['goles visitante']-partidos['goles local']
                if resultado1 <4:
                    pass
                elif (resultado1 >=4 or resultado2>=4) and int(partidos['año'])==respuesta:
                    goleadas.append({
                        'local':partidos['local'],
                        'visitante':partidos['visitante'],
                        'goles local':partidos['goles local'],
                        'goles visitante':partidos['goles visitante'],
                        'ronda':partidos['ronda'],
                    })
                    print(f'por {max(resultado1,resultado2)} goles: {partidos["local"]} | {partidos["goles local"]} vs {partidos["goles visitante"]} | {partidos["visitante"]} ({partidos["ronda"]})')
        else:
            break           

def enfrentamientos():
    mundiales = lectura()  
    eq1 = input("digite el nombre del primer equipo: ")
    eq2 = input("digite el nombre del segundo equipo: ")
    
    contador = 0
    enfrentamientos= []
    
    for mundial in mundiales:
        if (mundial['local'] == eq1 and mundial['visitante'] == eq2) or \
            (mundial['local'] == eq2 and mundial['visitante'] == eq1):
            contador += 1
            enfrentamientos.append({
                'año': mundial['año'],
                'resultado': f"{mundial['goles local']} - {mundial['goles visitante']}"
                
            })
    
    if enfrentamientos == 0:
        print(f"no hay enfrentamientos entre {eq1} y {eq2}.")
    else:
        
        print(f"{eq1} y {eq2} se han enfrentado {contador} veces :")
        for partidos in enfrentamientos:
            print(f"año: {partidos['año']}, resultado: {partidos['resultado']}")
            print('--------------------------------------------')

def main():
   
    while True:
        print('ingrese una de las opciones')
        print('1.goleadas mundiales')
        print('2.cantidad de veces que 2 paises se enfrentaron')
        print('3.salir')
        resultado=int(input('ingrese una opcion: '))
        if resultado ==1:
          goleadas()
        elif resultado == 2:
          enfrentamientos()
        elif resultado == 3:
            break
        else:
            print('opcion invalida ingrese una opcion valida')
if __name__ == '__main__':
    main()