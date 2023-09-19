import random as r


    

def nmayor(matriz):
    nmayor=matriz[0] [0]
    for i in matriz:
        for num in i:
            if num > nmayor:
                nmayor=num

    for j in range(len(matriz)):
        if nmayor in matriz[j] :
            print('---------------------')
            print('el numero mas alto de la matriz es:',nmayor)
            print(f'columna: {matriz[j].index(nmayor)}')
            print(f'fila: {j}')
    

           
def nmenor(matriz):
    nmenor=matriz[0] [0]
    for i in matriz:
        for num in i:
            if num < nmenor:
                nmenor=num
    
    for j in range(len(matriz)):
        if nmenor in matriz[j] :
            print('---------------------')
            print('el numero mas pequeño de la matriz es:',nmenor)
            print(f'columna: {matriz[j].index(nmenor)}')
            print(f'fila: {j}')
            
            






if __name__ == '__main__':
    matriz= [ r.sample(range(1,100),10),
              r.sample(range(1,100),10),
              r.sample(range(1,100),10),
              r.sample(range(1,100),10),
              r.sample(range(1,100),10)]
    
    for f in range (5):
        for c in range (10):
            print(matriz[f][c],end=' ')
        print()

    nmayor(matriz)
    nmenor(matriz)
  