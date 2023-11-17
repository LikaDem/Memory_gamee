import sys
from tkinter import Toplevel, Tk, IntVar, Radiobutton, Button
import pygame
from random import shuffle

root = Tk()

top = Toplevel()

top.title('Memory game')
top.geometry('400x300+550+300')
top.resizable(False, False)

var = IntVar()
Radiobutton(top, text='Легкая', variable=var, value=0).pack()
Radiobutton(top, text='Средняя', variable=var, value=2).pack()
Radiobutton(top, text='Сложная', variable=var, value=1).pack()
button1 = Button(top, text="Войти", command=lambda: command1()).pack()
button2 = Button(top, text="Выйти", command=lambda: command2()).pack()
class Window():
    def __init__(self, weight, hight, name):
        self._weight = weight
        self._hight = hight
        self._name = name
    def screen(self):
        return pygame.display.set_mode((self._weight, self._hight))
    def title(self):
        return pygame.display.set_caption(self._name)

class Game():
    def __init__(self, weight, hight):
        self._weight = weight
        self._hight = hight
    def posiz(self):
        position = []
        for i in range(6):
            for j in range(2):
                center_x = ((self._weight / 6) * (i + 2.5)) - (self._weight / 12)
                center_y = ((self._hight / 3) * (j + 1)) - (self._hight / 6)
                position.append(([center_x, center_y]))
        return position
    def posiz1(self):
        position = []
        for i in range(6):
            for j in range(2):
                center_x = ((self._weight / 6) * (i + 1)) - (self._weight / 12)
                center_y = ((self._hight / 3) * (j + 1)) - (self._hight / 6)
                position.append(([center_x, center_y]))
        return position
    def pozis2(self):
        position = []
        for i in range(6):
            for j in range(2):
                center_x = ((self._weight / 6) * (i + 2)) - (self._weight / 12)
                center_y = ((self._hight / 3) * (j + 1)) - (self._weight / 12)
                position.append(([center_x, center_y]))
        return position

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

def command1():

    brown = (100, 40, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    pink = (255, 100, 180)
    white = (192, 192, 192)

    screen_w = 800
    screen_h = 600

    root.deiconify()
    top.destroy()
    root.withdraw()

    if var.get() == 0:

        pygame.init()

        screen = Window(screen_w, screen_h, 'Визуальная память')
        window = screen.screen()
        screen.title()
        radius = 55
        colors = [red, blue, green]
        pairs = colors * 2
        shuffle(pairs)

        game = Game(screen_w, screen_h)
        positions = game.posiz()

        original_colors = pairs.copy()

        for i in range(len(pairs)):
            position = positions[i]
            color = pairs[i]
            pygame.draw.circle(window, color, position, radius)

        font = pygame.font.SysFont('Arial', 20)
        pygame.display.update()
        pygame.time.wait(3000)

        for i in range(len(pairs)):
            position = positions[i]
            pygame.draw.circle(window, white, position, radius)

        pygame.display.update()
        uncovered = []
        last_uncovered = None
        record = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = event.pos
                    for i in range(len(positions)):
                        position = positions[i]
                        if ((position[0] - mouse[0]) ** 2 + (position[1] - mouse[1]) ** 2) ** 0.5 < radius:
                            if i not in uncovered:
                                uncovered.append(i)
                                color = original_colors[i]
                                pygame.draw.circle(window, color, position, radius)
                                pygame.display.update()
                                if last_uncovered is not None and original_colors[last_uncovered] == original_colors[i]:
                                    record += 1
                                last_uncovered = i

                    if len(uncovered) == len(pairs):
                        final_score = font.render(f"Игра завершена", True, red)
                        final_score1 = font.render(f"Уровень памяти: {str(record)} из 3", True, white)
                        final = Final(final_score, final_score1, screen_w, screen_h, window)
                        final.final()

    elif var.get() == 2:
        pygame.init()

        screen = Window(screen_w, screen_h, 'Визуальная память')
        window = screen.screen()
        screen.title()

        radius = 52
        colors = [red, blue, green, yellow]
        pairs = colors * 2
        shuffle(pairs)

        game = Game(screen_w, screen_h)
        positions = game.pozis2()

        original_colors = pairs.copy()

        for i in range(len(pairs)):
            position = positions[i]
            color = pairs[i]
            pygame.draw.circle(window, color, position, radius)

        font = pygame.font.SysFont('Arial', 20)
        pygame.display.update()
        pygame.time.wait(5000)

        for i in range(len(pairs)):
            position = positions[i]
            pygame.draw.circle(window, white, position, radius)

        pygame.display.update()
        uncovered = []
        last_uncovered = None
        record = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = event.pos
                    for i in range(len(positions)):
                        position = positions[i]
                        if ((position[0] - mouse[0]) ** 2 + (position[1] - mouse[1]) ** 2) ** 0.5 < radius:
                            if i not in uncovered:
                                uncovered.append(i)
                                color = original_colors[i]
                                pygame.draw.circle(window, color, position, radius)
                                pygame.display.update()
                                if last_uncovered is not None and original_colors[last_uncovered] == original_colors[i]:
                                    record += 1
                                last_uncovered = i

                    if len(uncovered) == len(pairs):
                        final_score = font.render(f"Игра завершена", True, red)
                        final_score1 = font.render(f"Уровень памяти: {str(record)} из 4", True, white)
                        final = Final(final_score, final_score1, screen_w, screen_h, window)
                        final.final()

    elif var.get() == 1:
        pygame.init()

        screen = Window(screen_w, screen_h, 'Визуальная память')
        window = screen.screen()
        screen.title()

        radius = 50
        colors = [red, blue, green, yellow, brown, pink]
        pairs = colors * 2
        shuffle(pairs)

        game = Game(screen_w, screen_h)
        positions = game.posiz1()

        original_colors = pairs.copy()

        for i in range(len(pairs)):
            position = positions[i]
            color = pairs[i]
            pygame.draw.circle(window, color, position, radius)

        font = pygame.font.SysFont('Arial', 20)
        pygame.display.update()
        pygame.time.wait(10000)

        for i in range(len(pairs)):
            position = positions[i]
            pygame.draw.circle(window, white, position, radius)

        pygame.display.update()
        uncovered = []
        last_uncovered = None
        record = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = event.pos
                    for i in range(len(positions)):
                        position = positions[i]
                        if ((position[0] - mouse[0]) ** 2 + (position[1] - mouse[1]) ** 2) ** 0.5 < radius:
                            if i not in uncovered:
                                uncovered.append(i)
                                color = original_colors[i]
                                pygame.draw.circle(window, color, position, radius)
                                pygame.display.update()
                                if last_uncovered is not None and original_colors[last_uncovered] == original_colors[i]:
                                    record += 1
                                last_uncovered = i

                    if len(uncovered) == len(pairs):
                        final_score = font.render(f"Игра завершена", True, red)
                        final_score1 = font.render(f"Уровень памяти: {str(record)} из 6", True, white)
                        final = Final(final_score, final_score1, screen_w, screen_h, window)
                        final.final()

def command2():
    top.destroy()
    root.destroy()
    sys.exit()

root.withdraw()
root.mainloop()
