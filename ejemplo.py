#Ejemplo
def entrada():
    print("Este programa determina una operacion dentro de un rango de valores")
    while True:
        try:
            global a
            a=int(input("Ingrese el rango inferior : "))
            break
        except ValueError :
            print("Debe ingresar un numero entero")
    while True:
        try:
            global b
            b=int(input("Ingrese el rango superior : "))
            break
        except ValueError :
            print("Debe ingresar un numero entero")
    menu()
def menu():
    print("********MENU******")
    print("a)Determinar los numeros primos.")
    print("b)Determinar los numeros pares.")
    print("c)Determinar los numeros que terminan en un numero dado.")
    print("d)Determinar los numeros multiplos de un numero dado.")
    print("e)salir")
    print("¿QUE OPCION DESEA REALIZAR?")
    global c
    c=input()
    c=c.lower()
    verificar()
def verificar():
    if c=='a':
        primos2(a,b)
    elif c=='b':
        pares2(a,b)
    elif c=='c':
        termina(a,b)
    elif c=='d':
        multiplo(a,b)
    elif c=='e':
        salir()
    else :
        print("La opcion que Ud. a escojido es incorrecta")
        print("Vuelva a intentarlo")
        menu()
def primos(g):
    h=0
    for i in range (2,g):
        if(g%i==0):
            h=h+1
    if h>0:
        return False
    elif h==0:
        return True
def primos2(a,b):
    if a<0:
        a=3
    if b<0:
        b=0
    k=[]
    for f in range(a,b+1):
        if (primos(f)==True):
            k.append(f)
    print (k)
    continuar()
def pares(g):
    if (g%2==0):
        return True
    else:
        return False
def pares2(a,b):
    if a<0:
        a=0
    if b<0:
        b=0
    k=[]
    for f in range (a,b):
        if(pares(f)==True):
            k.append(f)
    print (k)
    continuar()
def termina(a,b):
    if a<0:
        a=0
    if b<0:
        b=0
    k=[]
    while True:
        try:
            e=int(input("Ingrese el numero de terminacion : "))
            break
        except ValueError :
            print("Debe ingresar un numero entero")
    while (a<b+1):
        if(a%10==e):
            k.append(a)
        a=a+1
    print(k)
    continuar()
def multiplo(a,b):
    if a<0:
        a=0
    if b<0:
        b=0
    k=[]
    while True:
        try:
            e=int(input("Ingrese el numero de multiplicidad : "))
            break
        except ValueError :
            print("Debe ingresar un numero entero")
    for i in range (a,b+1):
        if (i%e==0):
            k.append(i)
    print(k)
    continuar()
def salir():
    print("¿Esta seguro de que desea salir?")
    print("a) si")
    print("b) no")
    e=input()
    e=e.lower()
    if(e=='a'):
        sys.exit
    elif(e=='b'):
        entrada()
    else:
        print("La opcion es incorrecta")
        salir()
def continuar():
    print("Desea :")
    print("a)Cambiar sus datos")
    print("b)Realizar otra opercion")
    print("c) salir")
    e=input()
    e=e.lower()
    if(e=='c'):
        salir()
    elif(e=='a'):
        entrada()
    elif(e=='b'):
        menu()
    else :
        print("La opcion ingresada es incorrecta")
        print("Intentelo de nuevo")
        continuar()
entrada()
