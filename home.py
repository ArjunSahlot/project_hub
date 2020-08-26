import pygame, random

pygame.init()

class Ball:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.dirx, self.diry = random.choice((-3, -2, -1, 1, 2, 3)), random.choice((-3, -2, -1, 1, 2, 3))
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.radius = random.randint(3, 8)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self, width, height, balls):
        self.x += self.dirx
        self.y += self.diry

        destroy_balls(width, height, balls)

        return balls


def create_balls(width, height):
    balls = []
    for _ in range(100):
        balls.append(Ball(random.randint(0, width), random.randint(0, height)))

    return balls


def destroy_balls(width, height, balls):
    rem = []

    for ball in balls:
        if ball.x - ball.radius > width:
            rem.append(ball)
        elif ball.x + ball.radius < 0:
            rem.append(ball)
        elif ball.y - ball.radius > height:
            rem.append(ball)
        elif ball.y + ball.radius < 0:
            rem.append(ball)

    for r in rem:
        balls.remove(r)
        balls.append(Ball(random.randint(0, width), random.randint(0, height)))

    return balls


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
    info_text = big_font.render("Arjun's Project Hub", 1, (0, 0, 0))

    win.blit(vis_text, (50 + 225//2 - vis_text.get_width()//2, 475 + 100//2 - vis_text.get_height()//2))
    win.blit(games_text, (width - 50 - 225 + 225 // 2 - games_text.get_width() // 2, 475 + 100 // 2 - games_text.get_height() // 2))
    win.blit(info_text, (width//2 - info_text.get_width()//2, 50))

    return vis_button, games_button


def main(win, width, height, fps):
    home_run = True
    balls = create_balls(width, height)
    clock = pygame.time.Clock()
    while home_run:
        clock.tick(fps)
        vis_button, games_button = draw_window(win, width, height, balls)
        mouse_pos = pygame.mouse.get_pos()
        for ball in balls:
            ball.move(width, height, balls)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home_run = False
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                balls.append(Ball(mouse_pos[0], mouse_pos[1]))
                balls.pop(0)

            if vis_button.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "vis"

            if games_button.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "games"

        pygame.display.update()
