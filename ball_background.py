import pygame
import random
import math


class Ball:
    def __init__(self, x, y, width, height, bounce):
        self.x, self.y = x, y
        self.direction = random.randint(0, 360)
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.radius = random.randint(3, 8)
        self.velocity = random.randint(2, 5)
        self.bounce = bounce
        self.width, self.height = width, height

    def draw(self, win):
        pygame.draw.circle(win, self.color, (round(self.x), round(self.y)), self.radius)

    def move(self, balls):
        if not self.bounce:
            self.x += self.velocity * math.sin(math.radians(self.direction))
            self.y -= self.velocity * math.cos(math.radians(self.direction))

            destroy_balls(self.width, self.height, balls, self.bounce)
        else:
            self.x += self.velocity * math.sin(math.radians(self.direction))
            self.y -= self.velocity * math.cos(math.radians(self.direction))

            if self.x - self.radius < 0:
                self.direction -= 180

            if self.x + self.radius > self.width:
                self.direction += 180

            if self.y - self.radius < 0:
                self.direction += 180

            if self.y + self.radius > self.height:
                self.direction -= 180

        return balls


def create_balls(width, height, bounce=False):
    balls = []
    for _ in range(100):
        balls.append(Ball(random.randint(0, width), random.randint(0, height), width, height, bounce))

    return balls


def destroy_balls(width, height, balls, bounce):
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
        balls.append(Ball(random.randint(0, width), random.randint(0, height), width, height, bounce))

    return balls


def add_balls(events, width, height, balls, bounce=False):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(Ball(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], width, height, bounce))
            balls.pop(0)

    return balls
