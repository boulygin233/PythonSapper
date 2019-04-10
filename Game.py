from Field import *
from config import *
from main import *
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
        self.Field = Field(self.field_width, self.field_height, self.mine_number, self.screen_width, self.screen_height)

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
                        self.Field.num_draw(cell_click_x, cell_click_y,
                                            color[self.Field.field[cell_click_x][cell_click_y]])
                    elif self.Field.field[cell_click_x][cell_click_y] == 0:
                        self.Field.zero_finder(cell_click_x, cell_click_y)
                    else:
                        self.Field.mine_draw(cell_click_x, cell_click_y)
                elif self.Field.status[cell_click_x][cell_click_y] == 2:
                    self.Field.question_draw(cell_click_x, cell_click_y)
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
                    self.Field.flag_draw(cell_click_x, cell_click_y)
                elif self.Field.status[cell_click_x][cell_click_y] == 2:
                    self.Field.question_draw(cell_click_x, cell_click_y)
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
        for i in range(self.field_width):
            for j in range(self.field_height):
                pygame.draw.polygon(self.screen, BLACK, [[20 + 20 * i, 20 + 20 * j], [20 + 20 * i, 40 + 20 * j],
                                                         [40 + 20 * i, 40 + 20 * j], [40 + 20 * i, 20 + 20 * j]], 1)
                pygame.draw.polygon(self.screen, GRAY, [[21 + 20 * i, 21 + 20 * j], [21 + 20 * i, 39 + 20 * j],
                                                        [39 + 20 * i, 39 + 20 * j], [39 + 20 * i, 21 + 20 * j]])
                pygame.display.update()

