import ball_background as ballbg
import os
import pygame

pygame.init()

pygame.display.set_caption("Project Hub -- Home")
pygame.display.set_icon(pygame.transform.scale(pygame.image.load(os.path.join("assets", "home_icon.png")), (32, 32)))
SETTINGS = pygame.transform.scale(pygame.image.load(os.path.join("assets", "settings_button.png")), (65, 65))

FONT = pygame.font.SysFont("comicsans", 50)
BIG_FONT = pygame.font.SysFont("comicsans", 80)

FPS = 30

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

setting_buttons = [
    "General"
]


def draw_window(win, width, height, balls, status):
    win.fill((255, 255, 255))
    for ball in balls:
        ball.draw(win)

    if status == "IDLE":
        vis_button = pygame.draw.rect(win, (0, 255, 0), (50, 475, 225, 100))
        games_button = pygame.draw.rect(win, (0, 255, 0), (width - 50 - 225, 475, 225, 100))

        vis_text = FONT.render("Visualizers", 1, (0, 0, 0))
        games_text = FONT.render("Games", 1, (0, 0, 0))
        info_text = BIG_FONT.render("Project Hub", 1, (0, 0, 0))

        win.blit(vis_text, (50 + 225 // 2 - vis_text.get_width() // 2, 475 + 100 // 2 - vis_text.get_height() // 2))
        win.blit(games_text,
                 (width - 50 - 225 + 225 // 2 - games_text.get_width() // 2, 475 + 100 // 2 - games_text.get_height() // 2))
        win.blit(info_text, (width // 2 - info_text.get_width() // 2, 50))

        win.blit(SETTINGS, (15, 15))

        return vis_button, games_button

    else:
        pygame.draw.rect(win, (90, 90, 90), (0, 0, 250, HEIGHT))
        for ind, button in enumerate(setting_buttons):
            text = FONT.render(button, 1, (0, 0, 0))
            win.blit(text, (125 - text.get_width()//2, 15 + 75*ind))
            pygame.draw.line(win, (0, 0, 0), (30, 60 + 75*ind), (250-30, 60 + 75*ind), 5)

        if status == "GENERAL":
            pass


def main(win, width, height, fps):
    home_run = True
    balls = ballbg.create_balls(width, height)
    clock = pygame.time.Clock()
    status = "IDLE"
    while home_run:
        clock.tick(fps)
        if status == "IDLE":
            vis_button, games_button = draw_window(win, width, height, balls, status)
        else:
            draw_window(win, width, height, balls, status)
        mouse_pos = pygame.mouse.get_pos()
        for ball in balls:
            ball.move(balls)
        events = pygame.event.get()
        balls = ballbg.add_balls(events, width, height, balls)
        for event in events:
            if event.type == pygame.QUIT:
                home_run = False
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if status == "IDLE":
                    if vis_button.collidepoint(mouse_pos):
                        import visualizers

                    if games_button.collidepoint(mouse_pos):
                        import games

                    if 15 <= mouse_pos[0] <= 15 + 65 and 15 <= mouse_pos[1] <= 15 + 65:
                        status = "GENERAL"
                else:
                    pass

        pygame.display.update()


main(WINDOW, WIDTH, HEIGHT, FPS)
