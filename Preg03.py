#Autora: Giannina Bernal Navarrete

def separarvariables():
    c1 = str(input("Ingrese la cadena: "))
    cont = 0
    valor = c1.split()
    
    for i in range (len(valor)):
        cont = cont + len(valor[i])
    
    return cont

print(separarvariables())