def calculaProximo(vetor):
    novo = vetor[len(vetor)-1] + vetor[len(vetor)-2]
    vetor.append(novo)

fibonacci = [0,1]
while(len(fibonacci)<10):
    calculaProximo(fibonacci)

for i in fibonacci:
    print(i)