import pygame
import random


def main():
    FPS = 30
    WHITE = (255, 255, 255)
    GRAY = (150, 150, 150)
    LIGHTGRAY = (200, 200, 200)
    GREEN = (0, 200, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    DARKBLUE = (0, 0, 50)
    DARKGREEN = (0, 50, 0)
    DARKRED = (50, 0, 0)
    DARKGRAY = (50, 50, 50)
    W = 320
    H = 450
    wid = 8
    hig = 8
    m = 10
    pygame.init()
    sc = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 25)
    color = [WHITE, BLUE, GREEN, RED, DARKBLUE, DARKGREEN, DARKRED, DARKGRAY, BLACK]
    stat = 0
    pygame.display.set_caption("Sapper")

    def flag(x, y):
        pygame.draw.line(sc, BLACK, [34 + x * 20, 23 + y * 20], [34 + x * 20, 37 + y * 20], 1)
        pygame.draw.polygon(sc, RED,
                            [[33 + x * 20, 23 + y * 20], [23 + x * 20, 27 + y * 20], [33 + x * 20, 31 + y * 20]])
        pygame.display.update()

    def mine(x, y, W, H):
        pygame.draw.polygon(sc, WHITE, [[21 + x * 20, 21 + y * 20], [21 + x * 20, 39 + y * 20],
                                        [39 + x * 20, 39 + y * 20], [39 + x * 20, 21 + y * 20]])
        pygame.draw.circle(sc, RED, [31 + x * 20, 31 + y * 20], 7)
        pygame.draw.circle(sc, BLACK, [31 + x * 20, 31 + y * 20], 8, 1)
        pygame.display.update()
        pygame.time.delay(500)
        fint = pygame.font.Font(None, 50)
        pygame.draw.polygon(sc, (50, 50, 50), [[(W // 2) - 100, (H // 2) - 50], [(W // 2) - 100, (H // 2) + 50],
                                               [(W // 2) + 100, (H // 2) + 50], [(W // 2) + 100, (H // 2) - 50]])
        text = fint.render("Game Over!", True, RED)
        sc.blit(text, [(W // 2) - 96, (H // 2) - 20])
        pygame.display.update()

    def question(x, y):
        pygame.draw.polygon(sc, GRAY, [[21 + x * 20, 21 + y * 20], [21 + x * 20, 39 + y * 20],
                                       [39 + x * 20, 39 + y * 20], [39 + x * 20, 21 + y * 20]])
        text = font.render('?', True, BLACK)
        sc.blit(text, [26 + 20 * x, 22 + 20 * y])
        pygame.display.update()

    def drawn(x, y):
        for i in range(x):
            for j in range(y):
                pygame.draw.polygon(sc, BLACK, [[20 + 20 * i, 20 + 20 * j], [20 + 20 * i, 40 + 20 * j],
                                                [40 + 20 * i, 40 + 20 * j], [40 + 20 * i, 20 + 20 * j]], 1)
                pygame.draw.polygon(sc, GRAY, [[21 + 20 * i, 21 + 20 * j], [21 + 20 * i, 39 + 20 * j],
                                               [39 + 20 * i, 39 + 20 * j], [39 + 20 * i, 21 + 20 * j]])
                pygame.display.update()

    class Field:
        def __init__(self, x_, y_, n_):
            self.x = x_
            self.y = y_
            self.n = n_
            self.field = [[0 for i in range(y_)] for j in range(x_)]
            self.status = [[0 for i in range(y_)] for j in range(x_)]
            self.count = x_ * y_ - n_
            c = 0
            while c < n_:
                xx = random.randint(0, x_ - 1)
                yy = random.randint(0, y_ - 1)
                if self.field[xx][yy] == 0:
                    self.field[xx][yy] = 9
                    c += 1
            for i in range(x_):
                for j in range(y_):
                    if self.field[i][j] != 9:
                        if i == 0:
                            if j == 0:
                                for t in range(2):
                                    for s in range(2):
                                        if self.field[t][s] == 9:
                                            self.field[i][j] += 1
                            elif j == y_ - 1:
                                for t in range(2):
                                    for s in range(y_ - 2, y_):
                                        if self.field[t][s] == 9:
                                            self.field[i][j] += 1
                            else:
                                for t in range(2):
                                    for s in range(j - 1, j + 2):
                                        if self.field[t][s] == 9:
                                            self.field[i][j] += 1
                        elif i == x_ - 1:
                            if j == 0:
                                for t in range(x_ - 2, x_):
                                    for s in range(2):
                                        if self.field[t][s] == 9:
                                            self.field[i][j] += 1
                            elif j == y_ - 1:
                                for t in range(x_ - 2, x_):
                                    for s in range(y_ - 2, y_):
                                        if self.field[t][s] == 9:
                                            self.field[i][j] += 1
                            else:
                                for t in range(x_ - 2, x_):
                                    for s in range(j - 1, j + 2):
                                        if self.field[t][s] == 9:
                                            self.field[i][j] += 1
                        else:
                            if j == 0:
                                for t in range(i - 1, i + 2):
                                    for s in range(2):
                                        if self.field[t][s] == 9:
                                            self.field[i][j] += 1
                            elif j == y_ - 1:
                                for t in range(i - 1, i + 2):
                                    for s in range(y_ - 2, y_):
                                        if self.field[t][s] == 9:
                                            self.field[i][j] += 1
                            else:
                                for t in range(i - 1, i + 2):
                                    for s in range(j - 1, j + 2):
                                        if self.field[t][s] == 9:
                                            self.field[i][j] += 1

        def num(self, c, x, y, color):
            pygame.draw.polygon(sc, WHITE,
                                [[21 + x * 20, 21 + y * 20], [21 + x * 20, 39 + y * 20], [39 + x * 20, 39 + y * 20],
                                 [39 + x * 20, 21 + y * 20]])
            text = font.render(str(c), True, color)
            sc.blit(text, [26 + 20 * x, 22 + 20 * y])
            pygame.display.update()
            self.count -= 1

        def zero(self, i, j):
            if i == 0:
                if j == 0:
                    for t in range(2):
                        for s in range(2):
                            if 0 <= t < self.x and 0 <= s < self.y:
                                if 0 <= self.field[t][s] <= 8 and self.status[t][s] == 0:
                                    self.num(self.field[t][s], t, s, color[self.field[t][s]])
                                    self.status[t][s] = 1
                                    if self.field[t][s] == 0:
                                        self.zero(t, s)
                elif j == self.y - 1:
                    for t in range(2):
                        for s in range(self.y - 2, self.y):
                            if 0 <= t < self.x and 0 <= s < self.y:
                                if 0 <= self.field[t][s] <= 8 and self.status[t][s] == 0:
                                    self.num(self.field[t][s], t, s, color[self.field[t][s]])
                                    self.status[t][s] = 1
                                    if self.field[t][s] == 0:
                                        self.zero(t, s)
                else:
                    for t in range(2):
                        for s in range(j - 1, j + 2):
                            if 0 <= t < self.x and 0 <= s < self.y:
                                if 0 <= self.field[t][s] <= 8 and self.status[t][s] == 0:
                                    self.num(self.field[t][s], t, s, color[self.field[t][s]])
                                    self.status[t][s] = 1
                                    if self.field[t][s] == 0:
                                        self.zero(t, s)
            elif i == self.x - 1:
                if j == 0:
                    for t in range(self.x - 2, self.x):
                        for s in range(2):
                            if 0 <= t < self.x and 0 <= s < self.y:
                                if 0 <= self.field[t][s] <= 8 and self.status[t][s] == 0:
                                    self.num(self.field[t][s], t, s, color[self.field[t][s]])
                                    self.status[t][s] = 1
                                    if self.field[t][s] == 0:
                                        self.zero(t, s)
                elif j == self.y - 1:
                    for t in range(self.x - 2, self.x):
                        for s in range(self.y - 2, self.y):
                            if 0 <= t < self.x and 0 <= s < self.y:
                                if 0 <= self.field[t][s] <= 8 and self.status[t][s] == 0:
                                    self.num(self.field[t][s], t, s, color[self.field[t][s]])
                                    self.status[t][s] = 1
                                    if self.field[t][s] == 0:
                                        self.zero(t, s)
                else:
                    for t in range(self.x - 2, self.x):
                        for s in range(j - 1, j + 2):
                            if 0 <= t < self.x and 0 <= s < self.y:
                                if 0 <= self.field[t][s] <= 8 and self.status[t][s] == 0:
                                    self.num(self.field[t][s], t, s, color[self.field[t][s]])
                                    self.status[t][s] = 1
                                    if self.field[t][s] == 0:
                                        self.zero(t, s)
            else:
                if j == 0:
                    for t in range(i - 1, i + 2):
                        for s in range(2):
                            if 0 <= t < self.x and 0 <= s < self.y:
                                if 0 <= self.field[t][s] <= 8 and self.status[t][s] == 0:
                                    self.num(self.field[t][s], t, s, color[self.field[t][s]])
                                    self.status[t][s] = 1
                                    if self.field[t][s] == 0:
                                        self.zero(t, s)
                elif j == self.y - 1:
                    for t in range(i - 1, i + 2):
                        for s in range(self.y - 2, self.y):
                            if 0 <= t < self.x and 0 <= s < self.y:
                                if 0 <= self.field[t][s] <= 8 and self.status[t][s] == 0:
                                    self.num(self.field[t][s], t, s, color[self.field[t][s]])
                                    self.status[t][s] = 1
                                    if self.field[t][s] == 0:
                                        self.zero(t, s)
                else:
                    for t in range(i - 1, i + 2):
                        for s in range(j - 1, j + 2):
                            if 0 <= t < self.x and 0 <= s < self.y:
                                if 0 <= self.field[t][s] <= 8 and self.status[t][s] == 0:
                                    self.num(self.field[t][s], t, s, color[self.field[t][s]])
                                    self.status[t][s] = 1
                                    if self.field[t][s] == 0:
                                        self.zero(t, s)

        def leftclick(self, x_, y_):
            if self.status[x_][y_] == 0:
                if 0 < self.field[x_][y_] <= 8:
                    self.num(self.field[x_][y_], x_, y_, color[self.field[x_][y_]])
                elif self.field[x_][y_] == 0:
                    self.zero(x_, y_)
                else:
                    mine(x_, y_, W, H)
                self.status[x_][y_] = 1
            elif self.status[x_][y_] == 2:
                question(x_, y_)
                self.status[x_][y_] = 3
            elif self.status[x_][y_] == 3:
                pygame.draw.polygon(sc, GRAY, [[21 + x_ * 20, 21 + y_ * 20], [21 + x_ * 20, 39 + y_ * 20],
                                               [39 + x_ * 20, 39 + y_ * 20], [39 + x_ * 20, 21 + y_ * 20]])
                pygame.display.update()
                self.status[x_][y_] = 0

        def rightclick(self, x_, y_):
            if self.status[x_][y_] == 0:
                flag(x_, y_)
                self.status[x_][y_] = 2
            elif self.status[x_][y_] == 2:
                question(x_, y_)
                self.status[x_][y_] = 3
            elif self.status[x_][y_] == 3:
                pygame.draw.polygon(sc, GRAY, [[21 + x_ * 20, 21 + y_ * 20], [21 + x_ * 20, 39 + y_ * 20],
                                               [39 + x_ * 20, 39 + y_ * 20], [39 + x_ * 20, 21 + y_ * 20]])
                pygame.display.update()
                self.status[x_][y_] = 0

    sc.fill((100, 0, 255))
    Fon = pygame.font.Font(None, 50)
    pygame.draw.polygon(sc, GRAY, [[20, 20], [300, 20], [300, 430], [20, 430]])
    pygame.draw.rect(sc, LIGHTGRAY, (60, 80, 200, 90))
    pygame.draw.rect(sc, LIGHTGRAY, (60, 190, 200, 90))
    pygame.draw.rect(sc, LIGHTGRAY, (60, 300, 200, 90))
    txt = Fon.render("Choose level", True, BLACK)
    sc.blit(txt, [45, 30])
    eas = Fon.render("Easy", True, GREEN)
    hard = Fon.render("Hard", True, RED)
    med = Fon.render("Medium", True, BLUE)
    sc.blit(eas, [115, 110])
    sc.blit(med, [95, 220])
    sc.blit(hard, [115, 330])
    pygame.display.update()
    dic = True
    while dic:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= i.pos[0] <= 250 and 70 <= i.pos[1] <= 160:
                    wid = 8
                    hig = 8
                    m = 10
                    W = 200
                    H = 240
                    dic = False
                elif 50 <= i.pos[0] <= 250 and 190 <= i.pos[1] <= 270:
                    wid = 16
                    hig = 16
                    W = 360
                    H = 400
                    m = 40
                    dic = False
                elif 50 <= i.pos[0] <= 250 and 290 <= i.pos[1] <= 380:
                    wid = 30
                    hig = 16
                    W = 640
                    H = 400
                    m = 99
                    dic = False
    Game = Field(wid, hig, m)
    sc = pygame.display.set_mode((W, H))
    sc.fill((100, 0, 255))
    drawn(wid, hig)
    pygame.draw.rect(sc, DARKBLUE, (20, H - 50, 70, 30))
    pygame.draw.rect(sc, DARKBLUE, (110, H - 50, 70, 30))
    Fon = pygame.font.Font(None, 27)
    Res = Fon.render("Restart", True, GREEN)
    Ex = Fon.render("Exit", True, RED)
    sc.blit(Res, [23, H - 43])
    sc.blit(Ex, [127, H - 43])
    pygame.display.update()
    GM = True
    while GM:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                x = (i.pos[0] - 20) // 20
                y = (i.pos[1] - 20) // 20
                if 0 <= x <= wid - 1 and 0 <= y <= hig - 1:
                    if i.button == 1:
                        Game.leftclick(x, y)
                    elif i.button == 3:
                        Game.rightclick(x, y)
                elif 20 <= i.pos[0] <= 90 and H - 50 <= i.pos[1] <= H - 20 and i.button == 1:
                    main()
                elif 110 <= i.pos[0] <= 180 and H - 50 <= i.pos[1] <= H - 20 and i.button == 1:
                    GM = False
            if Game.count == 0:
                fint = pygame.font.Font(None, 50)
                pygame.draw.polygon(sc, (50, 50, 50), [[(W // 2) - 100, (H // 2) - 50], [(W // 2) - 100, (H // 2) + 50],
                                                       [(W // 2) + 100, (H // 2) + 50],
                                                       [(W // 2) + 100, (H // 2) - 50]])
                text = fint.render("You Win!", True, GREEN)
                sc.blit(text, [(W // 2) - 70, (H // 2) - 20])
                pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    exit()
