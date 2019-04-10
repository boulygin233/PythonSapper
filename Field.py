import random
from config import *
import pygame

pygame.init()
small_font = pygame.font.Font(None, 25)
big_font = pygame.font.Font(None, 50)


class Field:
    def __init__(self, field_width, field_height, mine_number, screen_width, screen_height):
        """
        Creator of Field
        """
        self.width = field_width
        self.height = field_height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
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

    def num_draw(self, num_coord_x, num_coord_y, num_color):
        """
        Draws numbers on field in open cells
        """
        pygame.draw.polygon(self.screen, WHITE,
                            [[21 + num_coord_x * 20, 21 + num_coord_y * 20],
                             [21 + num_coord_x * 20, 39 + num_coord_y * 20],
                             [39 + num_coord_x * 20, 39 + num_coord_y * 20],
                             [39 + num_coord_x * 20, 21 + num_coord_y * 20]])
        num_text = small_font.render(str(self.field[num_coord_x][num_coord_y]), True, num_color)
        self.screen.blit(num_text, [26 + 20 * num_coord_x, 22 + 20 * num_coord_y])
        pygame.display.update()
        self.status[num_coord_x][num_coord_y] = 1
        self.count -= 1

    def mine_draw(self, mine_coord_x, mine_coord_y):
        """
        Draws mine and Game Over text
        """
        pygame.draw.polygon(self.screen, WHITE, [[21 + mine_coord_x * 20, 21 + mine_coord_y * 20],
                                                 [21 + mine_coord_x * 20, 39 + mine_coord_y * 20],
                                                 [39 + mine_coord_x * 20, 39 + mine_coord_y * 20],
                                                 [39 + mine_coord_x * 20, 21 + mine_coord_y * 20]])
        pygame.draw.circle(self.screen, RED, [31 + mine_coord_x * 20, 31 + mine_coord_y * 20], 7)
        pygame.draw.circle(self.screen, BLACK, [31 + mine_coord_x * 20, 31 + mine_coord_y * 20], 8, 1)
        pygame.display.update()
        pygame.time.delay(500)
        pygame.draw.polygon(self.screen, (50, 50, 50),
                            [[(self.screen_width // 2) - 100, (self.screen_height // 2) - 50],
                             [(self.screen_width // 2) - 100, (self.screen_height // 2) + 50],
                             [(self.screen_width // 2) + 100, (self.screen_height // 2) + 50],
                             [(self.screen_width // 2) + 100, (self.screen_height // 2) - 50]])
        game_over_text = big_font.render("Game Over!", True, RED)
        self.screen.blit(game_over_text, [(self.screen_width // 2) - 96, (self.screen_height // 2) - 20])
        pygame.display.update()
        self.status[mine_coord_x][mine_coord_y] = 1

    def flag_draw(self, flag_coord_x, flag_coord_y):
        """
        Draws Flags, where player pressed the right button
        """
        pygame.draw.line(self.screen, BLACK, [34 + flag_coord_x * 20, 23 + flag_coord_y * 20],
                         [34 + flag_coord_x * 20, 37 + flag_coord_y * 20], 1)
        pygame.draw.polygon(self.screen, RED, [[33 + flag_coord_x * 20, 23 + flag_coord_y * 20],
                                               [23 + flag_coord_x * 20, 27 + flag_coord_y * 20],
                                               [33 + flag_coord_x * 20, 31 + flag_coord_y * 20]])
        pygame.display.update()
        self.status[flag_coord_x][flag_coord_y] = 2

    def question_draw(self, question_coord_x, question_coord_y):
        """
         Draws Question signs, where player pressed the button, if earlier there was Flag
        """
        pygame.draw.polygon(self.screen, GRAY, [[21 + question_coord_x * 20, 21 + question_coord_y * 20],
                                                [21 + question_coord_x * 20, 39 + question_coord_y * 20],
                                                [39 + question_coord_x * 20, 39 + question_coord_y * 20],
                                                [39 + question_coord_x * 20, 21 + question_coord_y * 20]])
        question_text = small_font.render('?', True, BLACK)
        self.screen.blit(question_text, [26 + 20 * question_coord_x, 22 + 20 * question_coord_y])
        pygame.display.update()
        self.status[question_coord_x][question_coord_y] = 3

    def zero_finder(self, last_zero_coord_x, last_zero_coord_y):
        """
        Opens all zeros and other numbers adjacent to cell with zero
        """
        if last_zero_coord_x == 0:
            x_iter = (0, 1)
        elif last_zero_coord_x == self.width - 1:
            x_iter = (last_zero_coord_x - 1, last_zero_coord_x)
        else:
            x_iter = (last_zero_coord_x - 1, last_zero_coord_x, last_zero_coord_x + 1)
        if last_zero_coord_y == 0:
            y_iter = (0, 1)
        elif last_zero_coord_y == self.height - 1:
            y_iter = (last_zero_coord_y - 1, last_zero_coord_y)
        else:
            y_iter = (last_zero_coord_y - 1, last_zero_coord_y, last_zero_coord_y + 1)
        for t in x_iter:
            for s in y_iter:
                if 0 <= t < self.width and 0 <= s < self.height:
                    if 0 <= self.field[t][s] <= 8 and not self.status[t][s]:
                        self.num_draw(t, s, color[self.field[t][s]])
                        self.status[t][s] = 1
                        if self.field[t][s] == 0:
                            self.zero_finder(t, s)

