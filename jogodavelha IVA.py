import os
import time

#limpa a tela para aparecer apenas o tabuleiro atualizado
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#parte visual do jogo, o tabuleiro
tabuleiro = [' ' for _ in range(9)]

def desenhar_tabuleiro(): #DEVE TER UMA FORMA DE MELHORAR ISSO, MAS POR ENQUANTO VAI ASSIM MESMO
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

def verificar_vitoria(jogador):    #Linhas, colunas e diagonais
    vitorias = [
        [0,1,2], [3,4,5], [6,7,8],  #Linhas
        [0,3,6], [1,4,7], [2,5,8],  #Colunas
        [0,4,8], [2,4,6]            #Diagonais
    ]
    
    return any(tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == jogador 
              for a,b,c in vitorias)

def jogada_ia(meu, adv): #O simbolo que a IA é e símbolo da IA adversária (ou seja IA1=X,O e IA2=O,X)
    # enta vencer
    for i in range(9):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = meu
            if verificar_vitoria(meu):
                return i
            tabuleiro[i] = ' '
    
    # enta bloquear
    for i in range(9):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = adv
            if verificar_vitoria(adv):
                tabuleiro[i] = meu
                return i
            tabuleiro[i] = ' '
    
    # entro
    if tabuleiro[4] == ' ':
        return 4
    
    #cantos
    cantos = [0,2,6,8]
    for canto in cantos:
        if tabuleiro[canto] == ' ':
            return canto
    
    #espaço vazio qualquer
    for i in range(9):
        if tabuleiro[i] == ' ':
            return i


#jogo
def jogar():
    global tabuleiro
    tabuleiro = [' ' for _ in range(9)]
    
    print("#JOGO DA VELHA - IA vs IA#")
    print("IA 1 = X | IA 2 = O")
    print(" 1 2 3 ")
    print(" 4 5 6 ")
    print(" 7 8 9 ")
    
    time.sleep(3) #pausa para que possamos ver as jogadas de 3 em 3 segundos
    #ou seja instântaneo o resultado do jogo
    
    turno = 0  
    #0 é IA1=X
    #1 é IA2=O
    
    while True:
        desenhar_tabuleiro()
        
        if turno == 0:
            print("\nIA 1 (X) pensando...")
            time.sleep(3)
            pos = jogada_ia('X', 'O')
            tabuleiro[pos] = 'X'
            
            if verificar_vitoria('X'):
                desenhar_tabuleiro()
                print("IA 1 (X) VENCEU!")
                break
                
        else:
            print("\nIA 2 (O) pensando...")
            time.sleep(3)
            pos = jogada_ia('O', 'X')
            tabuleiro[pos] = 'O'
            
            if verificar_vitoria('O'):
                desenhar_tabuleiro()
                print("IA 2 (O) VENCEU!")
                break
        
        #deu velha
        if ' ' not in tabuleiro:
            desenhar_tabuleiro()
            print("DEU VELHA! Ninguém venceu.")
            break
        
        turno = 1 - turno

#jogar novamente
while True:
    jogar()
    while True: #não achei outra forma de validar a resposta do usuário sem usar um loop dentro do outro
        resposta = input("\nJogar novamente? (s/n): ").lower().strip()
        
        if resposta in ['s', 'sim', 'y', 'yes']:
            break  
            
        elif resposta in ['n', 'não', 'nao', 'no']:
            print("Obrigado por jogar!")
            exit()  
            
        else:
            print("Resposta inválida! Digite S/N, SIM/NÃO ou Y/N")
            continue #continue para perguntar novamente