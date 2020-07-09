#Autora: Zavaleta Lorena

correo=str(input("Ingrese su correro electronico institucional: "))
validar=correo.split("@")
if (len(validar)==2):
    
    if (validar[1]=="untels.edu.pe"):
        
        print("Correo electrónico institucional valido.")
    
else:
    
    print("Correo electrónico institucional inválido.")
