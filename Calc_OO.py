class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Erro: divisão por zero!"
        return x / y

# Função principal
def main():
    calc = Calculator()

    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = calc.add(num1, num2)
    elif escolha == '2':
        resultado = calc.subtract(num1, num2)
    elif escolha == '3':
        resultado = calc.multiply(num1, num2)
    elif escolha == '4':
        resultado = calc.divide(num1, num2)
    else:
        resultado = "Opção inválida!"

    print("Resultado: ", resultado)

if __name__ == "__main__":
    main()
