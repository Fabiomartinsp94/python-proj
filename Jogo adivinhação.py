import random

numeros = random.randint(0,101)


print("Bem vindo ao jogo da Adivinhação")
print("Escolha uma dificuldade (1) fadinha (2)princesa (3)gorila")

dificuldade = int(input("digite a dificuldade"))

if (dificuldade == 1):
    tentativas = 20
elif (dificuldade == 2):
    tentativas = 10
else:
    tentativas=5



while (tentativas >= 1):
    chute_str = input("Digite seu numero: ")
    print("você digitou: " + chute_str)
    chute = int(chute_str)

    certo = numeros == chute
    menor = numeros > chute
    maior = numeros < chute

    if(certo):
        print("parabens, você acertou")
        break
    else:
        if(menor):
            print(chute_str + "é menor do que o numero a ser descoberto!")
        if(maior):
            print(chute_str + "é maior do que o numero a ser descoberto!")

    tentativas = tentativas -1


print("fim de jogo")