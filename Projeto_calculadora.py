# ENTRADA
valor_1 = input('Digite o valor 1: ')
valor_2 = input('Digite o valor 2: ')
print('Digite a operação:\n\t+ para adição\n\t- para subtração\n\t* para multiplicação\n\t/ para divisão')

#PROCESSAMENTO
operacao = input('Digite a operação desejada conforme menu acima: ')
equacao = f'{valor_1} {operacao} {valor_2}'
resultado = eval(equacao)

#SAIDA
print(f'{"*" * 25}\nResultado: {resultado}\n{"*" * 25}')