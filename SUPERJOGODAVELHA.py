import os
import time
import random

#Funções comuns a todos os modos de jogo (PvP, PvIA, IAvsIA)

def loading_animado():
    mensagem = "🚀 Iniciando Super Jogo da Velha"
    pontos = ""
    
    for i in range(20):  #+- 2 segundos. a cada (10) = 1s
        limpar_tela()
        print(mensagem + pontos)
        pontos += "."
        if len(pontos) > 3:
            pontos = ""
        time.sleep(0.1) #o tempo da velocidade da animação


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

tabuleiro = [' ' for _ in range(9)]

def desenhar_tabuleiro():
    limpar_tela()
    print("   |   |   ")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("   |   |   ")

def verificar_vitoria(jogador):
    vitorias = [
        [0,1,2], [3,4,5], [6,7,8],  #Linhas -
        [0,3,6], [1,4,7], [2,5,8],  #Colunas |
        [0,4,8], [2,4,6]            #Diagonais \ /
    ]
    return any(tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == jogador 
              for a,b,c in vitorias)


#funcções de jogadas

def jogada_humano():
    #unificada X e O
    while True:
        try:
            pos = int(input("\nSua jogada (1-9): ")) - 1
            if 0 <= pos <= 8 and tabuleiro[pos] == ' ':
                return pos
            else:
                print("POSIÇÃO INVÁLIDA! Use 1-9 onde está vazio.")
        except:
            print("ERRO! Digite um número de 1 a 9!")

def jogada_ia(meu_simbolo, simbolo_adversario): #jogada da IA 
    #Funções: vence/bloqueia/centro/cantos
    for i in range(9):  #vencer
        if tabuleiro[i] == ' ':
            tabuleiro[i] = meu_simbolo
            if verificar_vitoria(meu_simbolo):
                return i
            tabuleiro[i] = ' '
    
    for i in range(9): #atrapalhar
        if tabuleiro[i] == ' ':
            tabuleiro[i] = simbolo_adversario
            if verificar_vitoria(simbolo_adversario):
                tabuleiro[i] = meu_simbolo
                return i
            tabuleiro[i] = ' '
            
    #melhorar a IA para que ela possa ter mais variações de jogadas
    #centro
    for i in range(1):  #testa 1 vez
        if random.random(0,1.0) < 0.5:  #50% de chance de escolher o centro quando disponível
            if tabuleiro[4] == ' ':
                return 4
        else: 
            pass #acho que tem como modificar e melhorar 
    
    #cantos
    cantos = [0,2,6,8]
    for canto in random.sample(cantos, len(cantos)): 
        if tabuleiro[canto] == ' ':
            return canto
    
    #espaço vazio qualquer
    for i in range(9):
        if tabuleiro[i] == ' ':
            return i


#Visual Menu

def mostrar_menu():
    limpar_tela()
    print("="*35)
    print("     SUPER JOGO DA VELHA")
    print("="*35)
    print()
    print("ESCOLHA O MODO DE JOGO:")
    print("   1  PvP  - Jogador vs Jogador")
    print("   2️  PvIA - Jogador vs IA")
    print("   3️  IAvsIA - IA vs IA")
    print()
    print("   Ou digite: PVP, PvsIA, IAvsIA")
    print("="*35)

def escolher_modo():
    while True:
        modo = input("\nSeu modo (1/2/3 ou PVP/PVIA/IAVIA): ").strip().lower()
        if modo in ['1', 'pvp', 'pvp']:
            return 'pvp'
        elif modo in ['2', 'pvia', 'pvai', 'pvsia']:
            return 'pvia'
        elif modo in ['3', 'iavsia', 'iavsia']:
            return 'iavsia'
        else:
            print("INVÁLIDO! Tente: 1, 2, 3, PVP, PVIA ou IAVSIA")

def escolher_peca(): #não funciona
    while True:
        peca = input("\n⚔️  Escolha sua peça (X ou O): ").strip().upper()
        if peca in ['X', 'O']:
            return peca
        print("ERRADO! Escolha apenas X ou O!")

#Lógica dos jogos

def jogar_pvp():
    """PvP - Jogador vs Jogador"""
    reset_tabuleiro()
    print("\n👤 MODO PvP ATIVADO! 👤")
    print("🟥 Jogador 1 = X | 🟦 Jogador 2 = O")
    
    mostrar_numeros_posicoes()
    time.sleep(2)
    
    turno = 0  # 0=X, 1=O
    
    while True:
        desenhar_tabuleiro()
        
        if turno == 0:
            print("\n🟥 JOGADOR 1 (X) - Sua vez!")
            pos = jogada_humano()
            tabuleiro[pos] = 'X'
            
            if verificar_vitoria('X'):
                desenhar_tabuleiro()
                print("JOGADOR 1 (X) VENCEU!")
                break
        else:
            print("\n🟦 JOGADOR 2 (O) - Sua vez!")
            pos = jogada_humano()
            tabuleiro[pos] = 'O'
            
            if verificar_vitoria('O'):
                desenhar_tabuleiro()
                print("JOGADOR 2 (O) VENCEU!")
                break
        
        if ' ' not in tabuleiro:
            desenhar_tabuleiro()
            print("DEU VELHA! Ninguém venceu.")
            break
            
        turno = 1 - turno

def jogar_pvia(minha_peca):
    """PvIA - Jogador vs IA"""
    reset_tabuleiro()
    ia_peca = 'O' if minha_peca == 'X' else 'X'
    
    print(f"\n🤖 MODO PvIA ATIVADO! 🤖")
    print(f"   Você = {minha_peca} | IA = {ia_peca}")
    
    mostrar_numeros_posicoes()
    time.sleep(2)
    
    # Humano joga primeiro se for X
    turno_humano_primeiro = (minha_peca == 'X')
    turno_humano = turno_humano_primeiro
    
    while True:
        desenhar_tabuleiro()
        
        if turno_humano:
            print(f"\n👤 VOCÊ ({minha_peca}) - Sua vez!")
            pos = jogada_humano()
            tabuleiro[pos] = minha_peca
            
            if verificar_vitoria(minha_peca):
                desenhar_tabuleiro()
                print(f"🎉 VOCÊ ({minha_peca}) VENCEU! 🏆")
                break
        else:
            print(f"\n🤖 IA ({ia_peca}) pensando...")
            time.sleep(1)
            pos = jogada_ia(ia_peca, minha_peca)
            tabuleiro[pos] = ia_peca
            
            if verificar_vitoria(ia_peca):
                desenhar_tabuleiro()
                print(f"😈 IA ({ia_peca}) VENCEU!")
                break
        
        if ' ' not in tabuleiro:
            desenhar_tabuleiro()
            print("DEU VELHA! Ninguém venceu.")
            break
            
        turno_humano = not turno_humano

def jogar_iavsia():
    """IAvsIA - IA vs IA"""
    reset_tabuleiro()
    print("\n🤖MODO IAvsIA ATIVADO!")
    print("   IA 1 = X | IA 2 = O")
    
    mostrar_numeros_posicoes()
    time.sleep(2)
    
    turno = 0  # 0=IA1(X), 1=IA2(O)
    
    while True:
        desenhar_tabuleiro()
        
        if turno == 0:
            print("\n🤖 IA 1 (X) pensando...")
            time.sleep(1.5)
            pos = jogada_ia('X', 'O')
            tabuleiro[pos] = 'X'
            
            if verificar_vitoria('X'):
                desenhar_tabuleiro()
                print("IA 1 (X) VENCEU!")
                break
        else:
            print("\n🤖 IA 2 (O) pensando...")
            time.sleep(1.5)
            pos = jogada_ia('O', 'X')
            tabuleiro[pos] = 'O'
            
            if verificar_vitoria('O'):
                desenhar_tabuleiro()
                print("IA 2 (O) VENCEU!")
                break
        
        if ' ' not in tabuleiro:
            desenhar_tabuleiro()
            print("DEU VELHA! Ninguém venceu.")
            break
            
        turno = 1 - turno

#funções importantes mas como auxiliares

def reset_tabuleiro(): #reseta tabuleiro
    global tabuleiro
    tabuleiro = [' ' for _ in range(9)]

def mostrar_numeros_posicoes(): #mostra as posições para o jogador
    print("\nPOSIÇÕES:")
    print(" 1 2 3 ")
    print(" 4 5 6 ")
    print(" 7 8 9 ")

def jogar_novamente(modo): #recebe o modo atual como parâmetro
    while True:
        print("\nJogar novamente?")
        print("\n   S = Sim (mesmo modo)")
        print("\n   N = Sair")
        print("\n   M = Menu principal (escolher modo)")
        resposta = input(" ").lower().strip()
        
        if resposta in ['s', 'sim', 'y', 'yes']:
            return modo  #retorna o MESMO modo para continuar no mesmo tipo de jogo
            
        elif resposta in ['n', 'não', 'nao', 'no']:
            print("Obrigado por jogar!")
            exit()  
        
        elif resposta in['m', 'menu']:
            return None  #retorna None para voltar ao menu principal    
            
        else:
            print("Resposta inválida! Digite S/N, SIM/NÃO ou Y/N")
            continue

#loop principal do programa
#foi chato de fazer essa parte, mas é a melhor forma de validar a resposta do usuário sem usar um 
#loop dentro do outro, acho que tem como melhorar, mas por enquanto tá ok

def main():
    modo_atual = None #oo que determina se vai repetir o modo ou não. funciona como "cachê"
    while True:
        if modo_atual is None: # se tá vazio = 1º vez jogando, quase
            mostrar_menu()
            modo_atual = escolher_modo()
        
        if modo_atual == 'pvp':
            jogar_pvp()
        elif modo_atual == 'pvia':
            minha_peca = escolher_peca()
            jogar_pvia(minha_peca)
        elif modo_atual == 'iavsia':
            jogar_iavsia()
        
        modo_atual = jogar_novamente(modo_atual)
        if modo_atual is None:  
            break


if __name__ == "__main__":
    loading_animado()
    time.sleep(1)
    main()