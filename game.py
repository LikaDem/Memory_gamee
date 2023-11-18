import sys
import pygame

from random import shuffle
from tkinter import Toplevel, Tk, IntVar, Radiobutton, Button

from window import Window
from game_logic import Game
from final import Final

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

red = (255, 0, 0)
white = (192, 192, 192)

def colour(i):
    brown = (100, 40, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    pink = (255, 100, 180)
    colours = [red, blue, green, yellow, brown, pink]
    return colours[:i]

def parametrs(i):
    if (i == 'w'):
        return 800
    elif (i == 'h'):
        return 600

def f():
    pygame.quit()
    exit()

def command1():

    root.deiconify()
    top.destroy()
    root.withdraw()

    if var.get() == 0:

        pygame.init()

        screen = Window(parametrs('w'), parametrs('h'), 'Визуальная память')
        window = screen.screen()
        screen.title()

        radius = 55
        colors = colour(3)
        pairs = colors * 2
        shuffle(pairs)

        game = Game(parametrs('w'), parametrs('h'))
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
                    f()

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
                        final = Final(final_score, final_score1, parametrs('w'), parametrs('h'), window)
                        final.final()

    elif var.get() == 2:
        pygame.init()

        screen = Window(parametrs('w'), parametrs('h'), 'Визуальная память')
        window = screen.screen()
        screen.title()

        radius = 52
        colors = colour(4)
        pairs = colors * 2
        shuffle(pairs)

        game = Game(parametrs('w'), parametrs('h'))
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
                    f()

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
                        final = Final(final_score, final_score1, parametrs('w'), parametrs('h'), window)
                        final.final()

    elif var.get() == 1:
        pygame.init()

        screen = Window(parametrs('w'), parametrs('h'), 'Визуальная память')
        window = screen.screen()
        screen.title()

        radius = 50
        colors = colour(6)
        pairs = colors * 2
        shuffle(pairs)

        game = Game(parametrs('w'), parametrs('h'))
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
                    f()

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
                        final = Final(final_score, final_score1, parametrs('w'), parametrs('h'), window)
                        final.final()

def command2():
    top.destroy()
    root.destroy()
    sys.exit()

root.withdraw()
root.mainloop()
