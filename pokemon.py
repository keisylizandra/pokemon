from random import randint

mapa = [["A","A","A","A","A", "" ,"" ,"A","A","A","A","A"],
        ["A","","","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"A","" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","E","E","A","E","E","E","G","G","G","A"],
        ["A","" ,"" ,"" ,"A","G","G","G","G","G","G","A"],
        ["A","E","E","E","A","G","G","G","G","G","G","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"G","G","G","A"],
        ["A","A","E","E","E","A","A","A","G","G","G","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","" ,"E","E","" ,"E","E","E","E","E","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" , "A"],
        ["A","A","A","A","A","A","G","G","G","E","E","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"G","G","G","" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","E","" ,"" ,"E","E","E","E","E","E","A"],
        ["A","" ,"G","G","G","G","" ,"" ,"G","G","G","A"],
        ["A","G","G","G","" ,"" ,"" ,"G","G","" ,"" ,"A"],
        ["A","A","A","A","A","A","G","A","A","A","A","A"]]

def aleatorio(valor):
    return randint(0,valor)


posAtual = [19 , 6]
pokedex = {}


def menu():
    print('  Bem-vindo!  ')
    print('A qualquer momento você pode escolher uma das opções: ')
    print('9 - Para abrir esse menu')
    print('8 - Subir')
    print('2 - Descer')
    print('4 - Ir para esquerda')
    print('6 - Ir para direta')
    print('5 - Abrir Pokedex')
    print('0 - Sair do Jogo')


def grama(): #Quando o personagem for pra grama
    pokemons = ['Ratata', 'Pidgey', 'Weedle', 'Caterpie', 'Paras', 'Charmander', 'Bulbasaur', 'Squirtle', 'Pikachu' , 'Evee']
    alea = aleatorio(1)
    if alea == 0:
        n = validacao('Um pokemon selvagem apareceu!\nCapturar ou correr?\n[1-Capturar ou 2-Correr]', [1, 2], 1)
        if n == 1:
            sorteio = aleatorio(9)
            if pokemons[sorteio] not in pokedex:
                pokedex[pokemons[sorteio]]  = {'HP': aleatorio(100),
                                               'Atk': aleatorio(100),
                                               'Def': aleatorio(100),
                                               'Sp.': aleatorio(100)
                                               }
            else:
                print('Esse pokemon já está na sua pokedex')
                print('Sua posição atual: ', posAtual)
        elif n == 2:
            print('Fujão')

    elif alea == 1:
        pass


def validacao(txt, valPossiveis, tipo):
    if tipo == 1: #Resposta é um número no tipo 1
        var = int(input(txt))
        while var not in valPossiveis:
            var = int(input(f'[Valor inválido] {txt}'))
    elif tipo == 2: #Resposta é um texto no tipo 2
        var = input(txt)
        while var not in valPossiveis:
            var = input(f'[Valor inválido] {txt}')
    return var
    

def mochila():
    while True:
        dig = validacao('Digite\n1 para Listar Detalhes\n2 para Apagar Registro\n0 para voltar ao menu principal\nEscolha uma ação: ', [1, 2, 0], 1)
        if dig == 0:
            menu()
            break
        elif dig == 1:
            print(pokedex)
        elif dig == 2:
            print(pokedex)
            r = validacao('Qual pokemon deseja excluir? ', pokedex ,2)
            del pokedex[r]


def move(): #Movimentos do personagem
    opc = validacao('Escolha sua opção: ', [8, 2, 4, 6, 5, 0, 9], 1)
    global cont

    if opc == 8:
        posAtual[0] -= 1
        if posAtual[0] == -1:
            return False
        elif mapa[posAtual[0]][posAtual[1]] == 'A':
            print('Bump!')
            posAtual[0] += 1
        elif mapa[posAtual[0]][posAtual[1]] == 'G':
            grama()
        elif mapa[posAtual[0]][posAtual[1]] == 'E':
            print('Bump!')
            posAtual[0] += 1

    elif opc == 2:
        posAtual[0] += 1
        if posAtual[0] == 20:
            return False
        elif mapa[posAtual[0]][posAtual[1]] == 'A':
            print('Bump!')
            posAtual[0] -= 1
        elif mapa[posAtual[0]][posAtual[1]] == 'G':
            grama()
        elif mapa[posAtual[0]][posAtual[1]] == 'E':
            posAtual[0] += 1

    elif opc == 4:
        posAtual[1] -= 1
        if  mapa[posAtual[0]][posAtual[1]] == 'A':
            print('Bump!')
            posAtual[1] += 1
        elif mapa[posAtual[0]][posAtual[1]] == 'G':
            grama()
        elif mapa[posAtual[0]][posAtual[1]] == 'E':
            print('Bump!')
            posAtual[1] += 1

    elif opc == 5:
        mochila()

    elif opc == 6:
        posAtual[1] += 1
        if mapa[posAtual[0]][posAtual[1]] == 'A':
            print('Bump!')
            posAtual[1] -= 1
        elif mapa[posAtual[0]][posAtual[1]] == 'G':
            grama()
        elif mapa[posAtual[0]][posAtual[1]] == 'E':
            print('Bump!')
            posAtual[1] -= 1

    elif opc == 0:
        return False
        
    return True


cont = True
print(mapa)
menu()
print('Entrando na rota 1')
while (cont == True):
    if len(pokedex) == 10:
        print('Parabéns! Você completou a pokedex')
    print('Sua posição atual: ', posAtual)
    cont = move()
