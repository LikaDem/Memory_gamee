import pygame

class Final():
    def __init__(self, final, final1, screen_w, screen_h, window):
        self._final = final
        self._final1 = final1
        self._screen_w = screen_w
        self._screen_h = screen_h
        self._window = window
    def final(self):
        self._window.blit(self._final, (self._screen_w // 2 - 70, self._screen_h // 2 + 100))
        self._window.blit(self._final1, (self._screen_w // 2 - 100, self._screen_h // 2 + 125))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        exit()
