'''

    PROGRAMA AUXILIAR RESPONSAVEL POR MOSTRAR A TELA TUTORIAL DO JOGO SNAKE 1.0

    -> Conta com 1 opcao:

    1. Voltar (inicia o menu)
'''

from models import utilities, world
from levels import State
import pyxel

#CODIGO PRINCIPAL
class Tutorial(State):

    def __init__(self):
        #inicializando janela
        pyxel.mouse(True)
        #carregando icones do jogo
        pyxel.load("Assets/snake.pyxres")

        #declarando e inicializando retangulos do tutorial (bordas dos icones por categoria)
        self.rectangles = [[15, 15, 26, 26, pyxel.COLOR_GRAY, False],
                           [15, 46, 26, 10, pyxel.COLOR_GRAY, False],
                           [22, 62, 10, 26, pyxel.COLOR_GRAY, False],
                           [15, 94, 18, 10, pyxel.COLOR_GRAY, False]]

        #declarando tilemap para decoracao da tela tutorial
        self.decoration = world.World_SNAKE(pyxel.tilemaps[1], 16, 17, 8)

    def update(self, game):
        #checando se usuario deseja voltar ao menu
        if (pyxel.btn(pyxel.KEY_M) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_B)):
            return "menu"

    def draw(self, game):
        pyxel.cls(0) #limpando tela
        #desenhando retangulos do tutorial
        for x in range(4):
            pyxel.rect(self.rectangles[x][0], self.rectangles[x][1], self.rectangles[x][2], self.rectangles[x][3], self.rectangles[x][4])
        #desenhando tilemap
        for y in range(self.decoration.ALTURA):
            for x in range(self.decoration.LARGURA):
                worldItem = self.decoration.world_map[y][x]
                self.decoration.draw_worldItens(pyxel, x, y, 0, worldItem)
        #desenhando legendas dos itens
        pyxel.text(61, 21, "W, A, S, D", pyxel.COLOR_WHITE)
        pyxel.text(66, 29, "to move", pyxel.COLOR_WHITE)
        pyxel.text(63, 50, "Obstacles", pyxel.COLOR_WHITE)
        pyxel.text(58, 66, "Food (grow)", pyxel.COLOR_WHITE)
        pyxel.text(58, 74, "Life (get)", pyxel.COLOR_WHITE)
        pyxel.text(58, 82, "Fire (avoid)", pyxel.COLOR_WHITE)
        pyxel.text(58, 98, "Points (get)", pyxel.COLOR_WHITE)
        pyxel.text(25, 113, "<- Press M to return", pyxel.COLOR_WHITE)
        
