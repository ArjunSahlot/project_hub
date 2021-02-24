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

import pygame

def draw_back_button(win, image):
    pygame.draw.line(win, (0, 0, 0), (10, 60), (70, 25), 5)
    pygame.draw.line(win, (0, 0, 0), (10, 60), (70, 95), 5)
    box = pygame.draw.rect(win, (0, 0, 0), (80, 10, 100, 100), 5)
    image = pygame.transform.scale(image, (80, 80))
    win.blit(image, (90, 20))

    return box
