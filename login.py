import ball_background as ballbg
import os
import pygame
from text_box import TextInput

pygame.display.set_icon(pygame.image.load(os.path.join("assets", "login_icon.png")))
pygame.display.set_caption("Project Hub -- Login")

pygame.init()

FONT = pygame.font.SysFont("comicsans", 75)


def draw_window(win, width, height, balls, username_typing, password_typing):
    win.fill((255, 255, 255))
    for ball in balls:
        ball.draw(win)

    text = FONT.render("Login", 1, (0, 0, 0))
    win.blit(text, (width // 2 - text.get_width() // 2, 200))

    pygame.draw.rect(win, (255, 255, 255), (width // 2 - 250, 400, 500, 60))
    username_box = pygame.draw.rect(win, (0, 0, 0) if not username_typing else (0, 20, 255),
                                    (width // 2 - 250, 400, 500, 60), 3)

    pygame.draw.rect(win, (255, 255, 255), (width // 2 - 250, 500, 500, 60))
    password_box = pygame.draw.rect(win, (0, 0, 0) if not password_typing else (0, 20, 255),
                                    (width // 2 - 250, 500, 500, 60), 3)

    return username_box, password_box


def main(win, width, height, fps):
    login_run = True
    bouncing_balls = False
    balls = ballbg.create_balls(width, height, bouncing_balls)
    clock = pygame.time.Clock()
    username_text = TextInput("Username", max_string_length=36)
    password_text = TextInput("Password", max_string_length=36)
    username_typing = False
    password_typing = False
    while login_run:
        clock.tick(fps)
        for ball in balls:
            ball.move(balls)
        username_box, password_box = draw_window(win, width, height, balls, username_typing, password_typing)

        mouse_pos = pygame.mouse.get_pos()
        events = pygame.event.get()
        balls = ballbg.add_balls(events, width, height, balls, bouncing_balls)
        for event in events:
            if event.type == pygame.QUIT:
                login_run = False
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if username_box.collidepoint(mouse_pos):
                    username_typing = True
                    password_typing = False
                    if username_text.get_text() == "Username":
                        username_text.clear_text()
                elif password_box.collidepoint(mouse_pos):
                    password_typing = True
                    username_typing = False
                    if password_text.get_text() == "Password":
                        password_text.clear_text()
                    password_text.password = True
                else:
                    username_typing = False
                    password_typing = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print(len(username_text.get_text()))
                from Project_Hub import home

        if password_text.get_text() == "" and not password_typing:
            password_text.input_string = "Password"
            password_text.password = False
        if username_text.get_text() == "" and not username_typing:
            username_text.input_string = "Username"

        username_text.update(events, username_typing)
        win.blit(username_text.get_surface(),
                 (width // 2 - 250 + 20, 400 + 30 - username_text.get_surface().get_height() // 2))
        password_text.update(events, password_typing)
        win.blit(password_text.get_surface(),
                 (width // 2 - 250 + 20, 500 + 30 - password_text.get_surface().get_height() // 2))
        pygame.display.update()
