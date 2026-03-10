# bg_img=pygame.image.load("game_image/main_menu.png")
#     bg_img=pygame.transform.scale(bg_img,(1400,700))
from game_file.all_function import add_image
def main_menu_bg():
    add_image("game_image/main_menu.png",1700,700,0,0)


def game_logo():
    add_image("game_image/logo.png",700,400,380,60)

