import pygame

def draw_back_button(win, image):
    pygame.draw.line(win, (0, 0, 0), (10, 60), (70, 25), 5)
    pygame.draw.line(win, (0, 0, 0), (10, 60), (70, 95), 5)
    box = pygame.draw.rect(win, (0, 0, 0), (80, 10, 100, 100), 5)
    image = pygame.transform.scale(image, (80, 80))
    win.blit(image, (90, 20))

    return box
