#Estrutura de Condição ,de acordo com o usúraio
def logica(op, value1, value2,):
    if op == '+':
         print(f'O resutado da expressão com os seguintes numeros {value1},  {value2} foi de {value1 + value2}')
    elif op == "-":
         print(f'O resutado da expressão com os seguintes numeros {value1},  {value2} foi de {value1 - value2}')
    elif op == "*":
            print(f'O resutado da expressão com os seguintes numeros {value1},  {value2} foi de {value1 * value2}')
    elif op == "/":
            print(f'O resutado da expressão com os seguintes numeros {value1},  {value2} foi de {int(value1 / value2)}')

#Interação com o Usuario
#Vamos testar o valor, se é int ou float,para podermos retornar output

value1 = None
value2 = None
op = None
input1_nao_e_int_ou_float = True

#ve se o primeiro valor é int ou float
while input1_nao_e_int_ou_float:
     
     
while not type(value2) is int and float:
     value2 = input('Houve um erro na digitação,Informe um numero novamente: ')

logica(op, value1, value2)

# value1 = input('Informe um numero: ')
# op = str(input('Escolha uma operação para podermos continuar (+) (-) (*) (/): '))
# value2 = input('Informe o segundo numero: ')



