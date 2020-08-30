import os

import games
import home
import pygame
import visualizers
import login

FPS = 30

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


GAME_IMGS = [pygame.image.load(os.path.join("assets", "chess.png")),
             pygame.image.load(os.path.join("assets", "pong.png")),
             pygame.image.load(os.path.join("assets", "hangman.png")),
             pygame.image.load(os.path.join("assets", "sudoku.png"))]
VIS_IMGS = [pygame.image.load(os.path.join("assets", "search.png")),
            pygame.image.load(os.path.join("assets", "sort.png")),
            pygame.image.load(os.path.join("assets", "paint.png"))]

pygame.display.set_caption("Project Hub -- Login")
pygame.display.set_icon(pygame.image.load(os.path.join("assets", "login_icon.png")))


if login.main(WINDOW, WIDTH, HEIGHT, FPS) == "pass":
    pygame.display.set_caption("Project Hub -- Home")
    HOME_ICON = pygame.image.load(os.path.join("assets", "home_icon.png"))
    pygame.display.set_icon(pygame.transform.scale(HOME_ICON, (32, 32)))
    if home.main(WINDOW, WIDTH, HEIGHT, FPS) == "vis":
        pygame.display.set_caption("Project Hub -- Visualizers")
        pygame.display.set_icon(pygame.image.load(os.path.join("assets", "vis_icon.png")))
        click_in_vis = visualizers.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON, VIS_IMGS)
        if click_in_vis == "home":
            pygame.display.set_caption("Project Hub -- Home")
            HOME_ICON = pygame.image.load(os.path.join("assets", "home_icon.png"))
            pygame.display.set_icon(pygame.transform.scale(HOME_ICON, (32, 32)))
            if home.main(WINDOW, WIDTH, HEIGHT, FPS) == "vis":
                pygame.display.set_caption("Project Hub -- Visualizers")
                pygame.display.set_icon(pygame.image.load(os.path.join("assets", "vis_icon.png")))
                visualizers.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON, VIS_IMGS)

            else:
                pygame.display.set_caption("Project Hub -- Games")
                pygame.display.set_icon(pygame.image.load(os.path.join("assets", "game_icon.png")))
                games.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON, GAME_IMGS)

        elif click_in_vis == "search":
            from project_files.Algorithm_Visualizer import AlgorithmVisualizer

        elif click_in_vis == "sort":
            from project_files.Sorting_Visualizer import SortingVisualizer

        else:
            from project_files.Painter import paint


    else:
        pygame.display.set_caption("Project Hub -- Games")
        pygame.display.set_icon(pygame.image.load(os.path.join("assets", "game_icon.png")))
        click_in_games = games.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON, GAME_IMGS)
        if click_in_games == "home":
            pygame.display.set_caption("Project Hub -- Home")
            HOME_ICON = pygame.image.load(os.path.join("assets", "home_icon.png"))
            pygame.display.set_icon(pygame.transform.scale(HOME_ICON, (32, 32)))
            if home.main(WINDOW, WIDTH, HEIGHT, FPS) == "vis":
                pygame.display.set_caption("Project Hub -- Visualizers")
                pygame.display.set_icon(pygame.image.load(os.path.join("assets", "vis_icon.png")))
                visualizers.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON, VIS_IMGS)

            else:
                pygame.display.set_caption("Project Hub -- Games")
                pygame.display.set_icon(pygame.image.load(os.path.join("assets", "game_icon.png")))
                games.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON, GAME_IMGS)

        elif click_in_games == "chess":
            from project_files.Chess import game

        elif click_in_games == "pong":
            from project_files.Pong import game

        elif click_in_games == "hangman":
            from project_files.Hangman import game

        else:
            from project_files.Sudoku import game
