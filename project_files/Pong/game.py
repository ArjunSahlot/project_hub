import pygame, math, os, random
import numpy as np

pygame.init()

WIDTH, HEIGHT = 1000, 650
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong, By: Arjun Sahlot")
pygame.display.set_icon(pygame.image.load(os.path.join("assets", "icon.png")))

SCORE_FONT = pygame.font.SysFont("comicsans", 70)
ERROR_FONT = pygame.font.SysFont("comicsans", 130)

PLAYER_WIDTH = 25
PLAYER_HEIGHT = 150
PLAYER1_X = 20
PLAYER2_X = WIDTH - PLAYER_WIDTH - PLAYER1_X
PLAYER_SPEED = 7
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Ball:
    radius = 15
    velocity = 8

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.directionx, self.directiony = random.choice((-1, 1)), random.choice((-1, 1))

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), self.radius)

    def move(self, player1_x, player2_x, player1_y, player2_y):
        self.x += self.directionx * self.velocity
        self.y += self.directiony * self.velocity

        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.directiony *= -1

        if player1_x + PLAYER_WIDTH >= self.x - self.radius and player1_y < self.y - self.radius and player1_y + PLAYER_HEIGHT > self.y - self.radius:
            self.directionx *= -1
        if player2_x <= self.x + self.radius and player2_y < self.y - self.radius and player2_y + PLAYER_HEIGHT > self.y - self.radius:
            self.directionx *= -1


def dashed_line(win, col, start_pos, end_pos, width, dash_length):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length

    if x1 == x2:
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif y1 == y2:
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a ** 2 + b ** 2))
        dx = dl * a / c
        dy = dl * b / c

        xcoords = [x for x in np.arange(x1, x2, dx if x1 < x2 else -dx)]
        ycoords = [y for y in np.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(win, col, start, end, width)


def display_mesg(win, text):
    text = ERROR_FONT.render(text, 1, WHITE)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))
    pygame.display.update()
    pygame.time.delay(1000)
    exit()


def draw_window(win, width, height, player_width, player_height, player1_x, player2_x, player1_y, player2_y,
                player1_score, player2_score, ball):
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, (player1_x, player1_y, player_width, player_height))
    pygame.draw.rect(win, WHITE, (player2_x, player2_y, player_width, player_height))
    dashed_line(win, WHITE, (width // 2, 15), (width // 2, height), 5, 15)
    win.blit(SCORE_FONT.render(str(player1_score), 1, WHITE), (180, 20))
    win.blit(SCORE_FONT.render(str(player2_score), 1, WHITE),
             (WIDTH - 180 - SCORE_FONT.render(str(player2_score), 1, WHITE).get_width(), 20))
    ball.draw(win)


def main(win, width, height, player_width, player_height, player1_x, player2_x):
    player1_y, player2_y = height // 2 - player_height // 2, height // 2 - player_height // 2
    player1_score, player2_score = 0, 0
    ball = Ball(width // 2, random.randint(16, height - 16))
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        if ball.x - ball.radius <= 0:
            player2_score += 1
            ball = Ball(width // 2, random.randint(16, height - 16))

        elif ball.x + ball.radius >= WIDTH:
            player1_score += 1
            ball = Ball(width // 2, random.randint(16, height - 16))

        if ball.y > player1_y:
            player1_y += PLAYER_SPEED
        elif ball.y < player1_y + player_height:
            player1_y -= PLAYER_SPEED

        if player1_y < 0:
            player1_y = 0
        elif player1_y + player_height > height:
            player1_y = height - player_height
        if player2_y < 0:
            player2_y = 0
        elif player2_y + player_height > height:
            player2_y = height - player_height

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player2_y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            player2_y += PLAYER_SPEED

        draw_window(win, width, height, player_width, player_height, player1_x, player2_x, player1_y, player2_y,
                    player1_score, player2_score, ball)
        ball.move(player1_x, player2_x, player1_y, player2_y)

        if player1_score == 10:
            display_mesg(win, "Computer Won")
        if player2_score == 10:
            display_mesg(win, "You Won")

        pygame.display.update()


main(WINDOW, WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER1_X, PLAYER2_X)
