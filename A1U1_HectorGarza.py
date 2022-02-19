# Hector Alejandro Garza Arvizu
# Programacion Logica y Funcional
# Actividad 1 - Unidad 1

def _ejercicio1(a,b,c,d,x,y):
    value1 = b*a-pow(b,2)/4*c
    value2 = (a*b)/pow(3,2)
    value3 = (((b+c)/2*a+10)*3*b)-6
    value4 = pow(a,pow(b,c))
    value5 = 3*pow(x,4)-5*pow(x,3)+x*12-17
    value6 = (b+d)/(c+4)
    value7 = pow(b,2)-a*a*c
    value8 = pow((pow(x,2)+pow(y,2)),(1/2))
    value9 = 7*10-50%3*4+9
    value10 = (7*(10-5)%3)*4+9
    results = [value1, value2, value3, value4, value5, value6, value7, value8, value9, value10]
    return results

def _ejercicio2(a,b,c,d,x,y,w,semestre,grupo,nombre):
    if a==b and b==c and c==d:
        print('1.- ', True)
    else:
        print('1.- ', False)
    if y>x and y<w:
        print('2.- ', True)
    else:
        print('2.- ', False)
    if semestre>1 and semestre<9:
        print('3.- ', True)
    else:
        print('3.- ', False)
    if x!=y and y!=w and x!=w:
        print('4.- ', True)
    else:
        print('4.- ', False)
    if grupo=='a' or grupo=='b':
        print('5.- ', True)
    else:
        print('5.- ', False)
    if a%2==0 or a<3:
        print('6.- ', True)
    else:
        print('6.- ', False)
    if b%2==1 or b>=12:
        print('7.- ', True)
    else:
        print('7.- ', False)
    if nombre=='pepe' or nombre=='luis' or nombre=='mario':
        print('8.- ', True)
    else:
        print('8.- ', False)
    if x>7:
        print('9.- ', True)
    else:
        print('9.- ', False)
    if y<=3.2:
        print('10.- ', True)
    else:
        print('10.- ', False)


if __name__ == '__main__':
    i = 0
    a = int(input("Ingresa el valor de a: "))
    b = int(input("Ingresa el valor de b: "))
    c = int(input("Ingresa el valor de c: "))
    d = int(input("Ingresa el valor de d: "))
    x = int(input("Ingresa el valor de x: "))
    y = int(input("Ingresa el valor de y: "))
    w = int(input("Ingresa el valor de w: "))
    semestre = int(input("Ingresa el semestre: "))
    grupo = str(input("Ingresa el la letra del grupo: ")).lower()
    nombre = str(input("Ingresa el nombre: ")).lower()
    
    print('Ejercicio 1')
    results = _ejercicio1(a, b, c, d, x, y)
    print("Resultados: ")
    for value in results:
        i+=1
        print(str(i) + ".- ", value)
    
    print('Ejercicio 2')
    _ejercicio2(a,b,c,d,x,y,w,semestre,grupo,nombre)