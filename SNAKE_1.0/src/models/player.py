'''
    DECLARACAO DE OBJETOS

    Jogador composto (snake = cabeca + corpo + cauda): em desenvolvimento
'''

#CLASSE AUXILIAR DA CLASSE PRINCIPAL: SNAKE
class SnakePart():
    '''
        Inicializando atributos da parte do corpo da cobra, onde:
        tipo = "head" -> parte do corpo sera tratada como a cabeca da cobra 
        tipo = "body" -> parte do corpo sera tratada igual a um segmento do corpo da cobra
        tipo = "tail" -> parte do corpo sera tratada como a cauda da cobra

        Toda parte do corpo tera um atributo direcao, onde os possiveis valores serao:
        tipo = "head" -> 'w', 'a', 's', 'd'
        tipo = "body/tail" -> 'w', 'wa', 'aw', 'a', 'as', 'sa', 's', 'sd', 'ds', 'd', 'dw', 'wd'
        Esses valores servirao de referencia para a correta renderizacao dos sprites de movimento
        da cobra e tambem para o futuro deslocamento dos segmentos

        Toda parte do corpo tambem tera um atributo frente e um atributo costa, onde:
        frente = numero inteiro referente ao indice da parte do corpo no vetor corpo do jogador Snake
        costa = numero inteiro referente ao indice da parte do corpo no vetor corpo do jogador Snake
        OBS: -1 significa que a parte do corpo nao tem outra parte nessa posicao (seja frente ou costa)

        Exemplo: corpo do jogador cobra tem 1 cabeca, 1 corpo e 1 cauda. Suas partes estarao inicializadas como:
        corpo = [ [8, 24, "head", "s", -1, 1 ], [8, 16, "body", "s", 0, 2 ], [8, 8, "tail", "s", 1, -1 ] ]
    '''
    def __init__(self, posX, posY, tipo, direcao, frente=-1, costa=-1):
        self.posX = posX
        self.posY = posY
        self.tipo = tipo
        self.direcao = direcao
        self.frente = frente
        self.costa = costa

#CLASSE PRINCIPAL DO JOGADOR TIPO SNAKE
class Snake:
    #declarando flag de controle para uso na movimentacao
    movimentoValido = [False, 's']
    #inicializacao dos atributos
    def __init__(self, posX, posY, imgBank, pixelX, pixelY, largura, altura, Dx=8, vidas=3, pontos=0):
        self.posX = posX
        self.posY = posY
        self.imgBank = imgBank
        self.pixelX = pixelX
        self.pixelY = pixelY
        self.largura = largura
        self.altura = altura
        self.Dx = Dx #quantidade de pixels movidos por frame
        self.vidas = vidas #quantidade inicial de vidas do jogador 
        self.pontos = pontos #quantidade inicial de pontos do jogador
        self.dirAtual = 's' #flag usada para saber em que direcao a cobra esta se movendo (padrao = para baixo)
        self.corpo = [] #vetor corpo onde serao guardadas as partes da cobra para movimentacao pelo mapa
        #criando partes iniciais da cobra (cabeca e cauda) conforme posicao inicial do jogador no mapa
        cabeca = SnakePart(self.posX, self.posY, "head", self.dirAtual, -1, 1)
        cauda = SnakePart(self.posX, self.posY-8, "tail", self.dirAtual, 0, -1)
        #adicionando partes iniciais da cobra no seu vetor corpo
        self.corpo.append(cabeca)
        self.corpo.append(cauda)

    def move(self, direcao, larguraJanela, alturaJanela):
        '''
            Usando item 0 do vetor corpo (a cabeca da cobra) como referencial para verificar se o
            movimento do jogador eh valido (se ha espaco para mover)
            Ao validar espaco disponivel para mover, devemos atualizar as posicoes e direcoes de cada
            um dos segmentos do corpo da cobra (se orientando pelas referencias da frente e da costa)
        '''
        self.movimentoValido[0] = False
        #checando direcao escolhida e se eh possivel (dentro da janela do jogo)
        if (direcao == 'w' and (self.corpo[0].posY-self.Dx) >= 0):
            self.movimentoValido[0] = True
            self.movimentoValido[1] = 'w'
        elif (direcao == 'a' and (self.corpo[0].posX-self.Dx) >= 0):
            self.movimentoValido[0] = True
            self.movimentoValido[1] = 'a'
        elif (direcao == 's' and (self.corpo[0].posY+self.Dx) <= (alturaJanela-self.altura)):
            self.movimentoValido[0] = True
            self.movimentoValido[1] = 's'
        elif (direcao == 'd' and (self.corpo[0].posX+self.Dx) <= (larguraJanela-self.largura)):
            self.movimentoValido[0] = True
            self.movimentoValido[1] = 'd'
        #no caso do movimento ser valido, atualizar posicao e direcao de todos os segmentos do corpo com base na cabeca
        if (self.movimentoValido[0]):
            for parte in reversed(self.corpo):
                #atualizando elemento do fim ao inicio (cabeca sera a ultima)
                if (parte.frente != -1):
                    #atualizando posicao atual de acordo com direcao do segmento da frente
                    if (self.corpo[parte.frente].direcao == 'w'):
                        parte.posY -= self.Dx
                    elif (self.corpo[parte.frente].direcao == 'wa'):
                        parte.posY -= self.Dx
                    elif (self.corpo[parte.frente].direcao == 'aw'):
                        parte.posX -= self.Dx
                    elif (self.corpo[parte.frente].direcao == 'a'):
                        parte.posX -= self.Dx
                    elif (self.corpo[parte.frente].direcao == 'as'):
                        parte.posX -= self.Dx
                    elif (self.corpo[parte.frente].direcao == 'sa'):
                        parte.posY += self.Dx
                    elif (self.corpo[parte.frente].direcao == 's'):
                        parte.posY += self.Dx
                    elif (self.corpo[parte.frente].direcao == 'sd'):
                        parte.posY += self.Dx
                    elif (self.corpo[parte.frente].direcao == 'ds'):
                        parte.posX += self.Dx
                    elif (self.corpo[parte.frente].direcao == 'd'):
                        parte.posX += self.Dx
                    elif (self.corpo[parte.frente].direcao == 'dw'):
                        parte.posX += self.Dx
                    elif (self.corpo[parte.frente].direcao == 'wd'):
                        parte.posY -= self.Dx
                    parte.direcao = self.corpo[parte.frente].direcao #atualizando direcao
                else:
                    if (self.movimentoValido[1] == 'w'):
                        parte.posY -= self.Dx
                        parte.direcao = 'w'
                        #atualizando parte do corpo logo depois da cabeca de acordo com as possibilidades
                        if (self.corpo[parte.costa].direcao == 'w'):
                            self.corpo[parte.costa].direcao = 'w'
                        elif (self.corpo[parte.costa].direcao == 'a'):
                            self.corpo[parte.costa].direcao = 'aw'
                        elif (self.corpo[parte.costa].direcao == 'd'):
                            self.corpo[parte.costa].direcao = 'dw'
                    elif (self.movimentoValido[1] == 'a'):
                        parte.posX -= self.Dx
                        parte.direcao = 'a'
                        #atualizando parte do corpo logo depois da cabeca de acordo com as possibilidades
                        if (self.corpo[parte.costa].direcao == 'w'):
                            self.corpo[parte.costa].direcao = 'wa'
                        elif (self.corpo[parte.costa].direcao == 'a'):
                            self.corpo[parte.costa].direcao = 'a'
                        elif (self.corpo[parte.costa].direcao == 's'):
                            self.corpo[parte.costa].direcao = 'sa'
                    elif (self.movimentoValido[1] == 's'):
                        parte.posY += self.Dx
                        parte.direcao = 's'
                        #atualizando parte do corpo logo depois da cabeca de acordo com as possibilidades
                        if (self.corpo[parte.costa].direcao == 'a'):
                            self.corpo[parte.costa].direcao = 'as'
                        elif (self.corpo[parte.costa].direcao == 's'):
                            self.corpo[parte.costa].direcao = 's'
                        elif (self.corpo[parte.costa].direcao == 'd'):
                            self.corpo[parte.costa].direcao = 'ds'
                    elif (self.movimentoValido[1] == 'd'):
                        parte.posX += self.Dx
                        parte.direcao = 'd'
                        #atualizando parte do corpo logo depois da cabeca de acordo com as possibilidades
                        if (self.corpo[parte.costa].direcao == 'w'):
                            self.corpo[parte.costa].direcao = 'wd'
                        elif (self.corpo[parte.costa].direcao == 's'):
                            self.corpo[parte.costa].direcao = 'sd'
                        elif (self.corpo[parte.costa].direcao == 'd'):
                            self.corpo[parte.costa].direcao = 'd'
                                          
             
