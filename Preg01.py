
# Autor: Michael Condori Mavila

def NumeroPrimo(n):
    if n < 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2, n):
            if n % i == 0:
                return 0
        return 1
    
numero=int(input("Ingrese un numero para verificar si es primo: "))

if (NumeroPrimo(numero)==1):
    
    print(f"{numero} es primo.")
    
else:
    
    print(f"{numero} no es primo.")
