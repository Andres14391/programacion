import random as r

def nmayor(lista):
    if len(lista) == 1:
        return lista[0]
    num=nmayor(lista[1:])
    if lista[0] > num:
        return lista[0]
    else:
        return num



if __name__=="__main__":
    lista = r.sample(range(1,20),5)
    print(lista)

    mayor=nmayor(lista)
    print(f'El numero mayor de la lista es',mayor)