import ball_background as ballbg
import back_button as button
import pygame

pygame.init()


def draw_window(win, width, height, balls, home_icon):
    win.fill((255, 255, 255))
    for ball in balls:
        ball.draw(win)

    back_button = button.draw_back_button(win, home_icon)

    return back_button


def main(win, width, height, fps, home_icon):
    vis_run = True
    balls = ballbg.create_balls(width, height)
    clock = pygame.time.Clock()
    while vis_run:
        clock.tick(fps)
        back_button = draw_window(win, width, height, balls, home_icon)
        mouse_pos = pygame.mouse.get_pos()
        for ball in balls:
            ball.move(width, height, balls)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vis_run = False
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                balls.append(ballbg.Ball(mouse_pos[0], mouse_pos[1]))
                balls.pop(0)

            if back_button.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "home"

        pygame.display.update()
