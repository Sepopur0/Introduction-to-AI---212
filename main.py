from funcs import *
def main():
    screen=pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Search simulate")
    res=everything(screen)
    while True:
        if res[2]==-4:
            everything(screen)  
        elif res[2] in range(0,19):
            res=cheat_algori(screen,5-res[0],res[1],res[2])      

def everything(screen):
    screen.fill(black)
    step_1=menu(screen,["Hitori 5x5","Hashi 7x7","Quit"])
    zone= pygame.Surface((500,500))
    zone.fill(black)
    choice=create_gamescreen(zone,screen,step_1)
    act=-1
    s_1=pygame.Surface((150,50))
    pygame.draw.rect(s_1,yellow,pygame.Rect(0,0,button_width,button_height),0,40)
    pygame.Surface.set_alpha(s_1,100)
    pau=False
    cheatactiv=-1
    trupos=-1
    while True:
        for ev in pygame.event.get():
            if ev.type==MOUSEBUTTONDOWN:
                mousepos=pygame.mouse.get_pos()
                act=checkbox(mousepos,gamebutton_coor)               
                if (act>0 and not(pau)) or act==0 or act==5:
                    screen.blit(s_1,(1000,100+75*act))
                # elif not(pau):
                #     if act==-1:
                #         pos=checkpos(mousepos,modu)
                #         if (modu==7 or modu==10) and pos!=-1:
                #             if matrix[pos//modu][pos%modu]==0:
                #                 trupos=-1
                #             else:
                #                 trupos=pos
                #         else:
                #             trupos=pos
            elif ev.type==MOUSEBUTTONUP:
                # if act==-1 and not(pau) and trupos!=-1:
                #     if modu==5 or modu==8:
                #         draw_hitori_element(zone,-1,(modu//7),pos)
                #         matrix_solve[pos//modu][pos%modu]=-1
                #     elif modu==7 or modu==10:
                #         mousepos=pygame.mouse.get_pos()
                #         posend=checkpos(mousepos,modu)
                #         if matrix[posend//modu][posend%modu]!=0:
                #             if(trupos//modu==posend//modu):
                #                 while(trupos<posend):
                #                     trupos+=1
                #                     if not(matrix[posend//modu][trupos%modu] in range(1,9)):
                #                         matrix_solve[posend//modu][trupos%modu]=(matrix_solve[posend//modu][trupos%modu]+11)%33
                #                         draw_hashi_element(zone,matrix_solve[posend//modu][trupos%modu],modu//8,trupos,0)
                #                     else:
                #                         break
                #             elif(trupos%modu==posend%modu):
                #                 while(trupos<posend):
                #                     trupos+=modu
                #                     if not(matrix[trupos//modu][posend%modu] in range(1,9)):
                #                         matrix_solve[trupos//modu][posend%modu]=(matrix_solve[trupos//modu][posend%modu]+11)%33
                #                         draw_hashi_element(zone,matrix_solve[trupos//modu][posend%modu],modu//8,trupos,1)
                #                     else:
                #                         break  
                #     screen.blit(zone,(400,75))
                #     trupos=-1                                                 
                if act==0:
                    pau=not(pau)
                    if pau:
                        drawbutton(screen,"Resume",1000,100)
                        screen.blit(font.render("Game is paused",False,white),(575,580))
                    else:
                        drawbutton(screen,"Pause",1000,100)
                        screen.blit(font.render("Game is paused",False,black),(575,580))    
                elif act==1 and not(pau):
                    drawbutton(screen,"Refresh",1000,175)
                    zone.fill(black)
                    pygame.draw.rect(zone,white,(5,5,490,490),5)
                    if step_1==5:
                        choice=draw_hitori(zone)
                    else:
                        choice=draw_hashi(zone)
                    for i in range(0,5):
                        for ev in pygame.event.get():
                            if ev.type==pygame.QUIT:
                                sys.exit()
                        pygame.Surface.set_alpha(zone,80+i*35)
                        screen.blit(zone,(400,75))
                        pygame.display.update()
                        pygame.time.delay(200)
                    zone.set_alpha(255)
                    pygame.display.update()
                elif act==2 or act==3 and not(pau):
                    cheatactiv=act
                    break
                elif act==4:
                    return [0,0,-4]
                elif act==5:
                    sys.exit()
            elif ev.type==pygame.QUIT:
                sys.exit()
            pygame.display.update()
        if cheatactiv!=-1:
            break
    return cheat_algori(screen,act,step_1,choice)
main()
    

    
        
    