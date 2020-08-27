import home, visualizers, games
import os
import pygame

FPS = 30

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arjun Sahlot's Project Hub -- Home")
HOME_ICON = pygame.image.load(os.path.join("assets", "home_icon.png"))
pygame.display.set_icon(pygame.transform.scale(HOME_ICON, (32, 32)))

if home.main(WINDOW, WIDTH, HEIGHT, FPS) == "vis":
    pygame.display.set_caption("Arjun Sahlot's Project Hub -- Visualizers")
    pygame.display.set_icon(pygame.image.load(os.path.join("assets", "vis_icon.png")))
    if visualizers.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON) == "home":
        if home.main(WINDOW, WIDTH, HEIGHT, FPS) == "vis":
            pygame.display.set_caption("Arjun Sahlot's Project Hub -- Visualizers")
            pygame.display.set_icon(pygame.image.load(os.path.join("assets", "vis_icon.png")))
            visualizers.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON) == "home"

        else:
            pygame.display.set_caption("Arjun Sahlot's Project Hub -- Games")
            pygame.display.set_icon(pygame.image.load(os.path.join("assets", "game_icon.png")))
            games.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON) == "home"


else:
    pygame.display.set_caption("Arjun Sahlot's Project Hub -- Games")
    pygame.display.set_icon(pygame.image.load(os.path.join("assets", "game_icon.png")))
    if games.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON) == "home":
        if home.main(WINDOW, WIDTH, HEIGHT, FPS) == "vis":
            pygame.display.set_caption("Arjun Sahlot's Project Hub -- Visualizers")
            pygame.display.set_icon(pygame.image.load(os.path.join("assets", "vis_icon.png")))
            visualizers.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON) == "home"

        else:
            pygame.display.set_caption("Arjun Sahlot's Project Hub -- Games")
            pygame.display.set_icon(pygame.image.load(os.path.join("assets", "game_icon.png")))
            games.main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON) == "home"

