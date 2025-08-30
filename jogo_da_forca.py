import random


palavras = [
    "gato", "maca", "brasil", "bicicleta", "parque", "girassol",
    "computador", "banana", "aviao", "elefante", "caneta", "oceano",
    "cachorro", "laranja", "franca", "passaro", "cidade", "montanha",
    "carro", "tigre", "brasil", "alemanha"
]

# Sorteia uma única palavra da lista
palavra_sorteada = random.choice(palavras)

# Cria a lista que representa a palavra a ser adivinhada (ex: ['_', '_', '_', '_'])
letras_descobertas = ["_" for _ in palavra_sorteada]

# Contadores de erros e letras acertadas
erros = 0
letras_acertadas = ""

# Define o número máximo de tentativas
LIMITE_ERROS = 6

print("--- Bem-vindo ao Jogo da Forca! ---")

# --- Loop Principal do Jogo ---
while True:
    # Mostra o estado atual da forca (palavra e erros)
    print(" ".join(letras_descobertas))
    print(f"Erros cometidos: {erros} de {LIMITE_ERROS}")

    # Pede uma letra ao jogador
    chute = input("Informe uma letra: ").lower().strip()

    # Verifica se o chute é uma única letra
    if len(chute) != 1 or not chute.isalpha():
        print("Por favor, digite apenas uma letra.")
        continue

    # --- Lógica de Verificação ---
    letra_encontrada = False
    
    # Percorre a palavra sorteada para verificar se o chute está correto
    for indice, letra in enumerate(palavra_sorteada):
        if chute == letra:
            letras_descobertas[indice] = letra
            letra_encontrada = True

    # Se a letra não foi encontrada, incrementa o contador de erros
    if not letra_encontrada:
        erros += 1
        print(f"Letra '{chute}' não encontrada. Tente novamente!")
    else:
        print(f"Boa! A letra '{chute}' está na palavra.")

    # --- Condições de Fim de Jogo ---

    # 1. Se o jogador venceu (não há mais '_' na lista)
    if "_" not in letras_descobertas:
        print("\n------------------------------------")
        print(f"Parabéns, você acertou! A palavra era: {palavra_sorteada}")
        print("------------------------------------")
        break

    # 2. Se o jogador perdeu (atingiu o limite de erros)
    if erros >= LIMITE_ERROS:
        print("\n------------------------------------")
        print("Que pena, você foi enforcado!")
        print(f"A palavra correta era: {palavra_sorteada}")
        print("------------------------------------")
        break
