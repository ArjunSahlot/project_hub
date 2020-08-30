import ball_background as ballbg
from text_box import TextInput
import pygame


pygame.init()

FONT = pygame.font.SysFont("comicsans", 75)

def draw_window(win, width, height, balls, username_typing, password_typing):
    win.fill((255, 255, 255))
    for ball in balls:
        ball.draw(win)

    text = FONT.render("Login", 1, (0, 0, 0))
    win.blit(text, (width//2 - text.get_width()//2, 200))

    pygame.draw.rect(win, (255, 255, 255), (width//2 - 250, 400, 500, 60))
    username_box = pygame.draw.rect(win, (0, 0, 0) if not username_typing else (0, 20, 255), (width//2 - 250, 400, 500, 60), 3)

    pygame.draw.rect(win, (255, 255, 255), (width // 2 - 250, 500, 500, 60))
    password_box = pygame.draw.rect(win, (0, 0, 0) if not password_typing else (0, 20, 255), (width // 2 - 250, 500, 500, 60), 3)

    return username_box, password_box

def main(win, width, height, fps):
    login_run = True
    balls = ballbg.create_balls(width, height)
    clock = pygame.time.Clock()
    username_text = TextInput("Username")
    password_text = TextInput("Password")
    username_typing = False
    password_typing = False
    while login_run:
        clock.tick(fps)
        for ball in balls:
            ball.move(width, height, balls)
        username_box, password_box = draw_window(win, width, height, balls, username_typing, password_typing)

        mouse_pos = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                login_run = False
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                balls.append(ballbg.Ball(mouse_pos[0], mouse_pos[1]))
                balls.pop(0)

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
                return "pass"

        if not password_typing:
            password_text.set_cursor_color((255, 255, 255))
        else:
            password_text.set_cursor_color((0, 0, 1))
        if not username_typing:
            username_text.set_cursor_color((255, 255, 255))
        else:
            username_text.set_cursor_color((0, 0, 1))

        username_text.update(events, username_typing)
        win.blit(username_text.get_surface(), (width//2 - 250 + 20, 400 + 30 - username_text.get_surface().get_height()//2))
        password_text.update(events, password_typing)
        win.blit(password_text.get_surface(), (width//2 - 250 + 20, 500 + 30 - password_text.get_surface().get_height()//2))
        pygame.display.update()
