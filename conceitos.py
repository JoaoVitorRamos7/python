# programação 

## sincrona
'''
Síncrona: Em programação síncrona, as operações são realizadas de forma sequencial, ou seja, uma tarefa é executada após a outra. Se uma tarefa precisa esperar o resultado de outra, o programa "trava" ou bloqueia até que essa operação seja concluída.
'''

# import time

# def tarefa_longa():
#     time.sleep(3)
#     print("Tarefa longa concluída!")

# def tarefa_pronta():
#     print("Tarefa pronta!")

# def programa_sincrono():
#     tarefa_longa()    # Mas a tarefa longa vai bloquear o fluxo de execução por 3 segundos
#     tarefa_pronta()   # A execução de tarefa_pronta ocorre imediatamente
#     print("Fim do programa.")

# programa_sincrono()


## asincrona
'''
Assíncrona: Na programação assíncrona, o programa não bloqueia a execução enquanto espera por tarefas demoradas. Ele pode iniciar a execução de uma tarefa e, enquanto espera o resultado de uma operação (como uma consulta a um banco de dados ou uma requisição de rede), o controle é dado para outras operações. Isso melhora a performance e a capacidade de resposta do programa.
'''
# import asyncio

# async def tarefa_longa():
#     await asyncio.sleep(3)
#     print(f"Tarefa longa concluída!")

# async def tarefa_pronta():
#     print(f"Tarefa pronta!")

# async def programa_assincrono():
#     await tarefa_pronta()  # Executa imediatamente
#     await tarefa_longa()   # Não bloqueia a execução, aguarda de forma assíncrona
#     print("Fim do programa.")

# asyncio.run(programa_assincrono())


## defensiva
def processar_dados(dados):
    # Verificar se os dados são uma lista
    if not isinstance(dados, list):
        raise TypeError("Os dados precisam ser uma lista.")
    if not dados:
        raise ValueError("A lista não pode estar vazia.")
    
    # Processo fictício de manipulação de dados
    return [dado * 2 for dado in dados]

# Exemplo de uso
try:
    dados_validos = ['a', 2, 3]
    dados_invalidos = "não é uma lista"
    print(processar_dados(dados_validos))  # Funcionando corretamente
    print(processar_dados(dados_invalidos))  # Gerará erro
except (TypeError, ValueError) as e:
    print(f"Erro: {e}")
