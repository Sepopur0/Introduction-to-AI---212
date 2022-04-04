from funcs import *


def main():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Search simulate")
    res = everything(screen)
    while True:
        if res[2] == -4:
            res=everything(screen)
        elif res[2] in range(0, 19):
            res = cheat_algori(screen, 5-res[0], res[1], res[2])


def everything(screen):
    screen.fill(black)
    step_1 = menu(screen, ["Hitori 5x5", "Hashi 7x7", "Quit"])
    zone = pygame.Surface((500, 500))
    zone.fill(black)
    choice = create_gamescreen(zone, screen, step_1)
    act = -1
    s_1 = pygame.Surface((150, 50))
    pygame.draw.rect(s_1, yellow, pygame.Rect(
        0, 0, button_width, button_height), 0, 40)
    pygame.Surface.set_alpha(s_1, 100)
    pau = False
    cheatactiv = -1
    trupos = -1
    while True:
        for ev in pygame.event.get():
            if ev.type == MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                act = checkbox(mousepos, gamebutton_coor)
                if (act > 0 and not(pau)) or act == 0 or act == 5:
                    screen.blit(s_1, (1000, 100+75*act))
            elif ev.type == MOUSEBUTTONUP:
                if act == 0:
                    pau = not(pau)
                    if pau:
                        drawbutton(screen, "Resume", 1000, 100)
                        screen.blit(font.render("Game is paused",
                                    False, white), (575, 580))
                    else:
                        drawbutton(screen, "Pause", 1000, 100)
                        screen.blit(font.render("Game is paused",
                                    False, black), (575, 580))
                elif act == 1 and not(pau):
                    drawbutton(screen, "Refresh", 1000, 175)
                    zone.fill(black)
                    pygame.draw.rect(zone, white, (5, 5, 490, 490), 5)
                    if step_1 == 5:
                        choice = draw_hitori(zone)
                    else:
                        choice = draw_hashi(zone)
                    for i in range(0, 5):
                        for ev in pygame.event.get():
                            if ev.type == pygame.QUIT:
                                sys.exit()
                        pygame.Surface.set_alpha(zone, 80+i*35)
                        screen.blit(zone, (400, 75))
                        pygame.display.update()
                        pygame.time.delay(200)
                    zone.set_alpha(255)
                    pygame.display.update()
                elif act == 2 or act == 3 and not(pau):
                    cheatactiv = act
                    break
                elif act == 4:
                    return [0, 0, -4]
                elif act == 5:
                    sys.exit()
            elif ev.type == pygame.QUIT:
                sys.exit()
            pygame.display.update()
        if cheatactiv != -1:
            break
    return cheat_algori(screen, act, step_1, choice)

if __name__ == "__main__":
    main()
