import pygame
import random


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
