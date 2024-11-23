#Interação com o Usuario
value1 = int(input('Informe um numero: '))

op = str(input('Escolha uma operação para podermos continuar (+) (-) (*) (/): '))

value2 = int(input('Informe o segundo numero: '))

#Estrutura de Condição ,de acordo com o usúraio
if op == '+':
    print(f'O resutado da expressão com os seguintes numeros {value1}, {value2} foi de {value1 + value2}')
elif op == "-":
    print(f'O resutado da expressão com os seguintes numeros {value1}, {value2} foi de {value1 - value2}')
elif op == "*":
    print(f'O resutado da expressão com os seguintes numeros {value1}, {value2} foi de {value1 * value2}')
elif op == "/":
    print(f'O resutado da expressão com os seguintes numeros {value1}, {value2} foi de {int(value1 / value2)}')