def descobreParOuImpar(numero):
    resto = numero % 2
    
    if resto == 0:
        return "Par"
    else:
        return "Impar"
    

print(descobreParOuImpar(float(input("Digite um numero: "))))