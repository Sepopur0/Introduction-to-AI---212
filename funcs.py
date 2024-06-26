from data import *
from profiler import hitori_profiler,get_random_board,hashi_profiler
from hashi_funcs.boardstate import load_map
def checkbox(coor, coor_list):
    i = 0
    for lis in coor_list:
        if (coor[0] in range(lis[0], lis[1])) and (coor[1] in range(lis[2], lis[3])):
            return i
        i = i+1
    return -1


def checkpos(pos, modu):
    if modu == 5:
        mod = 60
        if (pos[0] in range(500, 800)) and (pos[1] in range(175, 475)):
            return ((pos[0]-500)//mod)+((pos[1]-175)//mod)*modu
    elif modu == 7 or modu == 10:
        mod = 420//modu
        if (pos[0] in range(440, 860)) and (pos[1] in range(115, 535)):
            return ((pos[0]-440)//mod)+((pos[1]-115)//mod)*modu
    elif modu == 8:
        mod = 60
        if (pos[0] in range(410, 890)) and (pos[1] in range(85, 565)):
            return ((pos[0]-410)//mod)+((pos[1]-85)//mod)*modu
    return -1


def create_gamescreen(zone, screen, step_1):
    screen.fill(black)
    drawbutton(screen, "Pause", 1000, 100)
    drawbutton(screen, "Refresh", 1000, 175)
    drawbutton(screen, "Cheat: DFS", 1000, 250)
    drawbutton(screen, "Cheat: A*", 1000, 325)
    drawbutton(screen, "Home", 1000, 400)
    drawbutton(screen, "Quit", 1000, 475)
    pygame.draw.rect(zone, white, (5, 5, 490, 490), 5)
    matrix = -1
    if step_1 == 5:
        matrix = draw_hitori(zone)
    else:
        matrix = draw_hashi(zone)
    for i in range(0, 10):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()
        pygame.Surface.set_alpha(zone, 85+i*17)
        screen.blit(zone, (400, 75))
        pygame.display.update()
        pygame.time.delay(100)
    zone.set_alpha(255)
    pygame.display.update()
    return matrix


def drawbutton(screen, str, top, left):
    pygame.draw.rect(screen, neon_dark_green, pygame.Rect(
        top, left, button_width, button_height), 0, 40)
    pygame.draw.rect(screen, red_1, pygame.Rect(
        top, left, button_width, button_height), 3, 40)
    screen.blit(font.render(str, False, black), (top+10, left+15))


def draw_hashi(zone, opt=-1):
    choice = -1
    if opt == -1:
        choice = random.randint(0,19)
    else:
        choice = opt
    matrix = load_map( f"board_hashi/{choice}.txt")
    # matrix=hashi_list_norm[choice]
    for i in range(0, 7):
        for j in range(0, 7):
            draw_hashi_element(zone, matrix[i][j], 7*i+j)
    return choice


def draw_hashi_element(zone, number, pos):
    modu = 1
    wid = 1
    modu = 7
    wid = 60
    pygame.draw.rect(zone, black, (40+wid*(pos % modu),
                     40+wid*(pos//modu), wid, wid))
    pygame.draw.line(zone, gray, (40+wid*(pos % modu), 40+wid/2+wid*(pos//modu)),
                     (40+wid+wid*(pos % modu), 40+wid/2+wid*(pos//modu)), 1)
    pygame.draw.line(zone, gray, (40+wid/2+wid*(pos % modu), 40+wid*(pos//modu)),
                     (40+wid/2+wid*(pos % modu), 40+wid+wid*(pos//modu)), 1)
    if number != 0 and number < 10:
        pygame.draw.circle(zone, black, (40+wid/2+wid*(pos %
                           modu), 40+wid/2+wid*(pos//modu)), 20)
        pygame.draw.circle(zone, gray, (40+wid/2+wid*(pos %
                           modu), 40+wid/2+wid*(pos//modu)), 20, 3)
        zone.blit(font_number.render(str(number), False, white),
                  (wid/2+wid*(pos % modu)+33, wid/2+wid*(pos//modu)+26))
    if number == 21:
        pygame.draw.line(zone, gray, (40+wid*(pos % modu), 40+wid/2+wid*(pos//modu)),
                             (40+wid+wid*(pos % modu), 40+wid/2+wid*(pos//modu)), 8)
    elif number == 22:
        pygame.draw.line(zone, gray, (40+wid*(pos % modu), 35+wid/2+wid*(pos//modu)),
                             (40+wid+wid*(pos % modu), 35+wid/2+wid*(pos//modu)), 5)
        pygame.draw.line(zone, gray, (40+wid*(pos % modu), 45+wid/2+wid*(pos//modu)),
                             (40+wid+wid*(pos % modu), 45+wid/2+wid*(pos//modu)), 5)
    elif number == 11:
            pygame.draw.line(zone, gray, (40+wid/2+wid*(pos % modu), 40+wid*(pos//modu)),
                             (40+wid/2+wid*(pos % modu), 40+wid+wid*(pos//modu)), 8)
    elif number == 12:
            pygame.draw.line(zone, gray, (35+wid/2+wid*(pos % modu), 40+wid*(pos//modu)),
                             (35+wid/2+wid*(pos % modu), 40+wid+wid*(pos//modu)), 5)
            pygame.draw.line(zone, gray, (45+wid/2+wid*(pos % modu), 40+wid*(pos//modu)),
                             (45+wid/2+wid*(pos % modu), 40+wid+wid*(pos//modu)), 5)


def draw_hitori(zone, opt=-1):
    choice = -1
    if opt == -1:
        choice = random.randint(0, 19)
    else:
        choice = opt
    matrix = get_random_board(choice)
    for i in range(0, 5):
        for j in range(0, 5):
            draw_hitori_element(zone, matrix[i][j], 5*i+j)
    return choice


def draw_hitori_element(zone, number, pos):  # number is 0 if black box
    if number != 0:
        pygame.draw.rect(zone, white, (100+60*(pos % 5),
                         100+60*(pos//5), 60, 60), 3)
        zone.blit(font_number.render(str(number), False, white),
                  (100+60*(pos % 5)+22, 100+60*(pos//5)+18))
    else:
        pygame.draw.rect(
            zone, gray, (100+60*(pos % 5), 100+60*(pos//5), 60, 60))


def menu(screen, stringlist):  # return 0 for hitori, 1 for hashi
    i = 0
    screen.blit(font_title.render("Not a puzzle game",False,white),(350,100))
    for string in stringlist:
        drawbutton(screen, string, 575, 300+75*i)
        i += 1
    pygame.display.update()
    s_1 = pygame.Surface((150, 50))
    pygame.draw.rect(s_1, yellow, pygame.Rect(
        0, 0, button_width, button_height), 0, 40)
    pygame.Surface.set_alpha(s_1, 100)
    act = -1
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                act = checkbox(mousepos, startbutton_coor)
                if act != -1:
                    screen.blit(s_1, (575, 300+75*act))
            elif ev.type == pygame.MOUSEBUTTONUP:
                if act == 0:
                    return 5
                elif act == 1:
                    return 7
                elif act == 2:
                    sys.exit()
            elif ev.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()


# choice=2 if dfs, 3 if A*; type=5 if hitori, 7 if hashi
def cheat_algori(screen, choice, type, matrixidx):
    screen.fill(black)
    pygame.time.delay(200)
    zone = pygame.Surface((500, 500))
    pygame.draw.rect(zone, white, (5, 5, 490, 490), 5)
    s_1 = pygame.Surface((150, 50))
    pygame.draw.rect(s_1, yellow, pygame.Rect(
        0, 0, button_width, button_height), 0, 40)
    pygame.Surface.set_alpha(s_1, 100)
    if type == 5:
        draw_hitori(zone, matrixidx)
    else:
        draw_hashi(zone, matrixidx)
    screen.blit(zone, (400, 75))
    screen.blit(font.render("Just a minute...", False, white), (575, 590))
    pygame.display.update()
    matrixlist = []
    algo = ""
    runtime = -1
    memused = -1
    if type == 5:
        if choice == 2:  # dfs
            res = hitori_profiler('dfgs', matrixidx)
            algo = "DFS "
            matrixlist = res[0]
            runtime = res[1]
            memused = res[2]
        else:
            res = hitori_profiler('a-star', matrixidx)
            algo = "A* "
            matrixlist = res[0]
            runtime = res[1]
            memused = res[2]
    else:
        if choice==2:
            res=hashi_profiler("dfgs",matrixidx)
            algo= "DFS "
            matrixlist=res[0]
            runtime=res[1]
            memused=res[2]
        else:
            res=hashi_profiler("a-star",matrixidx)
            algo= "A* "
            matrixlist=res[0]
            runtime=res[1]
            memused=res[2]
    drawbutton(screen, "Pause", 1000, 150)
    drawbutton(screen, "Statistic: Off", 1000, 225)
    if choice == 2:
        drawbutton(screen, "Cheat: A*", 1000, 300)
    else:
        drawbutton(screen, "Cheat: DFS", 1000, 300)
    drawbutton(screen, "Home", 1000, 375)
    drawbutton(screen, "Quit", 1000, 450)
    pygame.draw.rect(screen, black, (530, 575, 400, 100))
    pygame.display.update()
    pau = False
    wait = True
    showstat = False
    count = 0
    matrixlen = len(matrixlist)
    idx = -1
    while True:
        for ev in pygame.event.get():
            if ev.type == MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                act = checkbox(mousepos, cheatbutton_coor)
                if (act > 0 and not(pau)) or act == 0 or act == 4:
                    screen.blit(s_1, (1000, 150+75*act))
            elif ev.type == MOUSEBUTTONUP:
                if act == 0:
                    pau = not(pau)
                    if pau:
                        drawbutton(screen, "Resume", 1000, 150)
                        screen.blit(font.render("Cheat is paused",
                                    False, white), (565, 580))
                    else:
                        drawbutton(screen, "Pause", 1000, 150)
                        screen.blit(font.render("Cheat is paused",
                                    False, black), (565, 580))
                elif act == 1:
                    showstat = not(showstat)
                    if showstat:
                        drawbutton(screen, "Statistic: On", 1000, 225)
                        screen.blit(font.render("Testcase No."+str(matrixidx), False, white), (30, 200))
                        screen.blit(font.render(algo+"Time:", False, white), (30, 250))
                        screen.blit(font.render(str(runtime)+"s", False, white), (30, 300))
                        screen.blit(font.render(algo+"Maximum memory used:", False, white), (30, 350))
                        screen.blit(font.render(str(memused)+"MiB", False, white), (30, 400))
                    else:
                        drawbutton(screen, "Statistic: Off", 1000, 225)
                        pygame.draw.rect(screen, black, (20, 190, 370, 450))
                elif act == 2:
                    return [choice, type, matrixidx]
                elif act == 3:
                    return [0, 0, -4]
                elif act == 4:
                    sys.exit()
        if not(pau) and wait:
            count += 1
            if count == 750:
                count = 0
                idx += 1
                if idx == matrixlen-1:
                    screen.blit(font.render(
                        "Cheat is finished! This is the result.", False, white), (475, 580))
                    wait = False
                if type == 5:
                    for i in range(0, 5):
                        for j in range(0, 5):
                            draw_hitori_element(
                                zone, matrixlist[idx][i][j], 5*i+j)
                else:
                    for i in range(0, 7):
                        for j in range(0, 7):
                            draw_hashi_element(
                                zone, matrixlist[idx][i][j], 7*i+j)
                screen.blit(zone, (400, 75))
        pygame.display.update()
        pygame.time.delay(1)
