import pygame
import os
import re
import random
import numpy as np
import math
import time


'''Functions'''
def letterinsert(letter, tries, userword, theword):
    try:
        notguessedcollection.remove(letter.lower())
    except ValueError:
        return
    if letter.lower() in theword:
        indices = [i for i, y in enumerate(theword) if y == letter.lower()]
        for index in indices:
            userword[index] = letter
    else:
        tries -= 1


def revealletters(lettersrevealed, tries, userword, theword):
    wordlist = list(theword)
    revealedletters = np.random.choice(wordlist,size = lettersrevealed, replace = False)
    for q in revealedletters:
        letterinsert(q, tries, userword, theword)


def display(win = False, lose = False):
    window.fill((255,255,255))
    window.blit(HANGER, (0,0))
    text = font.render(' '.join(userword), 1, (0, 0, 0))
    window.blit(text, (WIDTH//2 - text.get_width()//2, 440))
    window.fill((0,0,0), rect = (0,420, WIDTH, 22))
    for i in letters:
        x,y,letter = i
        if letter.lower() in notguessedcollection:
            pygame.draw.circle(window, (0,0,0), (x,y), radius, 5)
            window.blit(font.render(letter, 1, (0,0,0)), (x - font.render(letter, 1, (0,0,0)).get_width()//2 + 1, y - font.render(letter, 1, (0,0,0)).get_height()//2 + 1))
    if win:
        window.blit(font.render("You Won", 1, (0,0,0)), (WIDTH//2, HEIGHT//2))
        time.sleep(3)
    if lose:
        window.blit(font.render("You Lost", 1, (0,0,0)), (WIDTH//2, HEIGHT//2))
        time.sleep(3)


'''Get words from a a_file'''
a_file = open("dict_for_hangman.txt", "r")

quizwords = []
for line in a_file:
  stripped_line = line.strip()
  quizwords.append(stripped_line)

a_file.close()

'''Setup + Constants'''
pygame.init()
WIDTH, HEIGHT = 1200, 500
window = pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.SysFont('comicsans', 70)
pygame.display.set_caption("Hangman, By: Arjun Sahlot")
pygame.display.set_icon(pygame.image.load(os.path.join("project_files", "Hangman", "assets", "icon.png")))
HANGER = pygame.transform.scale(pygame.image.load(os.path.join("project_files", "Hangman", "assets", "hanger.png")), (250, 430))
print("Before you start please answer the questions below.")
default_letters_min = 7
default_letters_max = 12
default_letters_revealed = 0
defaultsettings = input(f"Do you want to use the default settings: {default_letters_min}-{default_letters_max} letters and {default_letters_revealed} revealed? ")
if defaultsettings.lower() == "y":
    letternum = random.randint(7,12)
    theword = random.choice(quizwords)
    while len(theword) != letternum:
        theword = random.choice(quizwords)
    userword = ['_' for x in range(len(theword))]
    lettersinword = len(set(theword))
    lettersrevealed = 0
    print("Your settings are the following:")
    print(f"{len(theword)} letters")
    print(f"{lettersrevealed} letters revealed")
else:
    letternum = int(input('How many letters should be in the word(max is 28)? '))
    lettersrevealed = int(input(f'How many letters do you want revealed(max is {lettersinword + 3})? ')) + 1
theword = random.choice(quizwords)
while len(theword) != letternum:
    theword = random.choice(quizwords)
userword = ['_' for x in range(len(theword))]
lettersinword = len(set(theword))
notguessedcollection = list('abcdefghijklmnopqrstuvwxyz')
tries = 9
revealletters(lettersrevealed, tries, userword, theword)
fps = 50
gap = 15
radius = 30
letter_startx, letter_starty = 450, radius
letters = []
for i in range(26):
    if i == 21:
        letter_startx += radius*2 + gap
    x = letter_startx + gap*2 +((radius*2 + gap) * (i % 7))
    y = letter_starty + ((i//7) * (gap + radius * 2))
    letter = chr(65+i)
    letters.append([x,y,letter])

pygame.mouse.set_cursor(*pygame.cursors.broken_x)


'''Game Loop'''
run = True
win = False
lose = False

while run:
    display(win, lose)
    pygame.time.Clock().tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouseX, mouseY = pygame.mouse.get_pos()
    for i in letters:
        x,y,l = i
        if math.sqrt((x - mouseX)**2 + (y - mouseY)**2) < radius:
            if pygame.mouse.get_pressed()[0]:
                letterinsert(l.lower(), tries, userword, theword)

    if tries == 0:
        lose = True
    if '_' not in userword:
        win = True


    pygame.display.update()

pygame.quit()
