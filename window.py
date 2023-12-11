import pygame

class Window():
    def __init__(self, weight, hight, name):
        self._weight = weight
        self._hight = hight
        self._name = name
    def screen(self):
        return pygame.display.set_mode((self._weight, self._hight))
    def title(self):
        return pygame.display.set_caption(self._name)
