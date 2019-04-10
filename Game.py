from Field import *
from config import *
import pygame


class Game:
    pygame.display.set_caption("Sapper")

    def __init__(self):
        """
        Create Game
        """
        self.screen_width = 320
        self.screen_height = 450
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.screen.fill(VIOLET)
        pygame.draw.polygon(self.screen, GRAY, [[20, 20], [300, 20], [300, 430], [20, 430]])
        pygame.draw.rect(self.screen, LIGHTGRAY, (60, 80, 200, 90))
        pygame.draw.rect(self.screen, LIGHTGRAY, (60, 190, 200, 90))
        pygame.draw.rect(self.screen, LIGHTGRAY, (60, 300, 200, 90))
        choose_lvl_text = big_font.render("Choose level", True, BLACK)
        self.screen.blit(choose_lvl_text, [45, 30])
        easy_text = big_font.render("Easy", True, GREEN)
        hard_text = big_font.render("Hard", True, RED)
        medium_text = big_font.render("Medium", True, BLUE)
        self.screen.blit(easy_text, [115, 110])
        self.screen.blit(medium_text, [95, 220])
        self.screen.blit(hard_text, [115, 330])
        pygame.display.update()
        dic = True
        while dic:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= i.pos[0] <= 250 and 70 <= i.pos[1] <= 160:
                        self.field_width = 8
                        self.field_height = 8
                        self.mine_number = 10
                        self.screen_width = 200
                        self.screen_height = 240
                        dic = False
                    elif 50 <= i.pos[0] <= 250 and 190 <= i.pos[1] <= 270:
                        self.field_width = 16
                        self.field_height = 16
                        self.screen_width = 360
                        self.screen_height = 400
                        self.mine_number = 40
                        dic = False
                    elif 50 <= i.pos[0] <= 250 and 290 <= i.pos[1] <= 380:
                        self.field_width = 30
                        self.field_height = 16
                        self.screen_width = 640
                        self.screen_height = 400
                        self.mine_number = 99
                        dic = False
        self.Field = Field(self.field_width, self.field_height, self.mine_number)

    def num_draw(self, num_coord_x, num_coord_y, num_color):
        """
        Draws numbers on field in open cells
        """
        pygame.draw.polygon(self.screen, WHITE,
                            [[21 + num_coord_x * 20, 21 + num_coord_y * 20],
                             [21 + num_coord_x * 20, 39 + num_coord_y * 20],
                             [39 + num_coord_x * 20, 39 + num_coord_y * 20],
                             [39 + num_coord_x * 20, 21 + num_coord_y * 20]])
        num_text = small_font.render(str(self.Field.field[num_coord_x][num_coord_y]), True, num_color)
        self.screen.blit(num_text, [26 + 20 * num_coord_x, 22 + 20 * num_coord_y])
        pygame.display.update()
        self.Field.status[num_coord_x][num_coord_y] = 1
        self.Field.count -= 1

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
        self.Field.status[mine_coord_x][mine_coord_y] = 1

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
        self.Field.status[flag_coord_x][flag_coord_y] = 2

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
        self.Field.status[question_coord_x][question_coord_y] = 3

    def zero_finder(self, last_zero_coord_x, last_zero_coord_y):
        """
        Opens all zeros and other numbers adjacent to cell with zero
        """
        if last_zero_coord_x == 0:
            x_iter = (0, 1)
        elif last_zero_coord_x == self.field_width - 1:
            x_iter = (last_zero_coord_x - 1, last_zero_coord_x)
        else:
            x_iter = (last_zero_coord_x - 1, last_zero_coord_x, last_zero_coord_x + 1)
        if last_zero_coord_y == 0:
            y_iter = (0, 1)
        elif last_zero_coord_y == self.field_height - 1:
            y_iter = (last_zero_coord_y - 1, last_zero_coord_y)
        else:
            y_iter = (last_zero_coord_y - 1, last_zero_coord_y, last_zero_coord_y + 1)
        for t in x_iter:
            for s in y_iter:
                if 0 <= t < self.field_width and 0 <= s < self.field_height:
                    if 0 <= self.Field.field[t][s] <= 8 and not self.Field.status[t][s]:
                        self.num_draw(t, s, color[self.Field.field[t][s]])
                        self.Field.status[t][s] = 1
                        if self.Field.field[t][s] == 0:
                            self.zero_finder(t, s)

    def left_click(self, click_position_x, click_position_y):
        """
        Handles click on left mouse button and calls desired function
        """
        if 20 <= click_position_x <= 20 * (self.field_width + 1) and 20 <= click_position_y <= 20 * (
                self.field_height + 1):
            cell_click_x = (click_position_x - 20) // 20
            cell_click_y = (click_position_y - 20) // 20
            if 0 <= cell_click_x <= self.field_width - 1 and 0 <= cell_click_y <= self.field_height - 1:
                if self.Field.status[cell_click_x][cell_click_y] == 0:
                    if 0 < self.Field.field[cell_click_x][cell_click_y] <= 8:
                        self.num_draw(cell_click_x, cell_click_y,
                                      color[self.Field.field[cell_click_x][cell_click_y]])
                    elif self.Field.field[cell_click_x][cell_click_y] == 0:
                        self.zero_finder(cell_click_x, cell_click_y)
                    else:
                        self.mine_draw(cell_click_x, cell_click_y)
                elif self.Field.status[cell_click_x][cell_click_y] == 2:
                    self.question_draw(cell_click_x, cell_click_y)
                elif self.Field.status[cell_click_x][cell_click_y] == 3:
                    pygame.draw.polygon(self.screen, GRAY, [[21 + cell_click_x * 20, 21 + cell_click_y * 20],
                                                            [21 + cell_click_x * 20, 39 + cell_click_y * 20],
                                                            [39 + cell_click_x * 20, 39 + cell_click_y * 20],
                                                            [39 + cell_click_x * 20, 21 + cell_click_y * 20]])
                    pygame.display.update()
                    self.Field.status[cell_click_x][cell_click_y] = 0
        elif 20 <= click_position_x <= 90 and self.screen_height - 50 <= click_position_y <= self.screen_height - 20:
            return 1
        elif 110 <= click_position_x <= 180 and self.screen_height - 50 <= click_position_y <= self.screen_height - 20:
            exit()
        return 0

    def right_click(self, click_position_x, click_position_y):
        """
        Handles click on right mouse button and calls desired function
        """
        if 20 <= click_position_x <= 20 * (self.field_width + 1) and 20 <= click_position_y <= 20 * (
                self.field_height + 1):
            cell_click_x = (click_position_x - 20) // 20
            cell_click_y = (click_position_y - 20) // 20
            if 0 <= cell_click_x <= self.field_width - 1 and 0 <= cell_click_y <= self.field_height - 1:
                if self.Field.status[cell_click_x][cell_click_y] == 0:
                    self.flag_draw(cell_click_x, cell_click_y)
                elif self.Field.status[cell_click_x][cell_click_y] == 2:
                    self.question_draw(cell_click_x, cell_click_y)
                elif self.Field.status[cell_click_x][cell_click_y] == 3:
                    pygame.draw.polygon(self.screen, GRAY, [[21 + cell_click_x * 20, 21 + cell_click_y * 20],
                                                            [21 + cell_click_x * 20, 39 + cell_click_y * 20],
                                                            [39 + cell_click_x * 20, 39 + cell_click_y * 20],
                                                            [39 + cell_click_x * 20, 21 + cell_click_y * 20]])
                    pygame.display.update()
                    self.Field.status[cell_click_x][cell_click_y] = 0

    def start_field_draw(self):
        """
        Draws closed field
        """
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill(VIOLET)
        for i in range(self.field_width):
            for j in range(self.field_height):
                pygame.draw.polygon(self.screen, BLACK, [[20 + 20 * i, 20 + 20 * j], [20 + 20 * i, 40 + 20 * j],
                                                         [40 + 20 * i, 40 + 20 * j], [40 + 20 * i, 20 + 20 * j]], 1)
                pygame.draw.polygon(self.screen, GRAY, [[21 + 20 * i, 21 + 20 * j], [21 + 20 * i, 39 + 20 * j],
                                                        [39 + 20 * i, 39 + 20 * j], [39 + 20 * i, 21 + 20 * j]])
                pygame.display.update()

    def run(self):
        """
        Starts and runs the game
        """
        self.screen.fill(VIOLET)
        self.start_field_draw()
        pygame.draw.rect(self.screen, DARKBLUE, (20, self.screen_height - 50, 70, 30))
        pygame.draw.rect(self.screen, DARKBLUE, (110, self.screen_height - 50, 70, 30))
        medium_font = pygame.font.Font(None, 27)
        restart_text = medium_font.render("Restart", True, GREEN)
        exit_text = medium_font.render("Exit", True, RED)
        self.screen.blit(restart_text, [23, self.screen_height - 43])
        self.screen.blit(exit_text, [127, self.screen_height - 43])
        pygame.display.update()
        game_status = True
        while game_status:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1:
                        stat = self.left_click(i.pos[0], i.pos[1])
                        if stat:
                            self.__init__()
                            self.run()
                    elif i.button == 3:
                        self.right_click(i.pos[0], i.pos[1])
                if self.Field.count == 0:
                    pygame.draw.polygon(self.screen, (50, 50, 50),
                                        [[(self.screen_width // 2) - 100, (self.screen_height // 2) - 50],
                                         [(self.screen_width // 2) - 100, (self.screen_height // 2) + 50],
                                         [(self.screen_width // 2) + 100, (self.screen_height // 2) + 50],
                                         [(self.screen_width // 2) + 100, (self.screen_height // 2) - 50]])
                    win_text = big_font.render("You Win!", True, GREEN)
                    self.screen.blit(win_text, [(self.screen_width // 2) - 70, (self.screen_height // 2) - 20])
                    pygame.display.update()
