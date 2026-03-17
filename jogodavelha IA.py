import os

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

# Jogada da IA (simples mas esperta!)
def jogada_ia():
    for i in range(9): #vencer
        if tabuleiro[i] == ' ':
            tabuleiro[i] = 'O'
            if verificar_vitoria('O'): #analisa a possibilidade de vitória da IA, se tiver, joga
                return i
            tabuleiro[i] = ' '
    
    for i in range(9): #atrapalhar
        if tabuleiro[i] == ' ':
            tabuleiro[i] = 'X'
            if verificar_vitoria('X'): #analisa a possibilidade de vitória do humano, se tiver, bloqueia
                tabuleiro[i] = 'O'
                return i
            tabuleiro[i] = ' '
    
    #centro
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

#jogaddor
def jogada_humano():
    while True:
        try:
            pos = int(input("\nSua jogada (1-9): ")) - 1
            if 0 <= pos <= 8 and tabuleiro[pos] == ' ':
                return pos
            else: #aqui puxa caso o usuário digite um número válido, mas a posição já esteja ocupada
                print("❌ Posição inválida! Use 1-9 onde está vazio.")
        except: #aqui puxa caso o usuário digite algo que não seja um número ou não esteja entre 1-9
            print("❌ Digite um número de 1 a 9!")

#jogo
def jogar():
    global tabuleiro
    tabuleiro = [' ' for _ in range(9)]
    
    print("#JOGO DA VELHA#")
    print("Você é X | IA é O")
    print(" 1 2 3 ")
    print(" 4 5 6 ")
    print(" 7 8 9 ")
    
    turno = 0  # 0 = humano, 1 = IA
    
    while True:
        desenhar_tabuleiro()
        
        if turno == 0:  #HUMANO VENCEU
            pos = jogada_humano()
            tabuleiro[pos] = 'X'
            
            if verificar_vitoria('X'):
                desenhar_tabuleiro()
                print("O HUMANO VENCEU!")
                break
                
        else:  #IA VENCEU
            pos = jogada_ia()
            tabuleiro[pos] = 'O'
            
            if verificar_vitoria('O'):
                desenhar_tabuleiro()
                print("A IA VENCEU!")
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
            print("👋 Valeu por jogar!")
            exit()  
            
        else:
            print("❌ Resposta inválida! Digite S/N, SIM/NÃO ou Y/N")
            continue #continue para perguntar novamente