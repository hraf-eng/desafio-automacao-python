# 4. Implemente o algoritmo do Bubble Sort em Python e utilize este algoritmo
# para desenvolver um programa, que recebe uma string como entrada e
# ordena os valores informados. Esta string deve ser separada por espaços
# em branco, informando assim os números que devem ser ordenados.
# Como saída este programa deve retornar um valor do tipo string
# apresentando os números ordenados.
# E.g.: Entrada: ‘10 8 2 3 5 1’
#  Saída: ‘1 2 3 5 8 10’

def bubble_sort(arr):
    # Define o indice final da busca (decrescente)
    for limite in reversed(range(0, len(arr))): 
        # Percorre o array
        for pos in range(0, limite):
            # Se item atual maior que o proximo
            if arr[pos] > arr[pos+1]:
                # Armazena valor do campo
                aux = arr[pos]

                # Troca os valores
                arr[pos] = arr[pos + 1]
                arr[pos + 1] = aux

# Coleta input do usuário
entrada = input('Informe os numeros: ')

# Quebra separa a entrada a cada espaço
dados = entrada.split(' ')

# Percorre o array dos dados de entrada
for i in range(len(dados)):
    # Converte a entrada de string para inteiro
    dados[i] = int(dados[i])

# Aplica o bubble sort no array
bubble_sort(dados)

saida = ''

# Percorre numeros ordenados
for numero in dados:
    # Converte numero para string e concatena na string de saída
    saida = saida + str(numero) + ' '

# Exibe resultado
print(saida)