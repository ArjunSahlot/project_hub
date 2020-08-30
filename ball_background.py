import pygame
import random
import math


class Ball:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.direction = random.randint(0, 360)
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.radius = random.randint(3, 8)
        self.velocity = random.randint(2, 5)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (round(self.x), round(self.y)), self.radius)

    def move(self, width, height, balls):
        self.x += self.velocity * math.sin(math.radians(self.direction))
        self.y -= self.velocity * math.cos(math.radians(self.direction))

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
