import pygame
from time import sleep
from game_file.all_function import *
from game_file.masseage import *
from game_file.button import *
import game_file.game_state as state

def game_loop():
    
    block_size = 20
    x_change = block_size
    y_change = 0
    while state.isgame_loop_run:
        add_image("game_image/bg_main.png",2000,1000,-200,-200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                pygame.mixer.Sound("game_sound/key_press.mp3").play(0,0,-30)
                if event.key == pygame.K_RIGHT and state.direction != "LEFT":
                    state.direction = "RIGHT"
                    
                elif event.key == pygame.K_LEFT and state.direction != "RIGHT":
                    state.direction = "LEFT"
                
                elif event.key == pygame.K_UP and state.direction != "DOWN":
                    state.direction = "UP"
    
                elif event.key == pygame.K_DOWN and state.direction != "UP":
                    state.direction = "DOWN"

        # After event handling, before moving the snake:
        if state.direction == "RIGHT":
            x_change = block_size
            y_change = 0
        elif state.direction == "LEFT":
            x_change = -block_size
            y_change = 0
        elif state.direction == "UP":
            x_change = 0
            y_change = -block_size
        elif state.direction == "DOWN":
            x_change = 0
            y_change = block_size

        new_head = (state.snake_body[0][0] + x_change, state.snake_body[0][1] + y_change)
        state.snake_body.insert(0, new_head)


        ate_food = (new_head[0] == state.x_pos_food and new_head[1] == state.y_pos_food)
        if ate_food:
            pygame.mixer.Sound("game_sound/eat.mp3").play()
            sleep(.1)
            state.score+=1
            state.x_pos_food = random.randrange(20, 1340, block_size)
            state.y_pos_food = random.randrange(60, 640, block_size)
        else:
            state.snake_body.pop()  

    
        pygame.draw.rect(screen,(0,0,0), (state.x_pos_food,state.y_pos_food, block_size, block_size),0,10)




        if (new_head[0] < 20 or new_head[0] > 1360 or new_head[1] < 60 or new_head[1] > 660):
            pygame.mixer.Sound("game_sound/losing_sound.wav").play()
            sleep(1)
            screen.fill((30,30,30))
            massage(80, "Game Over", (200,200,200), 550, 10)
            state.isOut=True
            state.isgame_loop_run = False
            state.intro_run = True
            if state.high_score<state.score:
                    with open("game_file/highest_score.txt","w") as f:
                        f.write(f"{state.score}")
                    state.high_score=state.score
            
            massage(40,f"High Score: {state.high_score}",(200,200,200),550,300)
            massage(40,f"New Score: {state.score}",(200,200,200),550,400)
            pygame.display.update()
            pygame.event.clear()
            sleep(2)
            return
        
        
        for block in state.snake_body:
            pygame.draw.rect(screen, (0,255,0), (block[0], block[1], block_size, block_size),0,5)

        # pygame.draw.rect(screen,(255,0,0),(0,0,20,700))
        for block in state.snake_body[1:]:
            if block[0]==new_head[0] and block[1]==new_head[1]:
                pygame.mixer.Sound("game_sound/losing_sound.wav").play()
                sleep(1)
                screen.fill((30,30,30))
                massage(80, "Game Over", (200,200,200), 550, 10)
                massage(40,f"High Score: {state.high_score}",(200,200,200),550,300)
                massage(40,f"New Score: {state.score}",(200,200,200),550,400)
                state.isOut=True
                pygame.display.update()
                state.isgame_loop_run = False
                state.intro_run = True
                pygame.event.clear()
                
                if state.high_score<state.score:
                    with open("game_file/highest_score.txt","w") as f:
                        f.write(f"{state.score}")
                    state.high_score=state.score
                sleep(2)
                return


        add_image("game_image/Top_boundary.png",1400,181,0,602)
        add_image("game_image/Top_boundary.png",1400,497,0,-220)

        im=pygame.image.load("game_image/Top_boundary.png")
        im=pygame.transform.rotate(im,90)
        im=pygame.transform.scale(im,(150,700))
        screen.blit(im,(-66,0))
        screen.blit(im,(1315,0))

        massage(50,"pushpam\'s game",(153, 0,0),550,10)

        back_button()
        if is_click(10,10,90,30): #for back
            state.isgame_loop_run = False
            state.intro_run = True
            pygame.event.clear()
            sleep(0.1)
            return
    
        massage(50,f"Score: {state.score}",(254, 153, 0),200,10,(53, 194, 28))
        pygame.display.update()
        sleep(state.speed)
        # pygame.time.Clock().tick(50)