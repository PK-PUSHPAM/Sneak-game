
from game_file.main_menu import *
from game_file.game_interface import*
import game_file.game_state as state
def game_start():
    while(True):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        if state.intro_run:
            pygame.mixer.music.load("game_sound/game_main_bg_music.wav")
            pygame.mixer_music.play(-1,0.0)
            pygame.mixer.music.set_volume(.4)          
            intro()

        if state.level_run:
            level_interface()

        if state.isgame_loop_run:
            pygame.mixer_music.load("game_sound/interface.mp3")
            pygame.mixer_music.play(-1,0)
            game_loop()
            pygame.mixer_music.stop()

        if state.setting_run:
            highscore_interface()
    
        
        pygame.display.update()


game_start()

pygame.quit()
quit()

