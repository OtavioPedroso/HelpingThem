arq = open("Teste.txt", 'r')
qtd_prova = int(arq.readline())
respostas = arq.readline().rsplit()
lista = arq.readlines()
arq.close()

i = 0
resultados = []
while i < qtd_prova:
    acertos = 0
    resposta = lista[i].rsplit()
    j = 1
    k = len(resposta)
    while j < k:
        if resposta[j] == respostas[j - 1]:
            acertos = acertos + 1
        j = j + 1
    i = i + 1
    resultados.append(resposta[0] + " " + str(acertos))

i = 0
while i < qtd_prova:
    print(resultados[i])
    i = i + 1
