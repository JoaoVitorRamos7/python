print('-=' * 20)
print("CALCULADORA")
print('-=' * 20)
n1 = int(input("Diite  o primeiro número: "))
operaçao = str(input("Informe a operação que deseja (+),(-),(/),(*): "))
while operaçao not in '+*-/':
    operaçao = str(input("Informe a operação que deseja (+),(-),(/),(*): "))
n2 = int(input("Digite o segundo valor para podermos finalizar sua operação Matemática: "))
som = 0
sub = 0
mult = 0 
div = float = 0
print('-=' * 20)
if operaçao == "+":
    som = n1 + n2
    print(f"A sua soma entre {n1} e {n2} é = {som}")
elif operaçao == "-":
    sub = n1 - n2
    print(f"A subtração entre os vaolres {n1} e {n2} é = {sub}")
elif operaçao == "/":
    div = n1 / n2
    print(f"A divisão sobre os valores {n1} e {n2} foi = {div}")
elif operaçao == "*":
    mult = n1 * n2
    print(f"A Multiplicação entre os seguintes números {n1} e {n2} conresponde = {mult}")