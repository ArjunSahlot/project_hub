import pygame, os, random
import tkinter as tk

pygame.init()

screen_width = tk.Tk().winfo_screenwidth()
screen_height = tk.Tk().winfo_screenheight()

WIDTH, HEIGHT = 800, 900
FPS = 60

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_width//2-WIDTH//2, screen_height//2-HEIGHT//2)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Corona Fall, By: Arjun Sahlot")
pygame.display.set_icon(pygame.image.load(os.path.join("assets", "icon.png")))

FONT = pygame.font.SysFont("comicsans", 50)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Player:
    def __init__(self, x, width, height, vel):
        self.x, self.y, self.width, self.height, self.vel = x, HEIGHT - height, width, height, vel
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "player.png")), (width, height))
        self._change_colors()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x + self.width < WIDTH:
            self.x += self.vel

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.image)

    def _change_colors(self):
        w, h = self.image.get_size()
        for x in range(w):
            for y in range(h):
                if self.image.get_at((x, y))[3] != 0:
                    self.image.set_at((x, y), WHITE)


class Corona:
    WIDTH, HEIGHT = 50, 50
    VEL = 5

    def __init__(self):
        self.x, self.y = random.randint(0, WIDTH - self.WIDTH) , -random.randint(0, 10)*80
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "corona.png")), (self.WIDTH, self.HEIGHT))

    def move(self, player):
        self.y += self.VEL

        if self.collide(player):
            return "crash"
        if self.y + self.HEIGHT > HEIGHT:
            return "out"

        return False

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def collide(self, player):
        player_mask = player.get_mask()
        mask = pygame.mask.from_surface(self.image)
        offset = (self.x - player.x, self.y - player.y)
        point = player_mask.overlap(mask, offset)

        if point:
            return True

        return False


def draw_window(win, player, coronas, score, max_score):
    win.fill(BLACK)
    for corona in coronas:
        corona.draw(win)
    player.draw(win)
    text1 = FONT.render(f"Max Score: {max_score}", 1, WHITE)
    text2 = FONT.render(f"Score: {score}", 1, WHITE)
    win.blit(text1, (WIDTH - text1.get_width() - 1, 5))
    win.blit(text2, (WIDTH - text2.get_width() - 5, 5 + text1.get_height() + 5))


def create_coronas(n):
    bullets = []
    for _ in range(n):
        bullets.append(Corona())

    return bullets


def move_coronas(player, bullets, score, n):
    for bullet in bullets:
        movement = bullet.move(player)
        if movement == "out":
            bullets.remove(bullet)
            bullets.append(Corona())
            score += 1
        elif movement == "crash":
            score = 0
            player = Player(random.randint(5, 35), 80, 125, 7)
            bullets = create_coronas(n)

    return player, bullets, score


def main(win):
    clock = pygame.time.Clock()
    player = Player(random.randint(5, 35), 80, 125, 7)
    n = 25
    coronas = create_coronas(n)
    score = 0
    try:
        with open("max_score.txt", "r") as f:
            line = f.readline()
            max_score = int(line)
    except FileNotFoundError:
        max_score = 0
    run = True
    while run:
        clock.tick(FPS)
        draw_window(win, player, coronas, score, max_score)
        player.move()
        player, coronas, score = move_coronas(player, coronas, score, n)
        if max_score < score:
            max_score = score
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("max_score.txt", "w") as f:
                    f.write(str(max_score))
                run = False
        pygame.display.update()


main(WINDOW)
