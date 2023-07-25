import Forca
import Adivinhacao

def escolha_jogos():
    print("************************************")
    print("* Escolha o seu jogo!! *")
    print("************************************")

    print("(1) Foca (2) Adivinhação")
    jogo = int(input("Qual o jogo:"))

    if jogo == 1:
        print("Jogando Forca")
        Forca.jogar_forca()
    elif jogo == 2:
        print("Jogando Adivinhação")
        Adivinhacao.jogar_adivinhacao()

if __name__ == "__main__":
    escolha_jogos()
