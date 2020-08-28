import ball_background as ballbg
import back_button as button
import pygame

pygame.init()


def bigger(image):
    return pygame.transform.scale(image, (image.get_width() + 20, image.get_height() + 20))


def draw_window(win, width, height, balls, home_icon, images, buttons):
    win.fill((255, 255, 255))
    for ball in balls:
        ball.draw(win)

    back_button = button.draw_back_button(win, home_icon)

    for i in range(len(images)):
        buttons[i] = pygame.draw.rect(win, (0, 0, 0), ((i % 3) * 325 + 50 - 20, (i // 3)*325 + 175 - 20, 310, 310), 0)
        win.blit(pygame.transform.scale(images[i], (275, 275)), ((i % 3) * 325 + 50, (i // 3)*325 + 175))

    return back_button, buttons


def main(win, width, height, fps, home_icon, images):
    run = True
    balls = ballbg.create_balls(width, height)
    clock = pygame.time.Clock()
    buttons = [0, 0, 0]
    while run:
        clock.tick(fps)
        back_button, buttons = draw_window(win, width, height, balls, home_icon, images, buttons)
        mouse_pos = pygame.mouse.get_pos()
        for ball in balls:
            ball.move(width, height, balls)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                balls.append(ballbg.Ball(mouse_pos[0], mouse_pos[1]))
                balls.pop(0)

            if back_button.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "home"

            for i in range(len(buttons)):
                if buttons[i].collidepoint(mouse_pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if i == 0:
                            return "search"
                        elif i == 1:
                            return "sort"
                        elif i == 2:
                            return "paint"

        pygame.display.update()
