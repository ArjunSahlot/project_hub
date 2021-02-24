#
#  Project hub
#  A group of some of my pygame projects.
#  Copyright Arjun Sahlot 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import pygame, os, random
import tkinter as tk

pygame.init()

screen_width = tk.Tk().winfo_screenwidth()
screen_height = tk.Tk().winfo_screenheight()

WIDTH, HEIGHT = 1000, 700
FPS = 60

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_width//2-WIDTH//2, screen_height//2-HEIGHT//2)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodger Plane, By: Arjun Sahlot")
pygame.display.set_icon(pygame.image.load(os.path.join("project_files", "Dodger_Plane", "assets", "icon.png")))

PLAYER_BACKFORTH = True

FONT = pygame.font.SysFont("comicsans", 50)
BIG_FONT = pygame.font.SysFont("comicsans", 100)


BLACK = (0, 0, 0)


class Player:
    def __init__(self, x, y, width, height, vel):
        self.x, self.y, self.width, self.height, self.vel = x, y, width, height, vel
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("project_files", "Dodger_Plane", "assets", "player.png")), (width, height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y + self.height < HEIGHT:
            self.y += self.vel
        if PLAYER_BACKFORTH:
            if keys[pygame.K_LEFT] and self.x > 0:
                self.x -= self.vel
            if keys[pygame.K_RIGHT] and self.x + self.width < WIDTH:
                self.x += self.vel

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.image)


class Bullet:
    WIDTH, HEIGHT = 40, 15
    VEL = 5

    def __init__(self, y):
        self.x, self.y = WIDTH + random.randint(0, 10)*80, y
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("project_files", "Dodger_Plane", "assets", "bullet.png")), (self.WIDTH, self.HEIGHT))

    def move(self, player):
        self.x -= self.VEL

        if self.collide(player):
            return "crash"
        if self.x + self.WIDTH < 0:
            return "out"

        return False

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def collide(self, player):
        player_mask = player.get_mask()
        mask = pygame.mask.from_surface(self.image)
        top_offset = (self.x - player.x, self.y - player.y)
        top_point = player_mask.overlap(mask, top_offset)

        if top_point:
            return True

        return False


class Clouds:
    VEL = 2

    def __init__(self):
        self.y = 0
        self.x1 = 0
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("project_files", "Dodger_Plane", "assets", "clouds_bg.png")), (WIDTH, HEIGHT))
        self.width = self.image.get_width()
        self.x2 = self.width

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width

        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width

    def draw(self, win):
        win.blit(self.image, (self.x1, self.y))
        win.blit(self.image, (self.x2, self.y))


def draw_window(win, player, clouds, bullets, score, max_score, playing):
    clouds.draw(win)
    player.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    text1 = FONT.render(f"Max Score: {max_score}", 1, BLACK)
    text2 = FONT.render(f"Score: {score}", 1, BLACK)
    win.blit(text1, (WIDTH - text1.get_width() - 1, 5))
    win.blit(text2, (WIDTH - text2.get_width() - 5, 5 + text1.get_height() + 5))
    if not playing:
        text = BIG_FONT.render("Press SPACEBAR to play", 1, BLACK)
        win.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))


def create_bullets(n):
    bullets = []
    for _ in range(n):
        bullets.append(Bullet(random.randint(0, HEIGHT - 40)))

    return bullets


def move_bullets(player, bullets, score, n):
    rem = []
    for bullet in bullets:
        movement = bullet.move(player)
        if movement == "out":
            rem.append(bullet)
            score += 1
        elif movement == "crash":
            score = 0
            player = Player(random.randint(5, 35), random.randint(0, HEIGHT-50), 100, 50, 7)
            bullets = create_bullets(n)

    for bullet in rem:
        bullets.remove(bullet)
        bullets.append(Bullet(random.randint(0, HEIGHT - 40)))

    return player, bullets, score


def move_objs(player, bullets, score, n, clouds):
    player.move()
    clouds.move()
    return move_bullets(player, bullets, score, n)


def main(win):
    clock = pygame.time.Clock()
    player = Player(random.randint(5, 35), random.randint(0, HEIGHT-50), 100, 50, 7)
    clouds = Clouds()
    n = 15
    bullets = create_bullets(n)
    score = 0
    try:
        with open("project_files/Dodger_Plane/max_score.txt", "r") as f:
            line = f.readline()
            max_score = int(line)
    except FileNotFoundError:
        max_score = 0
    run = True
    playing = False
    while run:
        clock.tick(FPS)
        draw_window(win, player, clouds, bullets, score, max_score, playing)
        if playing:
            player, bullets, score = move_objs(player, bullets, score, n, clouds)
        if max_score < score:
            max_score = score
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("project_files/Dodger_Plane/max_score.txt", "w") as f:
                    f.write(str(max_score))
                run = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = True if playing == False else False
        pygame.display.update()


main(WINDOW)
