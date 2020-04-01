# 5. Um “turning number” é o menor número em um array unimodal, que
# decresce e então, torna a crescer. Escreva uma função que encontra o
# index de um “turning number” em um array unimodal, por exemplo, o
# turning number em um array {10, 9, 8, 7, 6, 1, 2, 3, 4, 5} é 1, e o seu index é
# 5 (o qual é a saída esperada).

def calcula_turning_number(arr):
    # Inicia variavel com o primeiro valor
    anterior = arr[0]
    # Percorre array
    for x in arr:
        # Se os valores começaram a aumentar
        if x > anterior:
            # Retorna indice do ultimo valor antes do aumento
            return arr.index(anterior)
        else:
            # Atualiza variavel do numero anterior
            anterior = x

# Entrada de exemplo
entrada = [10, 9, 8 ,7, 6, 1, 2, 3, 4, 5]

# Realiza calculo do turning number
print(calcula_turning_number(entrada))
