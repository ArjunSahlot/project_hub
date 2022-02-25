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

import ball_background as ballbg
import os
import pygame
import pickle
from text_box import TextInput
from login_utils import Users

pygame.display.set_icon(pygame.image.load(os.path.join("assets", "login_icon.png")))
pygame.display.set_caption("Project Hub -- Login")

pygame.init()

BIG_FONT = pygame.font.SysFont("comicsans", 75)
MID_FONT = pygame.font.SysFont("comicsans", 45)
SMALL_FONT = pygame.font.SysFont("comicsans", 20)

PARENT = os.path.dirname(__file__)


def draw_window(win, width, height, balls, username_typing, password_typing, status):
    win.fill((255, 255, 255))
    for ball in balls:
        ball.draw(win)

    text = BIG_FONT.render("Login", 1, (0, 0, 0))
    win.blit(text, (width // 2 - text.get_width() // 2, 200))
    if status == "invalid":
        text1 = BIG_FONT.render("Invalid Credentials", 1, (255, 0, 0))
        win.blit(text1, (width // 2 - text1.get_width() // 2, 200 + text.get_height() + 10))

    pygame.draw.rect(win, (255, 255, 255), (width // 2 - 250, 400, 500, 60))
    username_box = pygame.draw.rect(win, (0, 0, 0) if not username_typing else (0, 20, 255),
                                    (width // 2 - 250, 400, 500, 60), 3)

    pygame.draw.rect(win, (255, 255, 255), (width // 2 - 250, 500, 500, 60))
    password_box = pygame.draw.rect(win, (0, 0, 0) if not password_typing else (0, 20, 255),
                                    (width // 2 - 250, 500, 500, 60), 3)

    create_box = pygame.draw.rect(win, (0, 255, 0), (width // 2 + 250 - 120, 575, 120, 20))
    create_text = SMALL_FONT.render("Create an Account", 1, (0, 0, 0))
    win.blit(create_text,
             (width // 2 + 250 - 120 + 60 - create_text.get_width() // 2, 575 + 10 - create_text.get_height() // 2))

    change_box = pygame.draw.rect(win, (0, 255, 0), (width // 2 - 250, 575, 120, 20))
    change_text = SMALL_FONT.render("Change Password", 1, (0, 0, 0))
    win.blit(change_text,
             (width // 2 - 250 + 60 - change_text.get_width() // 2, 575 + 10 - change_text.get_height() // 2))

    return username_box, password_box, create_box, change_box


def validate_user(users, username, password):
    return users.is_user_valid(username, password)


def draw_create(win, width, height, balls, username_typing, password_typing1, password_typing2, display):
    win.fill((255, 255, 255))
    for ball in balls:
        ball.draw(win)

    text = BIG_FONT.render("Create an Account", 1, (0, 0, 0))
    win.blit(text, (width // 2 - text.get_width() // 2, 100))

    pygame.draw.rect(win, (255, 255, 255), (width // 2 - 250, 300, 500, 60))
    username_box = pygame.draw.rect(win, (0, 0, 0) if not username_typing else (0, 20, 255),
                                    (width // 2 - 250, 300, 500, 60), 3)

    pygame.draw.rect(win, (255, 255, 255), (width // 2 - 250, 400, 500, 60))
    password_box1 = pygame.draw.rect(win, (0, 0, 0) if not password_typing1 else (0, 20, 255),
                                     (width // 2 - 250, 400, 500, 60), 3)

    pygame.draw.rect(win, (255, 255, 255), (width // 2 - 250, 500, 500, 60))
    password_box2 = pygame.draw.rect(win, (0, 0, 0) if not password_typing2 else (0, 20, 255),
                                     (width // 2 - 250, 500, 500, 60), 3)

    create_box = pygame.draw.rect(win, (0, 255, 0), (width // 2 + 250 - 120, 560 + 15, 120, 40))
    text = MID_FONT.render("Create!", 1, (0, 0, 0))
    win.blit(text, (width // 2 + 250 - 120 + 60 - text.get_width() // 2, 560 + 15 + 20 - text.get_height() // 2))

    two = three = False
    if display is not None:
        text = BIG_FONT.render(display, 1, (255, 0, 0))
        win.blit(text, (width//2 - text.get_width()//2, 150))
        if display == "Success, Your account has been created":
            two = True
        elif display == "Unfortunately there was a bug...":
            three = True

    if two:
        text = BIG_FONT.render("You are being redirected...", 1, (255, 0, 0))
        win.blit(text, (width // 2 - text.get_width() // 2, 200))

    if three:
        text = BIG_FONT.render("Please try again", 1, (255, 0, 0))
        win.blit(text, (width // 2 - text.get_width() // 2, 200))

    return username_box, password_box1, password_box2, create_box


def create_account(win, width, height, users, fps):
    clock = pygame.time.Clock()
    bouncing_balls = False
    balls = ballbg.create_balls(width, height, bouncing_balls)
    create_run = True
    username_text = TextInput("Username", max_string_length=36)
    password_text1 = TextInput("New Password", max_string_length=36)
    password_text2 = TextInput("Confirm New Password", max_string_length=36)
    username_typing = False
    password_typing1 = False
    password_typing2 = False
    display = None
    while create_run:
        clock.tick(fps)
        mouse_pos = pygame.mouse.get_pos()
        for ball in balls:
            ball.move(balls)
        events = pygame.event.get()
        balls = ballbg.add_balls(events, width, height, balls, bouncing_balls)
        username_box, password_box1, password_box2, create_box = draw_create(win, width, height, balls, username_typing,
                                                                             password_typing1, password_typing2,
                                                                             display)
        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if username_box.collidepoint(mouse_pos):
                    username_typing = True
                    password_typing1 = False
                    password_typing2 = False
                    if username_text.get_text() == "Username":
                        username_text.clear_text()
                elif password_box1.collidepoint(mouse_pos):
                    password_typing1 = True
                    password_typing2 = False
                    username_typing = False
                    if password_text1.get_text() == "New Password":
                        password_text1.clear_text()
                    password_text1.password = True
                elif password_box2.collidepoint(mouse_pos):
                    password_typing2 = True
                    password_typing1 = False
                    username_typing = False
                    if password_text2.get_text() == "Confirm New Password":
                        password_text2.clear_text()
                    password_text2.password = True
                else:
                    username_typing = False
                    password_typing1 = False
                    password_typing2 = False

                if create_box.collidepoint(mouse_pos):
                    if users.is_user(username_text.get_text()):
                        display = "Username is already taken"
                    else:
                        if password_text1.get_text() != password_text2.get_text():
                            display = "Passwords do not match"
                        else:
                            try:
                                users.add_user(username_text.get_text(), password_text1.get_text())
                                users.store()
                                display = "Success, Your account has been created"
                                draw_create(win, width, height, balls, username_typing,
                                            password_typing1, password_typing2,
                                            display)
                                pygame.display.update()
                                pygame.time.delay(2000)
                                create_run = False
                            except:
                                display = "Unfortunately there was a bug..."

        if password_text1.get_text() == "" and not password_typing1:
            password_text1.input_string = "New Password"
            password_text1.password = False
        if password_text2.get_text() == "" and not password_typing2:
            password_text2.input_string = "Confirm New Password"
            password_text2.password = False
        if username_text.get_text() == "" and not username_typing:
            username_text.input_string = "Username"

        username_text.update(events, username_typing)
        win.blit(username_text.get_surface(),
                 (width // 2 - 250 + 20, 300 + 30 - username_text.get_surface().get_height() // 2))
        password_text1.update(events, password_typing1)
        win.blit(password_text1.get_surface(),
                 (width // 2 - 250 + 20, 400 + 30 - password_text1.get_surface().get_height() // 2))
        password_text2.update(events, password_typing2)
        win.blit(password_text2.get_surface(),
                 (width // 2 - 250 + 20, 500 + 30 - password_text2.get_surface().get_height() // 2))

        pygame.display.update()


def draw_change(win, width, height, balls, username_typing, password_typing1, password_typing2, display):
    win.fill((255, 255, 255))
    for ball in balls:
        ball.draw(win)

    text = BIG_FONT.render("Change Password", 1, (0, 0, 0))
    win.blit(text, (width // 2 - text.get_width() // 2, 100))

    pygame.draw.rect(win, (255, 255, 255), (width // 2 - 250, 300, 500, 60))
    username_box = pygame.draw.rect(win, (0, 0, 0) if not username_typing else (0, 20, 255),
                                    (width // 2 - 250, 300, 500, 60), 3)

    pygame.draw.rect(win, (255, 255, 255), (width // 2 - 250, 400, 500, 60))
    password_box1 = pygame.draw.rect(win, (0, 0, 0) if not password_typing1 else (0, 20, 255),
                                     (width // 2 - 250, 400, 500, 60), 3)

    pygame.draw.rect(win, (255, 255, 255), (width // 2 - 250, 500, 500, 60))
    password_box2 = pygame.draw.rect(win, (0, 0, 0) if not password_typing2 else (0, 20, 255),
                                     (width // 2 - 250, 500, 500, 60), 3)

    change_box = pygame.draw.rect(win, (0, 255, 0), (width // 2 + 250 - 134, 560 + 15, 134, 40))
    text = MID_FONT.render("Change!", 1, (0, 0, 0))
    win.blit(text, (width // 2 + 250 - 134 + 67 - text.get_width() // 2, 560 + 15 + 20 - text.get_height() // 2))

    if display is not None:
        text = BIG_FONT.render(display, 1, (255, 0, 0))
        win.blit(text, (width//2 - text.get_width()//2, 175))

    return username_box, password_box1, password_box2, change_box


def change_password(win, width, height, users, fps):
    clock = pygame.time.Clock()
    bouncing_balls = False
    balls = ballbg.create_balls(width, height, bouncing_balls)
    change_run = True
    username_text = TextInput("Username", max_string_length=36)
    password_text1 = TextInput("New Password", max_string_length=36)
    password_text2 = TextInput("Confirm New Password", max_string_length=36)
    username_typing = False
    password_typing1 = False
    password_typing2 = False
    display = None
    while change_run:
        clock.tick(fps)
        mouse_pos = pygame.mouse.get_pos()
        for ball in balls:
            ball.move(balls)
        events = pygame.event.get()
        balls = ballbg.add_balls(events, width, height, balls, bouncing_balls)
        username_box, password_box1, password_box2, change_box = draw_change(win, width, height, balls, username_typing,
                                                                             password_typing1, password_typing2, display)
        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if username_box.collidepoint(mouse_pos):
                    username_typing = True
                    password_typing1 = False
                    password_typing2 = False
                    if username_text.get_text() == "Username":
                        username_text.clear_text()
                elif password_box1.collidepoint(mouse_pos):
                    password_typing1 = True
                    password_typing2 = False
                    username_typing = False
                    if password_text1.get_text() == "New Password":
                        password_text1.clear_text()
                    password_text1.password = True
                elif password_box2.collidepoint(mouse_pos):
                    password_typing2 = True
                    password_typing1 = False
                    username_typing = False
                    if password_text2.get_text() == "Confirm New Password":
                        password_text2.clear_text()
                    password_text2.password = True
                else:
                    username_typing = False
                    password_typing1 = False
                    password_typing2 = False

                if change_box.collidepoint(mouse_pos):
                    if not users.is_user(username_text.get_text()):
                        display = "There is no account with this username"
                    else:
                        if password_text1.get_text() != password_text2.get_text():
                            display = "The passwords do not match"
                        else:
                            try:
                                users.change_password(username_text.get_text(), password_text1.get_text())
                                users.store()
                                display = "Successful, you are being redirected..."
                                draw_change(win, width, height, balls, username_typing, password_typing1, password_typing2, display)
                                pygame.display.update()
                                pygame.time.delay(2000)
                                change_run = False
                            except:
                                display = "There was an error, Try again."

        if password_text1.get_text() == "" and not password_typing1:
            password_text1.input_string = "New Password"
            password_text1.password = False
        if password_text2.get_text() == "" and not password_typing2:
            password_text2.input_string = "Confirm New Password"
            password_text2.password = False
        if username_text.get_text() == "" and not username_typing:
            username_text.input_string = "Username"

        username_text.update(events, username_typing)
        win.blit(username_text.get_surface(),
                 (width // 2 - 250 + 20, 300 + 30 - username_text.get_surface().get_height() // 2))
        password_text1.update(events, password_typing1)
        win.blit(password_text1.get_surface(),
                 (width // 2 - 250 + 20, 400 + 30 - password_text1.get_surface().get_height() // 2))
        password_text2.update(events, password_typing2)
        win.blit(password_text2.get_surface(),
                 (width // 2 - 250 + 20, 500 + 30 - password_text2.get_surface().get_height() // 2))

        pygame.display.update()


def main(win, width, height, fps):
    if os.path.isfile(os.path.join(PARENT, "users.obj")):
        users = pickle.load(open("users.obj", "rb"))
    else:
        users = Users("users.obj")
        users.store()

    login_run = True
    bouncing_balls = False
    balls = ballbg.create_balls(width, height, bouncing_balls)
    clock = pygame.time.Clock()
    username_text = TextInput("Username", max_string_length=36)
    password_text = TextInput("Password", max_string_length=36)
    username_typing = False
    password_typing = False
    status = "idle"
    while login_run:
        clock.tick(fps)
        for ball in balls:
            ball.move(balls)
        username_box, password_box, create_box, change_box = draw_window(win, width, height, balls, username_typing,
                                                                         password_typing, status)
        mouse_pos = pygame.mouse.get_pos()
        events = pygame.event.get()
        balls = ballbg.add_balls(events, width, height, balls, bouncing_balls)
        for event in events:
            if event.type == pygame.QUIT:
                login_run = False
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if username_box.collidepoint(mouse_pos):
                    username_typing = True
                    password_typing = False
                    if username_text.get_text() == "Username":
                        username_text.clear_text()
                elif password_box.collidepoint(mouse_pos):
                    password_typing = True
                    username_typing = False
                    if password_text.get_text() == "Password":
                        password_text.clear_text()
                    password_text.password = True
                else:
                    username_typing = False
                    password_typing = False
                if change_box.collidepoint(mouse_pos):
                    change_password(win, width, height, users, fps)
                    users = pickle.load(open("users.obj", "rb"))
                elif create_box.collidepoint(mouse_pos):
                    create_account(win, width, height, users, fps)
                    users = pickle.load(open("users.obj", "rb"))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if validate_user(users, username_text.get_text(), password_text.get_text()):
                    import home
                else:
                    status = "invalid"

        if password_text.get_text() == "" and not password_typing:
            password_text.input_string = "Password"
            password_text.password = False
        if username_text.get_text() == "" and not username_typing:
            username_text.input_string = "Username"

        username_text.update(events, username_typing)
        win.blit(username_text.get_surface(),
                 (width // 2 - 250 + 20, 400 + 30 - username_text.get_surface().get_height() // 2))
        password_text.update(events, password_typing)
        win.blit(password_text.get_surface(),
                 (width // 2 - 250 + 20, 500 + 30 - password_text.get_surface().get_height() // 2))
        pygame.display.update()
