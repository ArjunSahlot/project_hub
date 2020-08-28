import os
import pygame
import time
import solver
from assets import sudokugenerator as generate


def flatten(blahblahblah):
    for item in blahblahblah:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


def printBoard():
    window.blit(BOARD, (0, 0))
    for cell in celldata.values():
        picture = True
        if cell[2] == 1:
            picture = ONE
            cell[1] = False
        elif cell[2] == 2:
            picture = TWO
            cell[1] = False
        elif cell[2] == 3:
            picture = THREE
            cell[1] = False
        elif cell[2] == 4:
            picture = FOUR
            cell[1] = False
        elif cell[2] == 5:
            picture = FIVE
            cell[1] = False
        elif cell[2] == 6:
            picture = SIX
            cell[1] = False
        elif cell[2] == 7:
            picture = SEVEN
            cell[1] = False
        elif cell[2] == 8:
            picture = EIGTH
            cell[1] = False
        elif cell[2] == 9:
            picture = NINE
            cell[1] = False
        else:
            cell[1] = True
        if picture != True:
            window.blit(picture, (cell[0][0] + 3.5, cell[0][1] + 3.5))
            os.system("cls")

        window.blit(SOLVE_BUT, (850, 1000))


def pointsConverter(points=(0, 0, 0, 0)):  # converts a rect described top-left(x,y), bottom-right(x,y) into top-left(x,y), width, heigth
    return points[0], points[1], points[2] - points[0], points[3] - points[1]


def getNum(cellnum):  # gets the number input and saves it in the board

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_1]:
        board[cellnum - 1] = 1
        celldata[cellnum][2] = 1
    if pressed[pygame.K_2]:
        board[cellnum - 1] = 2
        celldata[cellnum][2] = 2
    if pressed[pygame.K_3]:
        board[cellnum - 1] = 3
        celldata[cellnum][2] = 3
    if pressed[pygame.K_4]:
        board[cellnum - 1] = 4
        celldata[cellnum][2] = 4
    if pressed[pygame.K_5]:
        board[cellnum - 1] = 5
        celldata[cellnum][2] = 5
    if pressed[pygame.K_6]:
        board[cellnum - 1] = 6
        celldata[cellnum][2] = 6
    if pressed[pygame.K_7]:
        board[cellnum - 1] = 7
        celldata[cellnum][2] = 7
    if pressed[pygame.K_8]:
        board[cellnum - 1] = 8
        celldata[cellnum][2] = 8
    if pressed[pygame.K_9]:
        board[cellnum - 1] = 9
        celldata[cellnum][2] = 9
    if pressed[pygame.K_BACKSPACE] or pressed[pygame.K_0] or pressed[pygame.K_SPACE]:
        board[cellnum - 1] = 0
        celldata[cellnum][2] = 0


def init():
    global BOTTOM_LEN, WIDTH, HEIGHT, window, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGTH, NINE, SOLVE_BUT, unflatBoard, BOARD, board
    BOTTOM_LEN = 50
    WIDTH = 1000
    HEIGHT = 1000 + BOTTOM_LEN
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku, By: Arjun Sahlot")
    pygame.display.set_icon(pygame.image.load(os.path.join("assets", "sudoku_icon.png")))
    ONE = pygame.image.load(os.path.join("assets", "1.png"))
    TWO = pygame.image.load(os.path.join("assets", "2.png"))
    THREE = pygame.image.load(os.path.join("assets", "3.png"))
    FOUR = pygame.image.load(os.path.join("assets", "4.png"))
    FIVE = pygame.image.load(os.path.join("assets", "5.png"))
    SIX = pygame.image.load(os.path.join("assets", "6.png"))
    SEVEN = pygame.image.load(os.path.join("assets", "7.png"))
    EIGTH = pygame.image.load(os.path.join("assets", "8.png"))
    NINE = pygame.image.load(os.path.join("assets", "9.png"))
    BOARD = pygame.transform.scale(pygame.image.load(os.path.join("assets", "sudoku_board.png")),
                                   (WIDTH, HEIGHT - BOTTOM_LEN))
    SOLVE_BUT = pygame.image.load(os.path.join("assets", "solve_button.png"))  # 136 by 45
    unflatBoard = generate.best(generate.run())
    board = list(flatten(unflatBoard))  # board that gets generated


init()

# contains positions of all the cells[topleftX,topleftY,bottomrightX,bottomrightY], if they have a number in them(
# useful for highlighting), and the number it contains
celldata = {
    1: [[9, 9, 114, 114], True],
    2: [[116, 9, 223, 114], True],
    3: [[225, 9, 330, 114], True],
    4: [[340, 9, 444, 114], True],
    5: [[447, 9, 555, 114], True],
    6: [[556, 9, 662, 114], True],
    7: [[672, 9, 774, 114], True],
    8: [[776, 9, 887, 114], True],
    9: [[888, 9, 992, 114], True],
    10: [[9, 117, 114, 223], True],
    11: [[116, 117, 223, 223], True],
    12: [[225, 117, 330, 223], True],
    13: [[340, 117, 445, 223], True],
    14: [[447, 117, 555, 223], True],
    15: [[556, 117, 663, 223], True],
    16: [[672, 117, 776, 223], True],
    17: [[776, 117, 886, 223], True],
    18: [[888, 117, 992, 223], True],
    19: [[9, 225, 114, 332], True],
    20: [[116, 225, 224, 332], True],
    21: [[225, 225, 332, 332], True],
    22: [[340, 225, 444, 332], True],
    23: [[447, 225, 555, 331], True],
    24: [[556, 225, 660, 332], True],
    25: [[672, 225, 774, 332], True],
    26: [[776, 225, 886, 332], True],
    27: [[888, 225, 993, 332], True],
    28: [[9, 340, 114, 445], True],
    29: [[116, 340, 223, 445], True],
    30: [[225, 340, 330, 445], True],
    31: [[340, 340, 445, 445], True],
    32: [[447, 340, 555, 445], True],
    33: [[556, 340, 663, 445], True],
    34: [[672, 340, 776, 445], True],
    35: [[776, 340, 886, 445], True],
    36: [[888, 340, 992, 445], True],
    37: [[9, 447, 114, 554], True],
    38: [[116, 447, 223, 554], True],
    39: [[225, 447, 330, 554], True],
    40: [[340, 447, 445, 554], True],
    41: [[447, 447, 555, 554], True],
    42: [[556, 447, 663, 554], True],
    43: [[672, 447, 776, 554], True],
    44: [[776, 447, 886, 554], True],
    45: [[888, 447, 992, 554], True],
    46: [[9, 557, 114, 662], True],
    47: [[116, 557, 223, 662], True],
    48: [[225, 557, 330, 662], True],
    49: [[340, 557, 445, 662], True],
    50: [[447, 557, 555, 662], True],
    51: [[556, 557, 663, 662], True],
    52: [[672, 557, 776, 662], True],
    53: [[776, 557, 886, 662], True],
    54: [[888, 557, 992, 662], True],
    55: [[9, 669, 114, 775], True],
    56: [[116, 669, 223, 775], True],
    57: [[225, 669, 330, 775], True],
    58: [[340, 669, 445, 775], True],
    59: [[447, 669, 555, 775], True],
    60: [[556, 669, 663, 775], True],
    61: [[672, 669, 776, 775], True],
    62: [[776, 669, 886, 775], True],
    63: [[888, 669, 992, 775], True],
    64: [[9, 778, 114, 886], True],
    65: [[116, 778, 223, 886], True],
    66: [[225, 778, 330, 886], True],
    67: [[340, 778, 445, 886], True],
    68: [[447, 778, 555, 886], True],
    69: [[556, 778, 663, 886], True],
    70: [[672, 778, 776, 886], True],
    71: [[776, 778, 886, 886], True],
    72: [[888, 778, 992, 886], True],
    73: [[9, 889, 114, 993], True],
    74: [[116, 889, 223, 993], True],
    75: [[225, 889, 330, 993], True],
    76: [[340, 889, 445, 993], True],
    77: [[447, 889, 555, 993], True],
    78: [[556, 889, 663, 993], True],
    79: [[672, 889, 776, 993], True],
    80: [[776, 889, 886, 993], True],
    81: [[888, 889, 992, 993], True]
}
# Adds board to celldata
for i in range(len(board)):
    celldata[i + 1].append(board[i])

'''Main Loop'''
run = True
while run:
    printBoard()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouseX, mouseY = pygame.mouse.get_pos()
    '''Highlights the box you are hovering on/clicked'''
    for key, value in celldata.items():
        if value[1]:
            if value[0][0] < mouseX < value[0][2] and value[0][1] < mouseY < value[0][3]:
                window.fill((168, 172, 179), rect=pointsConverter(value[0]))
        if pygame.mouse.get_pressed()[0] and value[0][0] < mouseX < value[0][2] and value[0][1] < mouseY < value[0][3]:
            window.fill((62, 240, 38), rect=pointsConverter(value[0]))
            getNum(key)
        if pygame.mouse.get_pressed()[2] and value[0][0] < mouseX < value[0][2] and value[0][1] < mouseY < value[0][3]:
            board[key - 1] = 0
            celldata[key][2] = 0

    if 850 < mouseX < 986 and mouseY < 1047.5 and mouseY > 1002.5 and pygame.mouse.get_pressed()[0]:
        solver.backtrack(unflatBoard)
        board = list(flatten(unflatBoard))
        solving = True

    pygame.display.update()

pygame.quit()
