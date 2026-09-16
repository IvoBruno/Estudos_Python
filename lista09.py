import random

def q1_megasena():
    sorteados = set(random.sample(range(1, 61), 6))
    
    usuario = set()
    while len(usuario) < 6:
        try:
            num = int(input(f"Digite o {len(usuario) + 1}º número (1-60): "))
            if 1 <= num <= 60 and num not in usuario:
                usuario.add(num)
            else:
                print("Número repetido ou fora da faixa (1-60).")
        except ValueError:
            print("Digite apenas números inteiros.")

    acertos = sorteados & usuario
    print(f"\nSorteados: {sorted(sorteados)}")
    print(f"Seus números: {sorted(usuario)}")
    print(f"Total de acertos: {len(acertos)}")

if __name__ == "__main__":
    q1_megasena()

