import pygame, os

import home, visualizers, games

HOME_FPS = 30

HOME_WIDTH, HOME_HEIGHT = 1000, 800
HOME_WINDOW = pygame.display.set_mode((HOME_WIDTH, HOME_HEIGHT))
pygame.display.set_caption("Arjun Sahlot's Project Hub -- Home")
pygame.display.set_icon(pygame.image.load(os.path.join("assets", "home_icon.png")))


home.main(HOME_WINDOW, HOME_WIDTH, HOME_HEIGHT, HOME_FPS)

# if home.main(HOME_WINDOW, HOME_WIDTH, HOME_HEIGHT, HOME_FPS) == "vis":
#     visualizers.main()
# else:
#     games.main()
