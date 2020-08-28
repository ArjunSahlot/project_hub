import home, visualizers, games
import os
import pygame

FPS = 30

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arjun Sahlot's Project Hub -- Home")
HOME_ICON = pygame.image.load(os.path.join("assets", "home_icon.png"))
pygame.display.set_icon(pygame.transform.scale(HOME_ICON, (32, 32)))

GAME_IMGS = [pygame.image.load(os.path.join("assets", "chess.png")), pygame.image.load(os.path.join("assets", "pong.png")), pygame.image.load(os.path.join("assets", "hangman.png")), pygame.image.load(os.path.join("assets", "sudoku.png"))]
VIS_IMGS = [pygame.image.load(os.path.join("assets", "search.png")), pygame.image.load(os.path.join("assets", "sort.png")), pygame.image.load(os.path.join("assets", "paint.png"))]


if home.main(WINDOW, WIDTH, HEIGHT, FPS) == "vis":
    pygame.display.set_caption("Arjun Sahlot's Project Hub -- Visualizers")
    pygame.display.set_icon(pygame.image.load(os.path.join("assets", "vis_icon.png")))
    click_in_vis = visualizers.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON, VIS_IMGS)
    if click_in_vis == "home":
        if home.main(WINDOW, WIDTH, HEIGHT, FPS) == "vis":
            pygame.display.set_caption("Arjun Sahlot's Project Hub -- Visualizers")
            pygame.display.set_icon(pygame.image.load(os.path.join("assets", "vis_icon.png")))
            visualizers.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON, VIS_IMGS)

        else:
            pygame.display.set_caption("Arjun Sahlot's Project Hub -- Games")
            pygame.display.set_icon(pygame.image.load(os.path.join("assets", "game_icon.png")))
            games.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON, GAME_IMGS)

    elif click_in_vis == "search":
        from project_files.Algorithm_Visualizer import AlgorithmVisualizer

    elif click_in_vis == "sort":
        pygame.display.set_icon(pygame.image.load(os.path.join("project_files", "Sorting_Visualizer", "assets", "icon.png")))
        from project_files.Sorting_Visualizer import SortingVisualizer

    else:
        pygame.display.set_icon(pygame.image.load(os.path.join("project_files", "Painter", "assets", "icon.png")))
        ERASER = pygame.transform.scale(pygame.image.load(os.path.join("project_files", "Painter", "assets", "eraser_icon.png")),(70, 70))
        CLEAR = pygame.transform.scale(pygame.image.load(os.path.join("project_files", "Painter", "assets", "clear_screen.png")),(70 - 14, 70 - 14))
        PICKER = pygame.transform.scale(pygame.image.load(os.path.join("project_files", "Painter", "assets", "color_picker.png")), (170, 170))
        from project_files.Painter import paint
        paint.main(pygame.display.set_mode((1000, 1000)), 1000, 1000, ERASER, CLEAR, PICKER)


else:
    pygame.display.set_caption("Arjun Sahlot's Project Hub -- Games")
    pygame.display.set_icon(pygame.image.load(os.path.join("assets", "game_icon.png")))
    if games.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON, GAME_IMGS) == "home":
        if home.main(WINDOW, WIDTH, HEIGHT, FPS) == "vis":
            pygame.display.set_caption("Arjun Sahlot's Project Hub -- Visualizers")
            pygame.display.set_icon(pygame.image.load(os.path.join("assets", "vis_icon.png")))
            visualizers.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON, VIS_IMGS)

        else:
            pygame.display.set_caption("Arjun Sahlot's Project Hub -- Games")
            pygame.display.set_icon(pygame.image.load(os.path.join("assets", "game_icon.png")))
            games.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON, GAME_IMGS)

