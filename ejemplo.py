#Ejemplo
print("CALCULADORA")
print("1)-- SUMA Y RESTA")
print("2)-- NUMEROS IMPARES MENOS MULTIPLO DE 7")
opc=int(input("Seleccione la opcion a realizar: "))
if opc==1:
    a=int(input("Ingrese un numero entero: "))
    b=int(input("Ingrese el segundo numero entero: "))
    print("La suma de ",a," y ",b,"es: ",(a+b))
    print("La diferencia de ",a," y ",b," es: ",(a-b))
if opc==2:
    a=int(input("Ingrese el limite inferior: "))
    b=int(input("Ingrese el limite superior: "))
    while a>b :
        print("El limite inferior es mayor que el limite superior")
        a=int(input("Ingrese el limite inferior: "))
        b=int(input("Ingrese el limite superior: "))
    cont=0
    for i in range(a,b+1):
        if i%2!=0 and i%7!=0:
            cont=cont+1
    print("La cantidad de numeros impares menos multiplos de 7 es: ",cont)
