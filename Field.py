import random
import pygame

pygame.init()
small_font = pygame.font.Font(None, 25)
big_font = pygame.font.Font(None, 50)


class Field:
    def __init__(self, field_width, field_height, mine_number):
        """
        Creator of Field
        """
        self.width = field_width
        self.height = field_height
        self.mines = mine_number
        self.field = [[0 for i in range(field_height)] for j in range(field_width)]
        self.status = [[0 for i in range(field_height)] for j in range(field_width)]
        self.count = self.width * self.height - self.mines
        c = 0
        while c < mine_number:
            mine_coord_x = random.randint(0, field_width - 1)
            mine_coord_y = random.randint(0, field_height - 1)
            if self.field[mine_coord_x][mine_coord_y] == 0:
                self.field[mine_coord_x][mine_coord_y] = 9
                c += 1
        for i in range(field_width):
            for j in range(field_height):
                if self.field[i][j] != 9:
                    if i == 0:
                        x_iter = (0, 1)
                    elif i == self.width - 1:
                        x_iter = (i - 1, i)
                    else:
                        x_iter = (i - 1, i, i + 1)
                    if j == 0:
                        y_iter = (0, 1)
                    elif j == self.height - 1:
                        y_iter = (j - 1, j)
                    else:
                        y_iter = (j - 1, j, j + 1)
                    for t in x_iter:
                        for s in y_iter:
                            if self.field[t][s] == 9:
                                self.field[i][j] += 1

