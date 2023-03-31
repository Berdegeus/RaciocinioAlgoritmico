def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y


def main():
    while True:
        print("Escolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")
        if escolha == '5':
            print("Até mais!")
            break
        elif escolha not in ('1', '2', '3', '4'):
            print("Opção inválida")
            continue

        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))

        if escolha == '1':
            print(num1, '+', num2, '=', soma(num1, num2))
        elif escolha == '2':
            print(num1, '-', num2, '=', subtracao(num1, num2))
        elif escolha == '3':
            print(num1, '*', num2, '=', multiplicacao(num1, num2))
        elif escolha == '4':
            print(num1, '/', num2, '=', divisao(num1, num2))

if __name__ == '__main__':
    main()