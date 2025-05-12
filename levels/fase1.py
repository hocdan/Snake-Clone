'''

    LEVEL 1 - arquivo que carrega a primeira fase do jogo 
'''

from models.world import *
from models.player import *
from levels import State
import pyxel
import random

#declarando constantes
LARGURA_JANELA = 128
ALTURA_JANELA = 137 #onde 128 pixels sao dedicados ao jogo e 9 pixels as informacoes do jogador (vida e pontos)
TAMANHO = 8 #referencia das dimensoes em pixels dos sprites no tilemap

#CODIGO PRINCIPAL
class Fase1(State):

    def onEnter(self, game):
        pyxel.mouse(True)
        pyxel.load("Assets/snake.pyxres")
        #carregando fonte das letras
        self.fonte = pyxel.Font("Assets/Fonts/VictoriaBold-8.bdf")

        #carregando componentes do jogo (mundo e jogador)
        self.player = Snake(8, 24, 0, 16, 0, 8, 8, 8, vidas=5, pontos=100)
        self.world = World_SNAKE(pyxel.tilemaps[0], 16, 16, 8, self.player)
        self.INPUT = 's' #flag de controle para a direcao passiva da cobra
        self.GAME_OVER = False 

    def update(self, game):
        #checando se jogador ja utilizou todas as vidas ao jogar
        if (self.player.vidas <= 0):
            self.GAME_OVER = True
        if (not self.GAME_OVER):
            #checando constantemente input do usuario, caso jogo nao tenha finalizado
            if (pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP)):
                self.INPUT = 'w'
            elif (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)):
                self.INPUT = 'a'
            elif (pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)):
                self.INPUT = 's'
            elif (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)):
                self.INPUT = 'd'
            #checando movimentos invalidos e nao deixando valor ser repassado na atualizacao
            if ( self.world.checkCollision(self.INPUT) == "invalido"):
                self.INPUT = self.world.SNAKE.corpo[0].direcao #restaurando direcao valida
            #atualizando mudanca de movimento a cada 0.5 segundos
            if (pyxel.frame_count%20 == 0):
                if ( self.world.checkCollision(self.INPUT) == "comida"):
                    self.world.grow()
                    if (self.world.checkCollision(self.INPUT) not in ["tijolo", "caixa", "corpo", "gelo", "invalido"]):
                        self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "fogo"):
                    self.player.vidas -= 1
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "vida"):
                    self.player.vidas += 1
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "moeda"):
                    self.player.pontos += 500
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "cristal"):
                    self.player.pontos += 2000
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) not in ["tijolo", "caixa", "corpo", "gelo", "invalido"]):
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) in ["tijolo", "caixa", "corpo", "gelo"] ):
                    self.player.vidas -= 1
        else:
            #checando se usuario ira querer reiniciar jogo
            if (pyxel.btn(pyxel.KEY_R) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_A)):
                #carregando componentes do jogo (mundo e jogador)
                self.player = Snake(8, 24, 0, 16, 0, 8, 8, 8, vidas=3, pontos=0)
                self.world = World_SNAKE(pyxel.tilemaps[0], 16, 16, 8, self.player)
                self.INPUT = 's' #flag de controle para a direcao passiva da cobra
                self.GAME_OVER = False 
            elif (pyxel.btn(pyxel.KEY_M) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_B)):
                #devolvendo controle para carregar arquivo "menu.py"
                return "menu"
        #chance de gerar comidas randomicas a cada 10 segundos em locais vazios do mapa
        if (pyxel.frame_count%320 == 0):
            posXrandom = random.randint(0, 127)
            posYrandom = random.randint(0, 127)
            self.world.addItem(posXrandom, posYrandom, WorldItem_SNAKE.COMIDA)

    def draw(self, game):
        pyxel.cls(0)
        if (not self.GAME_OVER):
            self.world.loadSnakeOnTilemap() #atualizando valores do jogador no tilemap
            #desenhando mapa
            for y in range(self.world.ALTURA):
                for x in range(self.world.LARGURA):
                    worldItem = self.world.world_map[y][x]
                    self.world.draw_worldItens(pyxel, x, y, 0, worldItem)
            #desenhando informacoes do jogador (pontuacao e vidas)
            pyxel.text(80, 130, "POINTS:{}".format(self.player.pontos), pyxel.COLOR_WHITE)
            pyxel.text(2, 130, "LIFE: ", pyxel.COLOR_WHITE)
            for vidas in range(self.player.vidas):
                if (vidas == 5):
                    pyxel.text(71, 129, "+{}".format(self.player.vidas-vidas), pyxel.COLOR_WHITE) #finalizando impressao de coracoes caso > 5
                    break
                pyxel.blt(21+(vidas*10), 128, 0, 32, 16, 8, 8) #desenhando icones de coracao
            
        else:
            #desenhando tela de fim de jogo
            pyxel.rectb(26, 10, 77, 11, pyxel.COLOR_WHITE) #desenhando bordas do quadro game over
            pyxel.text(28, 12, "GAME OVER", pyxel.COLOR_WHITE, self.fonte)
            pyxel.rectb(5, 35, 118, 30, pyxel.COLOR_WHITE) #desenhando bordas do quadro de status do jogador
            pyxel.text(10, 40, "You scored {} points!".format(self.player.pontos), pyxel.COLOR_WHITE)
            pyxel.text(10, 55, "Your lenght was: {} meters!".format(len(self.player.corpo)), pyxel.COLOR_WHITE)
            pyxel.text(8, 91, "> Press R to restart game", pyxel.COLOR_WHITE)
            pyxel.text(8, 101, "> Press M to go back to menu", pyxel.COLOR_WHITE)
            pyxel.text(8, 111, "> Press ESC to exit game", pyxel.COLOR_WHITE)
            pyxel.text(16, 126, "A game made by Daniel SG", pyxel.COLOR_WHITE) #creditos
            pyxel.line(13, 133, 113, 133, pyxel.COLOR_WHITE)
            #desenhando decoracoes da tela de game over
            pyxel.blt(5, 10, 0, 0, 24, 8, 8) #desenhando tijolo 1
            pyxel.blt(5, 18, 0, 0, 24, 8, 8) #desenhando tijolo 2
            pyxel.blt(13, 18, 0, 16, 16, 8, 8) #desenhando moeda
            pyxel.blt(115, 10, 0, 8, 24, 8, 8) #desenhando caixa 1
            pyxel.blt(115, 18, 0, 8, 24, 8, 8) #desenhando caixa 2
            pyxel.blt(107, 18, 0, 24, 16, 8, 8) #desenhando cristal
            pyxel.blt(35, 75, 0, 0, 0, 8, 8) #cabeca virada para a esquerda
            for i in range(6):
                pyxel.blt(43+(i*8), 75, 0, 0, 8, 8, 8) #6 segmentos de corpo virado para a esquerda
            pyxel.blt(91, 75, 0, 72, 0, 8, 8) #rabo virado para a esquerda
            pyxel.blt(13, 75, 0, 0, 16, 8, 8) #desenhando comida
            pyxel.blt(110, 75, 0, 24, 24, 8, 8) #desenhando fogo
