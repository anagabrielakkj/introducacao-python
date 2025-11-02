numero_secreto = 42
max_tentativas = 5

print("Bem-vindo ao Jogo da Adivinhação!")
print(f"Você tem {max_tentativas} tentativas para adivinhar o número secreto.")
print("--------------------------------------")

for tentativa_atual in range(max_tentativas):
    
    print(f"\n--- Tentativa {tentativa_atual + 1} de {max_tentativas} ---")
    
    try:
        palpite = int(input("Digite o seu palpite: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas um número.")
        continue 

    if palpite == numero_secreto:
        print("Parabéns")
        break 
    
    elif palpite < numero_secreto:
        print(f"O número secreto é MAIOR que {palpite}.")
        
    else:
        print(f"O número secreto é MENOR que {palpite}.")

else:
    print("\n--------------------------------------")
    print("Você perdeu! Todas as tentativas foram esgotadas.")
    print(f"O número correto era: {numero_secreto}")