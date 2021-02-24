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

import os

import pygame

pygame.init()

'''Images'''
WPAWN = pygame.transform.scale(pygame.image.load(
    os.path.join("project_files", "Chess", "assets", "wpawn.png")), (70, 90))
WKNIGHT = pygame.transform.scale(pygame.image.load(
    os.path.join("project_files", "Chess", "assets", "wknight.png")), (90, 90))
WBISHOP = pygame.transform.scale(pygame.image.load(
    os.path.join("project_files", "Chess", "assets", "wbishop.png")), (90, 90))
WROOK = pygame.transform.scale(pygame.image.load(
    os.path.join("project_files", "Chess", "assets", "wrook.png")), (80, 80))
WQUEEN = pygame.transform.scale(pygame.image.load(
    os.path.join("project_files", "Chess", "assets", "wqueen.png")), (90, 90))
WKING = pygame.transform.scale(pygame.image.load(
    os.path.join("project_files", "Chess", "assets", "wking.png")), (90, 90))
BPAWN = pygame.transform.scale(pygame.image.load(
    os.path.join("project_files", "Chess", "assets", "bpawn.png")), (70, 90))
BKNIGHT = pygame.transform.scale(pygame.image.load(
    os.path.join("project_files", "Chess", "assets", "bknight.png")), (90, 90))
BBISHOP = pygame.transform.scale(pygame.image.load(
    os.path.join("project_files", "Chess", "assets", "bbishop.png")), (90, 90))
BROOK = pygame.transform.scale(pygame.image.load(
    os.path.join("project_files", "Chess", "assets", "brook.png")), (80, 80))
BQUEEN = pygame.transform.scale(pygame.image.load(
    os.path.join("project_files", "Chess", "assets", "bqueen.png")), (90, 90))
BKING = pygame.transform.scale(pygame.image.load(
    os.path.join("project_files", "Chess", "assets", "bking.png")), (90, 90))
ICON = pygame.image.load(os.path.join("project_files", "Chess", "assets", "icon.png"))

'''Constants'''
WIDTH = 800
FPS = 30
CLOCK = pygame.time.Clock()
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
MOVES_SURF = pygame.Surface((WIDTH, WIDTH), pygame.SRCALPHA)
pygame.display.set_caption("Chess, By: Arjun Sahlot")
pygame.display.set_icon(ICON)

'''Colors'''
GREEN = (125, 147, 93)
WHITE = (235, 235, 211)
YELLOW = (245, 242, 148)
YELLOWGREEN = (190, 200, 89)
GREY = (0, 0, 0, 50)


class Cell:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.x = (WIDTH // 8) * col
        self.y = (WIDTH // 8) * row
        self.color = color
        self.old_color = color
        self.selected = None

    def change_pos(self, row, col):
        self.row = row
        self.col = col
        self.x = (WIDTH // 8) * col
        self.y = (WIDTH // 8) * row

    def get_pos(self):
        return self.row, self.col

    def select(self, cells):
        for row in cells:
            for cell in row:
                cell.selected = False
                cell.reset()

        self.selected = True

    def reset(self):
        self.color = self.old_color

    def draw(self, window):
        if self.selected:
            if self.color == WHITE:
                self.color = YELLOW
            elif self.color == GREEN:
                self.color = YELLOWGREEN
        window.fill(self.color, rect=(self.x, self.y, (WIDTH // 8), (WIDTH // 8)))


class Piece:
    def __init__(self, row, col, image, name, color):
        self.row = row
        self.col = col
        self.x = (WIDTH // 8) * col
        self.y = (WIDTH // 8) * row
        self.image = image
        self.name = name
        self.color = color

    def change_pos(self, new_row, new_col):
        self.row = new_row
        self.col = new_col
        self.x = (WIDTH // 8) * self.col
        self.y = (WIDTH // 8) * self.row

    def get_pos(self):
        return self.row, self.col

    def get_color(self):
        return self.color

    def get_opposite_color(self):
        if self.color == "WHITE":
            return "BLACK"
        elif self.color == "BLACK":
            return "WHITE"

    def draw(self, window):
        if self.image != "nothing":
            window.blit(self.image, (self.x +
                                     ((WIDTH // 8) - self.image.get_width()) // 2,
                                     self.y + ((WIDTH // 8) - self.image.get_height()) // 2))

    def draw_moves(self, window, moves):
        MOVES_SURF.fill((0, 0, 0, 0))
        for row, col in moves:
            x, y = rowcol_to_xy((row, col))
            pygame.draw.circle(
                MOVES_SURF, GREY, (x + 50, y + 50), 25)

    def __repr__(self):
        return self.name

    def possible_moves(self, board, flipped):
        moves = []
        pawncol = self.color
        if flipped:
            pawncol = "WHITE" if self.color == "BLACK" else "BLACK"
        # Rooks
        if self.name == "ROOK" or self.name == "QUEEN":
            # Down
            for row in range(self.row + 1, 8):
                if self.color == board[row][self.col].color:
                    break
                moves.append((row, self.col))
                if self.color == board[row][self.col].get_opposite_color():
                    break
            # Up
            for row in range(self.row - 1, -1, -1):
                if self.color == board[row][self.col].color:
                    break
                moves.append((row, self.col))
                if self.color == board[row][self.col].get_opposite_color():
                    break
            # Right
            for col in range(self.col + 1, 8):
                if self.color == board[self.row][col].color:
                    break
                moves.append((self.row, col))
                if self.color == board[self.row][col].get_opposite_color():
                    break
            # Left
            for col in range(self.col - 1, -1, -1):
                if self.color == board[self.row][col].color:
                    break
                moves.append((self.row, col))
                if self.color == board[self.row][col].get_opposite_color():
                    break

        # Bishops
        if self.name == "BISHOP" or self.name == "QUEEN":
            for row in range(self.row + 1, 8):
                try:
                    if self.color == board[row][self.col + (row - self.row)].color:
                        break
                    moves.append((row, self.col + (row - self.row)))
                    if self.color == board[row][self.col + (row - self.row)].get_opposite_color():
                        break
                except IndexError:
                    continue

            for row in range(self.row - 1, -1, -1):
                try:
                    if self.color == board[row][self.col + (row - self.row)].color:
                        break
                    moves.append((row, self.col + (row - self.row)))
                    if self.color == board[row][self.col + (row - self.row)].get_opposite_color():
                        break
                except IndexError:
                    continue

            for row in range(self.row + 1, 8):
                try:
                    if self.color == board[row][self.col - (row - self.row)].color:
                        break
                    moves.append((row, self.col - (row - self.row)))
                    if self.color == board[row][self.col - (row - self.row)].get_opposite_color():
                        break
                except IndexError:
                    continue

            for row in range(self.row - 1, -1, -1):
                try:
                    if self.color == board[row][self.col - (row - self.row)].color:
                        break
                    moves.append((row, self.col - (row - self.row)))
                    if self.color == board[row][self.col - (row - self.row)].get_opposite_color():
                        break
                except IndexError:
                    continue

        # Queens are incorporated with rooks and bishops

        # Kings
        if self.name == "KING":
            if self.row != 0:
                if self.col != 0:
                    if self.color != board[self.row - 1][self.col - 1].color:
                        moves.append((self.row - 1, self.col - 1))
                if self.color != board[self.row - 1][self.col].color:
                    moves.append((self.row - 1, self.col))
                if self.col != 7:
                    if self.color != board[self.row - 1][self.col + 1].color:
                        moves.append((self.row - 1, self.col + 1))

            if self.col != 0:
                if self.color != board[self.row][self.col - 1].color:
                    moves.append((self.row, self.col - 1))

            if self.col != 7:
                if self.color != board[self.row][self.col + 1].color:
                    moves.append((self.row, self.col + 1))

            if self.row != 7:
                if self.col != 0:
                    if self.color != board[self.row + 1][self.col - 1].color:
                        moves.append((self.row + 1, self.col - 1))
                if self.color != board[self.row + 1][self.col].color:
                    moves.append((self.row + 1, self.col))
                if self.col != 7:
                    if self.color != board[self.row + 1][self.col + 1].color:
                        moves.append((self.row + 1, self.col + 1))

        # Knights
        if self.name == "KNIGHT":
            for row in board:
                for spot in row:
                    if (abs(spot.get_pos()[0] - self.row) == 2 and abs(spot.get_pos()[1] - self.col) == 1) or \
                            (abs(spot.get_pos()[0] - self.row) == 1 and abs(spot.get_pos()[1] - self.col) == 2) and \
                            spot.color != self.color:
                        moves.append(spot.get_pos())

        # Pawns
        if self.name == "PAWN":
            if pawncol == "BLACK":
                if self.col != 0:
                    if self.color == board[self.row + 1][self.col - 1].get_opposite_color():
                        moves.append((self.row + 1, self.col - 1))
                if self.col != 7:
                    if self.color == board[self.row + 1][self.col + 1].get_opposite_color():
                        moves.append((self.row + 1, self.col + 1))
                if self.row == 1:
                    for row in range(self.row + 1, self.row + 3):
                        if board[row][self.col].name != "nothing":
                            break
                        moves.append((row, self.col))
                else:
                    if board[self.row + 1][self.col].name == "nothing":
                        moves.append((self.row + 1, self.col))
            else:
                if self.col != 0:
                    if self.color == board[self.row - 1][self.col - 1].get_opposite_color():
                        moves.append((self.row - 1, self.col - 1))
                if self.col != 7:
                    if self.color == board[self.row - 1][self.col + 1].get_opposite_color():
                        moves.append((self.row - 1, self.col + 1))
                if self.row == 6:
                    for row in range(self.row - 1, self.row - 3, -1):
                        if board[row][self.col].name != "nothing":
                            break
                        moves.append((row, self.col))
                else:
                    if board[self.row - 1][self.col].name == "nothing":
                        moves.append((self.row - 1, self.col))

        return moves


def flip_board(board, cells):
    newboard = []
    newcells = []

    for i in range(8):
        newboard.append([])
        for j in range(8):
            newboard[i].append(board[abs(i - 7)][j])

    for i in range(8):
        newcells.append([])
        for j in range(8):
            newcells[i].append(cells[abs(i - 7)][j])

    return newboard, newcells


def make_board():
    board = []

    for row in range(8):
        board.append([])
        for col in range(8):
            # Rooks
            if row == 0 and (col == 7 or col == 0):
                board[row].append(Piece(row, col, BROOK, "ROOK", "BLACK"))
            elif row == 7 and (col == 0 or col == 7):
                board[row].append(Piece(row, col, WROOK, "ROOK", "WHITE"))
            # Knights
            elif row == 0 and (col == 6 or col == 1):
                board[row].append(Piece(row, col, BKNIGHT, "KNIGHT", "BLACK"))
            elif row == 7 and (col == 1 or col == 6):
                board[row].append(Piece(row, col, WKNIGHT, "KNIGHT", "WHITE"))
            # Bishops
            elif row == 0 and (col == 5 or col == 2):
                board[row].append(Piece(row, col, BBISHOP, "BISHOP", "BLACK"))
            elif row == 7 and (col == 2 or col == 5):
                board[row].append(Piece(row, col, WBISHOP, "BISHOP", "WHITE"))
            # Queens
            elif row == 0 and col == 3:
                board[row].append(Piece(row, col, BQUEEN, "QUEEN", "BLACK"))
            elif row == 7 and col == 3:
                board[row].append(Piece(row, col, WQUEEN, "QUEEN", "WHITE"))
            # Kings
            elif row == 0 and col == 4:
                board[row].append(Piece(row, col, BKING, "KING", "BLACK"))
            elif row == 7 and col == 4:
                board[row].append(Piece(row, col, WKING, "KING", "WHITE"))
            # Pawns
            elif row == 1:
                board[row].append(Piece(row, col, BPAWN, "PAWN", "BLACK"))
            elif row == 6:
                board[row].append(Piece(row, col, WPAWN, "PAWN", "WHITE"))
            else:
                board[row].append(
                    Piece(row, col, "nothing", "nothing", "nothing"))

    return board


def update_board(board, cells):
    for i in range(8):
        for j in range(8):
            board[i][j].change_pos(i, j)
            cells[i][j].change_pos(i, j)

    return board, cells


def king_pos(board, color):
    for row in board:
        for piece in row:
            if piece.name == "KING" and piece.color == color:
                return piece.get_pos()


def king_in_check(board, color, flipped):
    for row in board:
        for piece in row:
            if piece.get_opposite_color() == color:
                if king_pos(board, color) in piece.possible_moves(board, flipped):
                    return True
    return False


def refine_moves(board, moves, piece, flipped):
    rem = []

    for pos in moves:
        tmpboard = copy(board)
        tmpboard[piece.row][piece.col] = Piece(
            piece.row, piece.col, "nothing", "nothing", "nothing")
        tmpboard[pos[0]][pos[1]] = piece
        if king_in_check(tmpboard, piece.color, flipped):
            rem.append(pos)

    for r in rem:
        moves.remove(r)

    return moves


def copy(board):
    newboard = []
    for row in board:
        newboard.append([])
        for piece in row:
            newboard[piece.get_pos()[0]].append(piece)

    return newboard


def make_cells():
    cells = []
    for row in range(8):
        cells.append([])
        for col in range(8):
            if row % 2 == 0:
                cells[row].append(
                    Cell(row, col, WHITE if col % 2 == 0 else GREEN))
            else:
                cells[row].append(
                    Cell(row, col, WHITE if col % 2 == 1 else GREEN))

    return cells


def xy_to_rowcol(xy):
    x, y = xy
    return y // (WIDTH // 8), x // (WIDTH // 8)


def rowcol_to_xy(rowcol):
    row, col = rowcol
    return col * (WIDTH // 8), row * (WIDTH // 8)


def draw_cells(window, cells):
    for row in cells:
        for cell in row:
            cell.draw(window)


def reset_moves_surf():
    MOVES_SURF.fill((0, 0, 0, 0))


def draw_window(window, board, cells):
    draw_cells(window, cells)

    for row in board:
        for piece in row:
            piece.draw(window)

    window.blit(MOVES_SURF, (0, 0))


def main(window):
    board = make_board()
    cells = make_cells()
    moving = False
    run = True
    flipped = False
    turn = "WHITE"
    while run:
        draw_window(window, board, cells)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()

            mouseRow, mouseCol = xy_to_rowcol(pygame.mouse.get_pos())

            for row in range(8):
                for col in range(8):
                    piece = board[row][col]
                    cell = cells[row][col]
                    if cell.selected and turn == piece.color:
                        piece_moves = refine_moves(board, piece.possible_moves(board, flipped), piece, flipped)
                        piece.draw_moves(window, piece_moves)
                        if event.type == pygame.MOUSEBUTTONDOWN and moving:
                            moving = False
                            mouseRow, mouseCol = xy_to_rowcol(
                                pygame.mouse.get_pos())
                            reset_moves_surf()
                            if (mouseRow, mouseCol) in piece_moves:
                                board[mouseRow][mouseCol] = piece
                                board[row][col] = Piece(
                                    row, col, "nothing", "nothing", "nothing")
                                if turn == "WHITE":
                                    turn = "BLACK"
                                else:
                                    turn = "WHITE"
                                # board = flip_board(board, cells)[0]
                                # cells = flip_board(board, cells)[1]
                                # flipped = True if flipped == False else False

            if event.type == pygame.MOUSEBUTTONDOWN and not moving:
                cells[mouseRow][mouseCol].select(cells)
                if board[mouseRow][mouseCol].color == turn:
                    moving = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    board = flip_board(board, cells)[0]
                    cells = flip_board(board, cells)[1]
                    flipped = True if flipped == False else False

            board = update_board(board, cells)[0]
            cells = update_board(board, cells)[1]
            pygame.display.update()

    pygame.quit()


main(WINDOW)
