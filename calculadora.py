# Funções da calculadora

# Função para realizar a operação de soma
def soma():
    """
    Realiza a operação de soma entre dois números inseridos pelo usuário e exibe o resultado.
    """
    n1 = input('Insira o primeiro número: ').replace(',', '.')  # Solicita o primeiro número
    n2 = input('Insira o segundo número: ').replace(',', '.')  # Solicita o segundo número

    n1 = float(n1)  # Converte o primeiro número para float
    n2 = float(n2)  # Converte o segundo número para float

    resultado = n1 + n2  # Calcula a soma dos números

    # Verifica se o resultado é um número inteiro ou decimal e formata a saída
    if resultado % 2 == 0:
        if resultado >= 1000:
            print(f'Resultado: {resultado:_.0f} \n'.replace('.', ',').replace('_', '.'))
        else:
            print(f'Resultado: {resultado:.0f} \n'.replace('.', ',').replace('_', '.'))
    else:
        if resultado >= 1000:
            if resultado % 1 != 0:
                print(f'Resultado: {resultado:_.2f} \n'.replace('.', ',').replace('_', '.'))
            else:
                print(f'Resultado: {resultado:.0f} \n'.replace('.', ',').replace('_', '.'))
        else:
            if resultado % 1 != 0:
                print(f'Resultado: {resultado:_.2f} \n'.replace('.', ',').replace('_', '.'))
            else:
                print(f'Resultado: {resultado:.0f} \n'.replace('.', ',').replace('_', '.'))


# Função para realizar a operação de subtração
def sub():
    """
    Realiza a operação de subtração entre dois números inseridos pelo usuário e exibe o resultado.
    """
    n1 = input('Insira o primeiro número: ').replace(',', '.')  # Solicita o primeiro número
    n2 = input('Insira o segundo número: ').replace(',', '.')  # Solicita o segundo número

    n1 = float(n1)  # Converte o primeiro número para float
    n2 = float(n2)  # Converte o segundo número para float

    resultado = n1 - n2  # Calcula a subtração dos números

    # Verifica se o resultado é um número inteiro ou decimal e formata a saída
    if resultado % 2 == 0:
        if resultado >= 1000:
            print(f'Resultado: {resultado:_.0f} \n'.replace('.', ',').replace('_', '.'))
        else:
            print(f'Resultado: {resultado:.0f} \n'.replace('.', ',').replace('_', '.'))
    else:
        if resultado >= 1000:
            if resultado % 1 != 0:
                print(f'Resultado: {resultado:_.2f} \n'.replace('.', ',').replace('_', '.'))
            else:
                print(f'Resultado: {resultado:.0f} \n'.replace('.', ',').replace('_', '.'))
        else:
            if resultado % 1 != 0:
                print(f'Resultado: {resultado:_.2f} \n'.replace('.', ',').replace('_', '.'))
            else:
                print(f'Resultado: {resultado:.0f} \n'.replace('.', ',').replace('_', '.'))


# Função para realizar a operação de multiplicação
def mult():
    """
    Realiza a operação de multiplicação entre dois números inseridos pelo usuário e exibe o resultado.
    """
    n1 = input('Insira o primeiro número: ').replace(',', '.')  # Solicita o primeiro número
    n2 = input('Insira o segundo número: ').replace(',', '.')  # Solicita o segundo número

    n1 = float(n1)  # Converte o primeiro número para float
    n2 = float(n2)  # Converte o segundo número para float

    resultado = n1 * n2  # Calcula a multiplicação dos números

    # Verifica se o resultado é um número inteiro ou decimal e formata a saída
    if resultado % 2 == 0:
        if resultado >= 1000:
            print(f'Resultado: {resultado:_.0f} \n'.replace('.', ',').replace('_', '.'))
        else:
            print(f'Resultado: {resultado:.0f} \n'.replace('.', ',').replace('_', '.'))
    else:
        if resultado >= 1000:
            if resultado % 1 != 0:
                print(f'Resultado: {resultado:_.2f} \n'.replace('.', ',').replace('_', '.'))
            else:
                print(f'Resultado: {resultado:.0f} \n'.replace('.', ',').replace('_', '.'))
        else:
            if resultado % 1 != 0:
                print(f'Resultado: {resultado:_.2f} \n'.replace('.', ',').replace('_', '.'))
            else:
                print(f'Resultado: {resultado:.0f} \n'.replace('.', ',').replace('_', '.'))


# Função para realizar a operação de divisão
def div():
    """
    Realiza a operação de divisão entre dois números inseridos pelo usuário e exibe o resultado.
    """
    n1 = input('Insira o primeiro número: ').replace(',', '.')  # Solicita o primeiro número
    n2 = input('Insira o segundo número: ').replace(',', '.')  # Solicita o segundo número

    n1 = float(n1)  # Converte o primeiro número para float
    n2 = float(n2)  # Converte o segundo número para float

    if n2 == 0:
        print('Não é possível dividir por zero \n')  # Verifica se o divisor é zero

    else:
        resultado = n1 / n2  # Calcula a divisão dos números

        # Verifica se o resultado é um número inteiro ou decimal e formata a saída
        if resultado % 2 == 0:
            if resultado >= 1000:
                print(f'Resultado: {resultado:_.0f} \n'.replace('.', ',').replace('_', '.'))
            else:
                print(f'Resultado: {resultado:.0f} \n'.replace('.', ',').replace('_', '.'))
        else:
            if resultado >= 1000:
                if resultado % 1 != 0:
                    print(f'Resultado: {resultado:_.2f} \n'.replace('.', ',').replace('_', '.'))
                else:
                    print(f'Resultado: {resultado:.0f} \n'.replace('.', ',').replace('_', '.'))
            else:
                if resultado % 1 != 0:
                    print(f'Resultado: {resultado:_.2f} \n'.replace('.', ',').replace('_', '.'))
                else:
                    print(f'Resultado: {resultado:.0f} \n'.replace('.', ',').replace('_', '.'))


# Inicia a calculadora

def app_calculadora():
    """
    Inicia a calculadora no terminal, onde o usuário pode selecionar operações matemáticas, como adição, subtração,
    multiplicação e divisão, e realizar cálculos com números inseridos interativamente. O loop principal permite que o
    usuário continue a operar até escolher a opção de sair.
    """
    while True:

        print('1 - Adição')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Sair')

        op = input('> ')

        if not op.isdigit():
            print('Insira uma opção válida')

        else:

            if int(op) == 5:
                print('Encerrando a calculadora')
                break

            if int(op) == 1:
                soma()

            if int(op) == 2:
                sub()

            if int(op) == 3:
                mult()

            if int(op) == 4:
                div()


# Chama a função app_calculadora para iniciar a calculadora
app_calculadora()
