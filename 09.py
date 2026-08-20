maior_nota = []
alunos = [{"nome": "ana", "nota": 9.5},{"nome": "bruno", "nota": 10},{"nome": "carla", "nota": 7},{"nome": "danilo", "nota": 10}]
for i in alunos:
    if(len(maior_nota) == 0):
        maior_nota.append(i)
    elif(i["nota"] > maior_nota[0]["nota"]):
        maior_nota.clear()
        maior_nota.append(i)
    elif(i["nota"] == maior_nota[0]["nota"]): 
        maior_nota.append(i)

print(maior_nota)
