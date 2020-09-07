import os
import random

import pygame

# Constants
pygame.init()
WIDTH, HEIGHT = 1200, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('comicsans', 30)
visfont = pygame.font.SysFont('comicsans', 40)
pygame.display.set_caption("Sorting Visualizer, By: Arjun Sahlot")
TOPBARHEIGHT = 80

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
TURQUOISE = (0, 255, 166)


# Functions
def generate_pillars(n):
    return [[random.randrange(100, 700), WHITE] for _ in range(n)]


def pillar_width_gap(n):
    global pillargap, pillarwidth
    pillargap = 3 if n < 200 else 0
    pillarwidth = round((WIDTH - 20 - n * pillargap) / n)
    return pillarwidth, pillargap


def display_window(window, pillars):
    global circle_x, TOPBARHEIGHT, vis_button, merge_button, insertion_button, selection_button, quick_button, bubble_button, merge_col, insertion_col, selection_col, bubble_col, quick_col, generate_col, generate_button
    window.fill((0, 0, 0))
    if algorithm == "Selection":
        selection_col = RED
    elif algorithm == "Bubble":
        bubble_col = RED
    elif algorithm == "Insertion":
        insertion_col = RED
    elif algorithm == "Quick":
        quick_col = RED
    elif algorithm == "Merge":
        merge_col = RED
    # draw top bar
    window.fill(GREY, rect=(0, 0, WIDTH, TOPBARHEIGHT))
    # draw text
    vis_text = visfont.render("Visualize!", 1, vis_col)
    window.blit(vis_text,
                (WIDTH // 2 - vis_text.get_width() // 2, TOPBARHEIGHT // 2 - vis_text.get_height() // 2))

    merge_text = font.render("Merge", 1, merge_col)
    window.blit(merge_text,
                (WIDTH // 2 + vis_text.get_width() // 2 + 20, TOPBARHEIGHT // 2 - merge_text.get_height() // 2))

    insertion_text = font.render("Insertion", 1, insertion_col)
    window.blit(insertion_text, (WIDTH // 2 + vis_text.get_width() // 2 + merge_text.get_width() + 40,
                                 TOPBARHEIGHT // 2 - insertion_text.get_height() // 2))

    selection_text = font.render("Selection", 1, selection_col)
    window.blit(selection_text, (
        WIDTH // 2 + vis_text.get_width() // 2 + merge_text.get_width() + insertion_text.get_width() + 60,
        TOPBARHEIGHT // 2 - selection_text.get_height() // 2))

    quick_text = font.render("Quick", 1, quick_col)
    window.blit(quick_text, (
        WIDTH // 2 + vis_text.get_width() // 2 + merge_text.get_width() + insertion_text.get_width() + selection_text.get_width() + 80,
        TOPBARHEIGHT // 2 - quick_text.get_height() // 2))

    bubble_text = font.render("Bubble", 1, bubble_col)
    window.blit(bubble_text, (
        WIDTH // 2 + vis_text.get_width() // 2 + merge_text.get_width() + insertion_text.get_width() + selection_text.get_width() + quick_text.get_width() + 100,
        TOPBARHEIGHT // 2 - bubble_text.get_height() // 2))

    generate_text = font.render("Generate New Set", 1, generate_col)
    window.blit(generate_text, (40, TOPBARHEIGHT // 2 - merge_text.get_height() // 2))

    # draw button around text
    vis_button = pygame.draw.rect(window, vis_col, (
        WIDTH // 2 - vis_text.get_width() // 2 - 5, TOPBARHEIGHT // 2 - vis_text.get_height() // 2 - 3,
        vis_text.get_width() + 10, vis_text.get_height() + 6), 3)

    merge_button = pygame.draw.rect(window, merge_col, (
        WIDTH // 2 + vis_text.get_width() // 2 + 15, TOPBARHEIGHT // 2 - merge_text.get_height() // 2 - 3,
        merge_text.get_width() + 10, merge_text.get_height() + 6), 3)

    insertion_button = pygame.draw.rect(window, insertion_col, (
        WIDTH // 2 + vis_text.get_width() // 2 + merge_text.get_width() + 35,
        TOPBARHEIGHT // 2 - insertion_text.get_height() // 2 - 3,
        insertion_text.get_width() + 10, insertion_text.get_height() + 6), 3)

    selection_button = pygame.draw.rect(window, selection_col, (
        WIDTH // 2 + vis_text.get_width() // 2 + merge_text.get_width() + insertion_text.get_width() + 55,
        TOPBARHEIGHT // 2 - selection_text.get_height() // 2 - 3,
        selection_text.get_width() + 10, selection_text.get_height() + 6), 3)

    quick_button = pygame.draw.rect(window, quick_col, (
        WIDTH // 2 + vis_text.get_width() // 2 + merge_text.get_width() + insertion_text.get_width() + selection_text.get_width() + 75,
        TOPBARHEIGHT // 2 - quick_text.get_height() // 2 - 3,
        quick_text.get_width() + 10, quick_text.get_height() + 6), 3)

    bubble_button = pygame.draw.rect(window, bubble_col, (
        WIDTH // 2 + vis_text.get_width() // 2 + merge_text.get_width() + insertion_text.get_width() + selection_text.get_width() + quick_text.get_width() + 95,
        TOPBARHEIGHT // 2 - bubble_text.get_height() // 2 - 3,
        bubble_text.get_width() + 10, bubble_text.get_height() + 6), 3)

    generate_button = pygame.draw.rect(window, generate_col, (
        40 - 5, TOPBARHEIGHT // 2 - generate_text.get_height() // 2 - 3, generate_text.get_width() + 10,
        generate_text.get_height() + 6), 3)

    # draw slider
    pygame.draw.rect(window, WHITE, (generate_text.get_width() + 75, TOPBARHEIGHT // 2 - 5, 230, 10))
    pygame.draw.circle(window, RED, (circle_x, TOPBARHEIGHT // 2), 8)

    # draw pillars
    for i in range(len(pillars)):
        window.fill(pillars[i][1],
                    rect=(10 + i * (pillarwidth + pillargap), pillars[i][0], pillarwidth, HEIGHT - pillars[i][0]))
    pygame.display.update()


def update_pillars(window, pillars, swap1, swap2, merge=False):
    pygame.time.delay(75)
    for i in range(len(pillars)):
        if not merge:
            if swap1 == pillars[i]:
                pillars[i][1] = RED
            elif swap2 == pillars[i]:
                pillars[i][1] = GREEN
    if merge:
        pillars[swap1][1] = RED
        pillars[swap2][1] = GREEN

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display_window(window, pillars)

    for i in range(len(pillars)):
        pillars[i][1] = WHITE

    if pygame.mouse.get_pressed()[2]:
        main(window)


def finish(window, pillars):
    for value in pillars:
        value[1] = TURQUOISE

    display_window(window, pillars)


def selection_sort(window, pillars):
    for i in range(len(pillars)):
        min_idx = i
        for j in range(i + 1, len(pillars)):
            if pillars[j] < pillars[min_idx]:
                min_idx = j
        pillars[i], pillars[min_idx] = pillars[min_idx], pillars[i]
        update_pillars(window, pillars, pillars[i], pillars[min_idx])


def bubble_sort(window, pillars):
    for i in range(len(pillars)):
        for j in range(len(pillars) - 1 - i):
            if pillars[j] > pillars[j + 1]:
                pillars[j], pillars[j + 1] = pillars[j + 1], pillars[j]
            update_pillars(window, pillars, pillars[j], pillars[j + 1])


def insertion_sort(window, pillars):
    for i in range(len(pillars)):
        cursor = pillars[i]
        idx = i
        while idx > 0 and pillars[idx - 1] > cursor:
            pillars[idx] = pillars[idx - 1]
            idx -= 1
        pillars[idx] = cursor
        update_pillars(window, pillars, pillars[idx], pillars[i])


def partition(window, pillars, start, end):
    x = pillars[end]
    i = start - 1
    for j in range(start, end + 1, 1):
        if pillars[j] <= x:
            i += 1
            if i < j:
                pillars[i], pillars[j] = pillars[j], pillars[i]
                update_pillars(window, pillars, pillars[i], pillars[j])
    return i


def quick_sort(window, pillars, start, end):
    if start < end:
        pivot = partition(window, pillars, start, end)
        quick_sort(window, pillars, start, pivot - 1)
        quick_sort(window, pillars, pivot + 1, end)


def merge(window, pillars, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = pillars[left + i][0]

    for j in range(0, n2):
        R[j] = pillars[middle + 1 + j][0]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            pillars[k][0] = L[i]
            i += 1
        else:
            pillars[k][0] = R[j]
            j += 1
        k += 1

    while i < n1:
        pillars[k][0] = L[i]
        i += 1
        k += 1

    while j < n2:
        pillars[k][0] = R[j]
        j += 1
        k += 1

    update_pillars(window, pillars, left, right, True)


def merge_sort(window, pillars, left, right):
    if left < right:
        mid = (left + (right - 1)) // 2
        merge_sort(window, pillars, left, mid)
        merge_sort(window, pillars, mid + 1, right)
        merge(window, pillars, left, mid, right)


def main(window):
    global pillarwidth, pillargap, vis_col, merge_col, insertion_col, selection_col, bubble_col, quick_col, algorithm, generate_col, circle_x
    n = 120
    pillars = generate_pillars(n)
    # get pillar width and gap
    pillarwidth, pillargap = pillar_width_gap(len(pillars))
    circle_x = n*23//50 + 250
    run = True
    algorithm = None
    vis_col, merge_col, insertion_col, selection_col, bubble_col, quick_col, generate_col = (
        BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE)

    while run:
        display_window(window, pillars)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
            if vis_button.collidepoint(pygame.mouse.get_pos()):
                vis_col = RED
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if algorithm == "Selection":
                        selection_sort(window, pillars)
                        finish(window, pillars)
                    elif algorithm == "Bubble":
                        bubble_sort(window, pillars)
                        finish(window, pillars)
                    elif algorithm == "Insertion":
                        insertion_sort(window, pillars)
                        finish(window, pillars)
                    elif algorithm == "Quick":
                        quick_sort(window, pillars, 0, n - 1)
                        finish(window, pillars)
                    elif algorithm == "Merge":
                        merge_sort(window, pillars, 0, n - 1)
                        finish(window, pillars)
            else:
                vis_col = BLUE

            if merge_button.collidepoint(pygame.mouse.get_pos()):
                merge_col = RED
                if event.type == pygame.MOUSEBUTTONDOWN:
                    algorithm = "Merge"
            else:
                merge_col = BLUE

            if quick_button.collidepoint(pygame.mouse.get_pos()):
                quick_col = RED
                if event.type == pygame.MOUSEBUTTONDOWN:
                    algorithm = "Quick"
            else:
                quick_col = BLUE

            if selection_button.collidepoint(pygame.mouse.get_pos()):
                selection_col = RED
                if event.type == pygame.MOUSEBUTTONDOWN:
                    algorithm = "Selection"
            else:
                selection_col = BLUE

            if insertion_button.collidepoint(pygame.mouse.get_pos()):
                insertion_col = RED
                if event.type == pygame.MOUSEBUTTONDOWN:
                    algorithm = "Insertion"
            else:
                insertion_col = BLUE

            if bubble_button.collidepoint(pygame.mouse.get_pos()):
                bubble_col = RED
                if event.type == pygame.MOUSEBUTTONDOWN:
                    algorithm = "Bubble"
            else:
                bubble_col = BLUE

            if generate_button.collidepoint(pygame.mouse.get_pos()):
                generate_col = RED
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pillars = generate_pillars(round((circle_x - 250) * 50 / 23))
                    pillarwidth, pillargap = pillar_width_gap(len(pillars))
            else:
                generate_col = BLUE

            mouseX, mouseY = pygame.mouse.get_pos()
            if 250 < mouseX < 480 and TOPBARHEIGHT // 2 - 8 < mouseY < TOPBARHEIGHT // 2 + 8:
                if True in pygame.mouse.get_pressed():
                    circle_x = mouseX

        pygame.display.update()

    pygame.quit()


# Run
main(WINDOW)
