print("Bienvenido a la calculadora de Corazon de Parlie")
num1= (float(input("Ingrese el primer numero:")))
num2= (float(input( "Ingrese el segundo numero:")))
print("Elija la operacion que desea realizar")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
operacion= (int(input("Ingrese el numero de la operacion que desea realizar:")))
if operacion==1:
    resultado= num1 + num2
    print("El resultado de la suma es:", resultado)
elif operacion==2:
    resultado= num1 - num2
    print("El resultado de la resta es:", resultado)
elif operacion==3:
    resultado= num1 * num2
    print("El resultado de la multiplicacion es:", resultado)
elif operacion==4:
    if num2==0:
        print("Error: No se puede dividir entre cero")
    else:
        resultado= num1 / num2
        print("El resultado de la division es:", resultado)
else:
    print("Operacion no valida")
