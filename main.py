from Game import *


def main():
    game = Game()
    game.Field.screen = pygame.display.set_mode((game.Field.screen_width, game.Field.screen_height))
    game.screen.fill((100, 0, 255))
    game.start_field_draw()
    pygame.draw.rect(game.screen, DARKBLUE, (20, game.screen_height - 50, 70, 30))
    pygame.draw.rect(game.screen, DARKBLUE, (110, game.screen_height - 50, 70, 30))
    medium_font = pygame.font.Font(None, 27)
    restart_text = medium_font.render("Restart", True, GREEN)
    exit_text = medium_font.render("Exit", True, RED)
    game.screen.blit(restart_text, [23, game.screen_height - 43])
    game.screen.blit(exit_text, [127, game.screen_height - 43])
    pygame.display.update()
    game_status = True
    while game_status:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    stat = game.left_click(i.pos[0], i.pos[1])
                    if stat:
                        main()
                elif i.button == 3:
                    game.right_click(i.pos[0], i.pos[1])
            if game.Field.count == 0:
                pygame.draw.polygon(game.screen, (50, 50, 50),
                                    [[(game.screen_width // 2) - 100, (game.screen_height // 2) - 50],
                                     [(game.screen_width // 2) - 100, (game.screen_height // 2) + 50],
                                     [(game.screen_width // 2) + 100, (game.screen_height // 2) + 50],
                                     [(game.screen_width // 2) + 100, (game.screen_height // 2) - 50]])
                win_text = big_font.render("You Win!", True, GREEN)
                game.screen.blit(win_text, [(game.screen_width // 2) - 70, (game.screen_height // 2) - 20])
                pygame.display.update()
