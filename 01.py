idade = int(input("Digite sua idade: "))
if(idade < 16):
    print("Não pode votar")
elif (idade >= 18 and idade < 80):
    print("Voto obrigatorio")
else:
    print("Voto opcional")