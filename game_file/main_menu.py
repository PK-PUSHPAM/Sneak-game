from game_file.all_function import *
from game_file.button import *
from game_file.masseage import *
from game_file.photo import *
import game_file.game_state as state 
from math import pow

def highscore_interface():
     while state.setting_run:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((200,200,200))
        back_button()
        name()

        massage(50,f"High Score:= {state.high_score}",(153, 166, 90),550,350)

        if(is_click(10,10,90,30)): #back button
            state.setting_run=False
            state.intro_run=True
            pygame.event.clear()
            sleep(0.1)
            return
        
        pygame.display.update() 




def level_interface():
    while state.level_run:
        screen.fill((200,200,200))
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if state.lev<5:
                    if event.key== pygame.K_UP:
                        pygame.mixer.Sound("game_sound/speed.mp3").play()
                        state.lev+=1
                if state.lev>1:
                    if event.key== pygame.K_DOWN:
                        pygame.mixer.Sound("game_sound/speed.mp3").play()
                        state.lev-=1 
                

        back_button()
        massage(50,"pushpam\'s game",(153, 166, 90),550,10)

        if(is_click(10,10,90,30)): #back button
            state.level_run=False
            state.intro_run=True
            pygame.event.clear()
            sleep(0.1)
            return
        
        pygame.draw.rect(screen,(250,150,150),(675,100,50,500),0,15)
        pygame.draw.rect(screen,(250,100,100),(675,100,50,500),3,15)
        pygame.draw.rect(screen,(255,0,0),(675,600-(state.lev)*100,50,(state.lev)*100),0,15)
        state.speed=1/pow(10,state.lev)
    
        pygame.display.update() 

def intro():
    global direction
    while state.intro_run:
        main_menu_bg()
        game_logo()
        massage(50,"pushpam\'s game",(153, 0,0),550,10)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()

        if is_click(400,470,150,40): #new game button
            state.intro_run = False
            state.isgame_loop_run=True
            state.x_pos_snake_head=40
            state.y_pos_snake_head=640
            state.direction="RIGHT"
            state.score=0
            state.isOut=False
            state.snake_body=[(40,660)]
            pygame.event.clear()
            sleep(0.1)

        if is_click(900,470,100,40): #level button
            state.intro_run=False
            state.level_run=True
            pygame.event.clear()
            sleep(0.1)

        if is_click(750,470,110,40): # continue button
            if  state.isOut==False:
                state.intro_run=False
                state.isgame_loop_run=True
                pygame.event.clear()
                sleep(0.1)
            elif state.isOut:
                state.intro_run = False
                state.isgame_loop_run=True
                state.isOut=False
                state.direction="RIGHT"
                state.score=0
                state.snake_body=[(40,640)]
                pygame.event.clear()
                sleep(0.1)

        if is_click(600,470,100,40): #High score button
            state.intro_run=False
            state.setting_run=True
            pygame.event.clear()
            sleep(0.1)




        start_button()
        highscore_button()
        continue_bt()
        level()
        pygame.display.update()
