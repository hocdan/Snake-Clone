'''
    COMPILADO DE FUNCOES UTEIS DIVERSAS

    - draw_text_with_border() -> desenha textos com fontes customizaveis com bordas coloridas nas letras

'''
import pyxel

def draw_text_with_border(x, y, s, col, bcol, font):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                pyxel.text(
                    x + dx,
                    y + dy,
                    s,
                    bcol, #valor para colorir a borda das letras
                    font, #arquivo da fonte para as letras
                )
    pyxel.text(x, y, s, col, font)

def checkPointOnRec(posX, posY, recX, recY, largura, altura):
    #checando se ponto de coordenada (X, Y) se encontra dentro de retangulo com as dimensoes passadas
    if ( posX >= recX and posX <= recX+largura and posY >= recY and posY <= recY+altura):
        return True
    else:
        return False