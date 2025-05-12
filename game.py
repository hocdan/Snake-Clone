import pyxel
from levels.menu import Menu
from levels.fase1 import Fase1
from levels.tutorial import Tutorial

class Game:
    def __init__(self):
        pyxel.init(128, 136, "SNAKE 1.0", fps=60)
        self.states = {
            "menu": Menu(),
            "fase1": Fase1(),
            "tutorial": Tutorial()
        }
        self.currentState = self.states["menu"]
        self.currentState.onEnter(self)
        pyxel.run(self.update, self.draw)
    
    def changeState(self, stateName):
        self.currentState.onExit(self)
        self.currentState = self.states[stateName]
        self.currentState.onEnter(self)

    def update(self):
        nextState = self.currentState.update(self)
        if nextState:
            self.changeState(nextState)
    
    def draw(self):
        self.currentState.draw(self)