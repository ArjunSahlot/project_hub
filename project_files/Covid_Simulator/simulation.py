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

import math, os
import random
import pygame
from text_box import TextInput

pygame.init()


# Window management
FPS = 60
SETTINGSHEIGHT = 220
GRAPHHEIGHT = 100
WIDTH, HEIGHT = 800, 600
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1920//2 - WIDTH//2, 1080//2 - (HEIGHT + SETTINGSHEIGHT + GRAPHHEIGHT)//2)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT + SETTINGSHEIGHT + GRAPHHEIGHT))
pygame.display.set_caption("Covid-19 Simulator, By: Arjun Sahlot")

# Images
W, H = 135, 120
START = pygame.transform.scale(pygame.image.load(os.path.join("project_files", "Covid_Simulator", "assets", "start_img.png")), (W, H))
PAUSE = pygame.transform.scale(pygame.image.load(os.path.join("project_files", "Covid_Simulator", "assets", "pause_img.png")), (W, H))

# Constants
MAX_RAD, MIN_RAD = 9, 3
DEATH_RATE = 4
INFECTION_SPREAD_RATE = 35
SOCIAL_DIST = 20
SIMULATION_SPEED = 1
POPULATION_SIZE = 200
VERT_BOUNDARIES = [] # contains x-values. this is for splitting the circles
# GRAPHLENGTH = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 20, 255)
GREY = (200, 200, 200)
DARK_GREY = (120, 120, 120)
DEAD_COL = BLACK
SUSCEPTIBLE_COL = (150, 175, 201)
INFECTED_COL = (177, 103, 47)
RECOVERED_COL = (193, 142, 189)

INFO_FONT = pygame.font.SysFont("comicsans", 25)
FONT = pygame.font.SysFont("comicsans", 30)


class Circle:
    def __init__(self, width, height, moving, type="susceptible"):
        try:
            self.radius = ((POPULATION_SIZE*-1)+1000)/(999/MAX_RAD-MIN_RAD+1) + MIN_RAD-1
        except ZeroDivisionError:
            self.radius = 20
        self.x = random.randint(int(self.radius) + 5, width - int(self.radius) - 5)
        self.y = random.randint(int(self.radius) + 5, height - int(self.radius) - 5)
        self.speedx = random.choice((-2, -1, 0, 1, 2))
        self.speedy = random.choice((-2, -1, 0, 1, 2))
        self.moving = moving
        self.type = type
        self.time = 0

    def draw(self, win):
        if self.type == "susceptible":
            pygame.draw.circle(win, SUSCEPTIBLE_COL, (int(self.x), int(600 - self.y)), round(self.radius))
        elif self.type == "infected":
            pygame.draw.circle(win, INFECTED_COL, (int(self.x), int(600 - self.y)), round(self.radius))
        elif self.type == "recovered":
            pygame.draw.circle(win, RECOVERED_COL, (int(self.x), int(600 - self.y)), round(self.radius))
        elif self.type == "dead":
            pygame.draw.circle(win, DEAD_COL, (int(self.x), int(600 - self.y)), round(self.radius))

    def move(self):
        if self.moving:
            self.x += self.speedx * SIMULATION_SPEED
            self.y += self.speedy * SIMULATION_SPEED
        if self.type == "infected":
            self.time += 1

        if self.time == FPS*14//(SIMULATION_SPEED + 0.0001):
            self.time = 0
            if percent_to_bool(DEATH_RATE):
                self.type = "dead"
                self.moving = False
            else:
                self.type = "recovered"


def create_circles(width, height):
    circles = []
    for x in range(POPULATION_SIZE-1):
        circles.append(Circle(width, height, True if not percent_to_bool(SOCIAL_DIST) else False))
    circles.append(Circle(width, height, True, "infected"))
    return circles


def percent_to_bool(val):
    return random.randint(1, 100) <= val


def circle_collide(circle_1, circle_2):
    x_speed, y_speed = 0, 0
    circle1_speed = math.sqrt((circle_1.speedx ** 2) + (circle_1.speedy ** 2))
    x_diff = -(circle_1.x - circle_2.x)
    y_diff = -(circle_1.y - circle_2.y)
    if x_diff > 0:
        if y_diff > 0:
            angle = math.degrees(math.atan(y_diff / x_diff))
            x_speed = -circle1_speed * math.cos(math.radians(angle))
            y_speed = -circle1_speed * math.sin(math.radians(angle))
        elif y_diff < 0:
            angle = math.degrees(math.atan(y_diff / x_diff))
            x_speed = -circle1_speed * math.cos(math.radians(angle))
            y_speed = -circle1_speed * math.sin(math.radians(angle))
    elif x_diff < 0:
        if y_diff > 0:
            angle = 180 + math.degrees(math.atan(y_diff / x_diff))
            x_speed = -circle1_speed * math.cos(math.radians(angle))
            y_speed = -circle1_speed * math.sin(math.radians(angle))
        elif y_diff < 0:
            angle = -180 + math.degrees(math.atan(y_diff / x_diff))
            x_speed = -circle1_speed * math.cos(math.radians(angle))
            y_speed = -circle1_speed * math.sin(math.radians(angle))
    elif x_diff == 0:
        if y_diff > 0:
            angle = -90
        else:
            angle = 90
        x_speed = circle1_speed * math.cos(math.radians(angle))
        y_speed = circle1_speed * math.sin(math.radians(angle))
    elif y_diff == 0:
        if x_diff < 0:
            angle = 0
        else:
            angle = 180
        x_speed = circle1_speed * math.cos(math.radians(angle))
        y_speed = circle1_speed * math.sin(math.radians(angle))
    circle_1.speedx = x_speed
    circle_1.speedy = y_speed
    if circle_1.type in ("recovered", "dead") or circle_2.type in ("recovered", "dead"):
        return
    if circle_1.type == "infected":
        if percent_to_bool(INFECTION_SPREAD_RATE):
            circle_2.type = "infected"
    if circle_2.type == "infected":
        if percent_to_bool(INFECTION_SPREAD_RATE):
            circle_1.type = "infected"


def draw_graph(win, circles, x):
    perc_peps_recovered = math.floor(num_recovered(circles)*100/POPULATION_SIZE)
    perc_peps_susceptible = math.floor(num_susceptible(circles)*100/POPULATION_SIZE)
    perc_peps_infected = math.floor(num_infected(circles)*100/POPULATION_SIZE)
    perc_peps_dead = math.floor(num_dead(circles)*100/POPULATION_SIZE)
    start_h = HEIGHT + SETTINGSHEIGHT
    pygame.draw.line(win, RECOVERED_COL, (x, start_h), (x, start_h + perc_peps_recovered))
    pygame.draw.line(win, SUSCEPTIBLE_COL, (x, start_h + perc_peps_recovered), (x, start_h + perc_peps_recovered + perc_peps_susceptible))
    pygame.draw.line(win, INFECTED_COL, (x, start_h + perc_peps_recovered + perc_peps_susceptible), (x, start_h + perc_peps_recovered + perc_peps_susceptible + perc_peps_infected))
    pygame.draw.line(win, DEAD_COL, (x, start_h + perc_peps_recovered + perc_peps_susceptible + perc_peps_infected), (x, start_h + perc_peps_recovered + perc_peps_susceptible + perc_peps_infected + perc_peps_dead))

    pygame.draw.line(win, BLACK, (x+2, start_h), (x+2, start_h + GRAPHHEIGHT), 2)


def close_to(a, b):
    if b - 3 <= a <= b + 3:
        return True
    return False


def collision_detect(circles):
    for circle in circles:
        if circle.x < circle.radius or circle.x > WIDTH - circle.radius:
            circle.speedx *= -1
        if circle.y < circle.radius or circle.y > HEIGHT - circle.radius:
            circle.speedy *= -1
        for x in VERT_BOUNDARIES:
            if circle.x > x and close_to(x, circle.x - circle.radius):
                circle.speedx *= -1
            if circle.x < x and close_to(x, circle.x + circle.radius):
                circle.speedx *= -1

    for circle1 in circles:
        for circle2 in circles:
            if circle1 != circle2:
                if math.sqrt(((circle1.x - circle2.x) ** 2) + ((circle1.y - circle2.y) ** 2)) <= (circle1.radius + circle2.radius):
                    circle_collide(circle1, circle2)


def draw_window(win, circles, simulating, infect_typing, social_typing, death_typing, pop_typing, simulating_time, creating_vertboundary):
    win.fill(WHITE, (0, 0, WIDTH, HEIGHT))
    for circle in circles:
        circle.draw(win)
    for x in VERT_BOUNDARIES:
        pygame.draw.line(win, BLACK, (x, 0), (x, HEIGHT), 3)
        
    infect = FONT.render("% Infect Rate", 1, BLACK)
    death = FONT.render("% Death Rate", 1, BLACK)
    social = FONT.render("% Social Distancing", 1, BLACK)
    pop = FONT.render("Population Size", 1, BLACK)

    win.fill(GREY, (0, HEIGHT, WIDTH, SETTINGSHEIGHT))
    infect_box = pygame.draw.rect(win, WHITE, (15, HEIGHT + 15, 100, (SETTINGSHEIGHT - 40 - 30)//3))
    pygame.draw.rect(win, BLACK if not infect_typing else BLUE, (15, HEIGHT + 15, 100, (SETTINGSHEIGHT - 40 - 30)//3), 3)
    win.blit(infect, (15 + 100 + 8, HEIGHT + 15 + ((SETTINGSHEIGHT - 40 - 30)//3)//2 - infect.get_height()//2))

    death_box = pygame.draw.rect(win, WHITE, (15, HEIGHT + 15 + (SETTINGSHEIGHT - 40 - 30)//3 + 15, 100, (SETTINGSHEIGHT - 40 - 30)//3))
    pygame.draw.rect(win, BLACK if not death_typing else BLUE, (15, HEIGHT + 15 + (SETTINGSHEIGHT - 40 - 30)//3 + 15, 100, (SETTINGSHEIGHT - 40 - 30)//3), 3)
    win.blit(death, (15 + 100 + 8, HEIGHT + 15 + ((SETTINGSHEIGHT - 40 - 30)//3)//2 - death.get_height()//2 + (SETTINGSHEIGHT - 40 - 30)//3 + 15))

    social_box = pygame.draw.rect(win, WHITE, (15, HEIGHT + 15 + (SETTINGSHEIGHT - 40 - 30)*2//3 + 15 + 15, 100, (SETTINGSHEIGHT - 40 - 30)//3))
    pygame.draw.rect(win, BLACK if not social_typing else BLUE, (15, HEIGHT + 15 + (SETTINGSHEIGHT - 40 - 30)*2//3 + 15 + 15, 100, (SETTINGSHEIGHT - 40 - 30)//3), 3)
    win.blit(social, (15 + 100 + 8, HEIGHT + 15 + ((SETTINGSHEIGHT - 40 - 30)//3)//2 - social.get_height()//2 + (SETTINGSHEIGHT - 40 - 30)*2//3 + 15 + 15))

    pop_box = pygame.draw.rect(win, WHITE, (15 + 100 + 8 + infect.get_width() + 250, HEIGHT + 15, 100, (SETTINGSHEIGHT - 40 - 30)//3))
    pygame.draw.rect(win, BLACK if not pop_typing else BLUE, (15 + 100 + 8 + infect.get_width() + 250, HEIGHT + 15, 100, (SETTINGSHEIGHT - 40 - 30)//3), 3)
    win.blit(pop, (15 + 100 + 8 + infect.get_width() + 250 + 100 + 8, HEIGHT + 15 + ((SETTINGSHEIGHT - 40 - 30)//3)//2 - pop.get_height()//2))

    text1 = INFO_FONT.render(f"{num_infected(circles)} infected, infect rate: {INFECTION_SPREAD_RATE}%", 1, BLACK)
    text2 = INFO_FONT.render(f"{num_dead(circles)} dead, death rate: {DEATH_RATE}%", 1, BLACK)
    text3 = INFO_FONT.render(f"{POPULATION_SIZE*SOCIAL_DIST//100} people social distancing ({SOCIAL_DIST}%)", 1, BLACK)
    text4 = INFO_FONT.render(f"{num_recovered(circles)} people recovered", 1, BLACK)
    
    win.blit(text1, (WIDTH - text1.get_width() - 10, 10))
    win.blit(text2, (WIDTH - text2.get_width() - 10, 10 + text1.get_height() + 3))
    win.blit(text3, (WIDTH - text3.get_width() - 10, 10 + text1.get_height() + 3 + text2.get_height() + 3))
    win.blit(text4, (WIDTH - text4.get_width() - 10, 10 + text1.get_height() + 3 + text2.get_height() + 3 + text3.get_height() + 3))

    win.blit(START if not simulating else PAUSE, (WIDTH - W, HEIGHT + SETTINGSHEIGHT - H))
    if simulating:
        graph_x = simulating_time//3
        draw_graph(win, circles, graph_x)

    vert_box = pygame.draw.rect(win, BLACK if not creating_vertboundary else BLUE, (WIDTH//2 + 50, HEIGHT + SETTINGSHEIGHT - 130, 125, 125), 5)
    pygame.draw.line(win, BLACK, (WIDTH//2 + 50 + 125//2, HEIGHT + SETTINGSHEIGHT - 130 + 10), (WIDTH//2 + 50 + 125//2, HEIGHT + SETTINGSHEIGHT - 130 + 20 + 50), 5)
    txt = INFO_FONT.render("Vert", 1, BLACK)
    txt2 = INFO_FONT.render("Bound", 1, BLACK)
    win.blit(txt, (WIDTH//2 + 50 + 125//2 - txt.get_width()//2, HEIGHT + SETTINGSHEIGHT - 130 + 20 + 50 + 5))
    win.blit(txt2, (WIDTH // 2 + 50 + 125 // 2 - txt2.get_width()// 2, HEIGHT + SETTINGSHEIGHT - 130 + 20 + 50 + 5 + txt.get_height() + 3))

    sim_box = pygame.draw.rect(win, DARK_GREY, (15 + 262, HEIGHT + 15 + 25 - 10 - 10, 200, 20))
    txt3 = INFO_FONT.render("Simulation Speed", 1, BLACK)
    win.blit(txt3, (15 + 262 + 100 - txt3.get_width()//2, HEIGHT + 15 + 25 - 10 - 10 + 20 + 7))
    pygame.draw.circle(win, WHITE, (round(277 + SIMULATION_SPEED/(3/201)), HEIGHT + 15 + 25 - 10), 10)

    return infect_box, death_box, social_box, pop_box, vert_box, sim_box


def parse_percent(text, code="n/a"):
    final = ""
    if code == "n/a":
        accepting_periods = True
        for i in text:
            if i.isdigit() or (i == "." and accepting_periods):
                final += i
                if i == ".":
                    accepting_periods = False
        if final.endswith("."):
            final += "0"

        if final == "":
            final += "0"

        return float(final)

    else:
        for i in text:
            if i.isdigit():
                final += i

        if final == "":
            final += "0"

        return int(final)


def num_dead(circles):
    count = 0
    for circle in circles:
        if circle.type == "dead":
            count += 1
    return count


def num_susceptible(circles):
    count = 0
    for circle in circles:
        if circle.type == "susceptible":
            count += 1
    return count


def num_recovered(circles):
    count = 0
    for circle in circles:
        if circle.type == "recovered":
            count += 1
    return count


def num_infected(circles):
    count = 0
    for circle in circles:
        if circle.type == "infected":
            count += 1
    return count


def main(win, width, height):
    global SOCIAL_DIST, INFECTION_SPREAD_RATE, DEATH_RATE, POPULATION_SIZE, SIMULATION_SPEED
    circles = create_circles(width, height)
    clock = pygame.time.Clock()
    social_text = TextInput(initial_string=str(SOCIAL_DIST), max_string_length=6)
    infect_text = TextInput(initial_string=str(INFECTION_SPREAD_RATE), max_string_length=6)
    death_text = TextInput(initial_string=str(DEATH_RATE), max_string_length=6)
    pop_text = TextInput(initial_string=str(POPULATION_SIZE), max_string_length=3)
    prev_socialtext = SOCIAL_DIST
    prev_poptext = POPULATION_SIZE
    social_typing = False
    infect_typing = False
    death_typing = False
    pop_typing = False
    creating_vertboundary = False
    simulating = False
    simulating_time = 0
    run = True
    win.fill(WHITE, (0, HEIGHT + SETTINGSHEIGHT, WIDTH, GRAPHHEIGHT))
    while run:
        clock.tick(FPS)
        infect_box, death_box, social_box, pop_box, vert_box, sim_box = draw_window(win, circles, simulating, infect_typing, social_typing, death_typing, pop_typing, simulating_time, creating_vertboundary)
        events = pygame.event.get()
        mouseX, mouseY = pygame.mouse.get_pos()
        if creating_vertboundary and mouseY < height:
            pygame.draw.line(win, BLACK, (mouseX, 0), (mouseX, HEIGHT), 3)
        if simulating:
            simulating_time += 1
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                exit()

            if mouseY < height:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if creating_vertboundary:
                        if mouseX not in VERT_BOUNDARIES:
                            VERT_BOUNDARIES.append(mouseX)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if infect_box.collidepoint(event.pos):
                    infect_typing = True
                else:
                    infect_typing = False
                if death_box.collidepoint(event.pos):
                    death_typing = True
                else:
                    death_typing = False
                if social_box.collidepoint(event.pos):
                    social_typing = True
                else:
                    social_typing = False
                if pop_box.collidepoint(event.pos):
                    pop_typing = True
                else:
                    pop_typing = False

                if height + SETTINGSHEIGHT > mouseX > WIDTH - W and mouseY > height + SETTINGSHEIGHT - H:
                    simulating = True if simulating == False else False

                if vert_box.collidepoint(event.pos):
                    creating_vertboundary = True if creating_vertboundary == False else False

        if pygame.mouse.get_pressed()[0]:
            if sim_box.collidepoint((mouseX, mouseY)):
                SIMULATION_SPEED = (mouseX-277)/(200/3)

        if simulating:
            for circle in circles:
                circle.move()
        if social_text.update(events, social_typing):
            SOCIAL_DIST = parse_percent(social_text.get_text())
            social_text.input_string = str(SOCIAL_DIST)
            if prev_socialtext != SOCIAL_DIST:
                circles = create_circles(width, height)
                simulating_time = 0
                win.fill(WHITE, (0, HEIGHT + SETTINGSHEIGHT, WIDTH, GRAPHHEIGHT))
            prev_socialtext = SOCIAL_DIST
        if infect_text.update(events, infect_typing):
            INFECTION_SPREAD_RATE = parse_percent(infect_text.get_text())
            infect_text.input_string = str(INFECTION_SPREAD_RATE)
        if death_text.update(events, death_typing):
            DEATH_RATE = parse_percent(death_text.get_text())
            death_text.input_string = str(DEATH_RATE)
        if pop_text.update(events, pop_typing):
            POPULATION_SIZE = parse_percent(pop_text.get_text(), code="pop")
            pop_text.input_string = str(POPULATION_SIZE)
            if prev_poptext != POPULATION_SIZE:
                circles = create_circles(width, height)
                simulating_time = 0
                win.fill(WHITE, (0, HEIGHT + SETTINGSHEIGHT, WIDTH, GRAPHHEIGHT))
        collision_detect(circles)
        win.blit(social_text.get_surface(), (social_box[0] + social_box[3] - social_text.get_surface().get_width()//2, social_box[1] + social_box[3]//2 - social_text.get_surface().get_height()//2))
        win.blit(infect_text.get_surface(), (infect_box[0] + infect_box[3] - infect_text.get_surface().get_width()//2, infect_box[1] + infect_box[3]//2 - infect_text.get_surface().get_height()//2))
        win.blit(death_text.get_surface(), (death_box[0] + death_box[3] - death_text.get_surface().get_width()//2, death_box[1] + death_box[3]//2 - death_text.get_surface().get_height()//2))
        win.blit(pop_text.get_surface(), (pop_box[0] + pop_box[3] - pop_text.get_surface().get_width()//2, pop_box[1] + pop_box[3]//2 - pop_text.get_surface().get_height()//2))

        pygame.display.update()

# if __name__ == "__main__":
#     main(WINDOW, WIDTH, HEIGHT)
# else:
#     print("This is not a module that you can use. Sorry.")

main(WINDOW, WIDTH, HEIGHT)
