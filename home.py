import ball_background as ballbg
import os
import pygame

pygame.init()

pygame.display.set_caption("Project Hub -- Home")
pygame.display.set_icon(pygame.transform.scale(pygame.image.load(os.path.join("assets", "home_icon.png")), (32, 32)))

FPS = 30

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_window(win, width, height, balls):
    win.fill((255, 255, 255))
    for ball in balls:
        ball.draw(win)

    font = pygame.font.SysFont("comicsans", 50)
    big_font = pygame.font.SysFont("comicsans", 80)

    vis_button = pygame.draw.rect(win, (0, 255, 0), (50, 475, 225, 100))
    games_button = pygame.draw.rect(win, (0, 255, 0), (width - 50 - 225, 475, 225, 100))

    vis_text = font.render("Visualizers", 1, (0, 0, 0))
    games_text = font.render("Games", 1, (0, 0, 0))
    info_text = big_font.render("Project Hub", 1, (0, 0, 0))

    win.blit(vis_text, (50 + 225 // 2 - vis_text.get_width() // 2, 475 + 100 // 2 - vis_text.get_height() // 2))
    win.blit(games_text,
             (width - 50 - 225 + 225 // 2 - games_text.get_width() // 2, 475 + 100 // 2 - games_text.get_height() // 2))
    win.blit(info_text, (width // 2 - info_text.get_width() // 2, 50))

    return vis_button, games_button


def main(win, width, height, fps):
    home_run = True
    balls = ballbg.create_balls(width, height)
    clock = pygame.time.Clock()
    while home_run:
        clock.tick(fps)
        vis_button, games_button = draw_window(win, width, height, balls)
        mouse_pos = pygame.mouse.get_pos()
        for ball in balls:
            ball.move(balls)
        events = pygame.event.get()
        balls = ballbg.add_balls(events, width, height, balls)
        for event in events:
            if event.type == pygame.QUIT:
                home_run = False
                exit()

            if vis_button.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from Project_Hub import visualizers

            if games_button.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from Project_Hub import games

        pygame.display.update()


main(WINDOW, WIDTH, HEIGHT, FPS)
