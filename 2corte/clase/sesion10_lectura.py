def read():
    F=open('matrizAsignacion.txt','rt')
    line=F.readlines()  #leer las lineas una por una
    for i in line:
        a=i.rstrip('\n').split(',')
        print(f'{a} = {int(a[0])+int(a[1])}') #imprime la variable 'a' y sume el renglon 0 y 1 de a

def read2():
    F=open('matrizAsignacion.txt','rt')
    line=F.readline()
    F.seek(3)
    while line!='':
        print(line)
        opc=input('presieone enter')
        line=F.readline()
    print('finalizo la lectura')

def read3():
    F=open('matrizAsignacion.txt','rt')
    line=F.read()
    F.close()
    print(line,len(line))
    print('-----------')
    a=line.split('\n')
    for i in a:
        b=i.split(',')
        print(b)




if __name__ == '__main__':
    #read()
    #read2()
    read3()