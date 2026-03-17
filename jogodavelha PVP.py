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


#X
def jogada_humanoX():
    while True:
        try:
            pos = int(input("\nSua jogada (1-9): ")) - 1
            if 0 <= pos <= 8 and tabuleiro[pos] == ' ':
                return pos
            else: #aqui puxa caso o usuário digite um número válido, mas a posição já esteja ocupada
                print("POSIÇÃO INVÁLIDA! Use 1-9 onde está vazio.")
        except: #aqui puxa caso o usuário digite algo que não seja um número ou não esteja entre 1-9
            print("ERRADO! Digite um número de 1 a 9!")


#y
def jogada_humanoY():
    while True:
        try:
            pos = int(input("\nSua jogada (1-9): ")) - 1
            if 0 <= pos <= 8 and tabuleiro[pos] == ' ':
                return pos
            else: #aqui puxa caso o usuário digite um número válido, mas a posição já esteja ocupada
                print("POSIÇÃO INVÁLIDA! Use 1-9 onde está vazio.")
        except: #aqui puxa caso o usuário digite algo que não seja um número ou não esteja entre 1-9
            print("ERRADO! Digite um número de 1 a 9!")


#jogo
def jogar():
    global tabuleiro
    tabuleiro = [' ' for _ in range(9)]
    
    print("#JOGO DA VELHA#")
    print("Você é X | IA é O")
    print(" 1 2 3 ")
    print(" 4 5 6 ")
    print(" 7 8 9 ")
    
    time.sleep(3)
    
    turno = 0  # 0 = X, 1 = Y
    
    while True:
        desenhar_tabuleiro()
        
        if turno == 0:  #X VENCEU
            pos = jogada_humanoX()
            tabuleiro[pos] = 'X'
            
            if verificar_vitoria('X'):
                desenhar_tabuleiro()
                print("O X VENCEU!")
                break
                
        else:  #Y VENCEU
            pos = jogada_humanoY()
            tabuleiro[pos] = 'O'
            
            if verificar_vitoria('O'):
                desenhar_tabuleiro()
                print("A Y VENCEU!")
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