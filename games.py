import back_button as button
import ball_background as ballbg
import os
import pygame

pygame.init()

pygame.display.set_caption("Project Hub -- Games")
pygame.display.set_icon(pygame.image.load(os.path.join("assets", "game_icon.png")))

HOME_ICON = pygame.image.load(os.path.join("assets", "home_icon.png"))

FPS = 30

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

GAME_IMGS = [pygame.image.load(os.path.join("assets", "chess.png")),
             pygame.image.load(os.path.join("assets", "pong.png")),
             pygame.image.load(os.path.join("assets", "hangman.png")),
             pygame.image.load(os.path.join("assets", "sudoku.png"))]


def bigger(image):
    return pygame.transform.scale(image, (image.get_width() + 20, image.get_height() + 20))


def draw_window(win, width, height, balls, home_icon, images, buttons):
    win.fill((255, 255, 255))
    for ball in balls:
        ball.draw(win)

    back_button = button.draw_back_button(win, home_icon)

    for i in range(len(images)):
        buttons[i] = pygame.draw.rect(win, (0, 0, 0), ((i % 3) * 325 + 50 - 20, (i // 3) * 325 + 175 - 20, 310, 310), 0)
        win.blit(pygame.transform.scale(images[i], (275, 275)), ((i % 3) * 325 + 50, (i // 3) * 325 + 175))

    return back_button, buttons


def main(win, width, height, fps, home_icon, images):
    games_run = True
    balls = ballbg.create_balls(width, height)
    clock = pygame.time.Clock()
    buttons = [0, 0, 0, 0]
    while games_run:
        clock.tick(fps)
        back_button, buttons = draw_window(win, width, height, balls, home_icon, images, buttons)
        mouse_pos = pygame.mouse.get_pos()
        for ball in balls:
            ball.move(balls)
        events = pygame.event.get()
        balls = ballbg.add_balls(events, width, height, balls)
        for event in events:
            if event.type == pygame.QUIT:
                games_run = False
                exit()

            if back_button.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from Project_Hub import home

            for i in range(len(buttons)):
                if buttons[i].collidepoint(mouse_pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if i == 0:
                            from project_files.Chess import game
                        elif i == 1:
                            from project_files.Pong import game
                        elif i == 2:
                            from project_files.Hangman import game
                        elif i == 3:
                            from project_files.Sudoku import game

        pygame.display.update()


main(WINDOW, WIDTH, HEIGHT, FPS, HOME_ICON, GAME_IMGS)
