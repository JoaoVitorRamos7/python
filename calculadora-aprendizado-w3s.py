# cabeçalho da calculadora
def header_cabeçalho():
    print('-=' * 20)
    print("CALCULADORA")
    print('-=' * 20)
header_cabeçalho()

# Interação com o usuario,Criamos uma variavel que recebe a informação do usuario
valor1= float(input("Digite  o primeiro número: "))

# Uma variavel do tipo str que recebe a operação do usuario 
# a função strip, retira os espaços do input , no qual o usario escreve
op = str(input("Informe a operação que deseja (+),(-),(/),(*): ")).strip()

# Criamos uma estrutura de Repetição While,que enquando a varivel operação n for '+*-/' ficara em loop
def repetição():
    while operacao not in '+*-/':
        # a função input , retorna a imformação do usuario
         operacao = str(input("Informe a operação que deseja (+),(-),(/),(*): "))

# função que retorna a informação do usuário
valor2 = float(input("Digite o segundo valor para podermos finalizar sua operação Matemática: "))

#variaveis 

#Estrutura de Condição
print('-=' * 20)
def recurcese(op,valor1,valor2):
    if op == "+":
        print(f"A sua soma entre {valor1} e {valor2} é = {valor1 + valor2}")
    elif op == "-":
        print(f"A subtração entre os vaolres {valor1} e {valor2} é = {valor1 + valor2}")
    elif op == "/":
        print(f"A divisão sobre os valores {valor1} e {valor2} foi = {valor1 + valor2}")
    elif op == "*":
        print(f"A Multiplicação entre os seguintes números {valor1} e {valor2} conresponde = {valor1 + valor2}")
recurcese()