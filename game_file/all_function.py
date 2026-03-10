import pygame
import random
from time import sleep
pygame.init()
screen=pygame.display.set_mode((1400,700))


def button(t_size,text,t_color,x_pos,y_pos,rect_color,rect_width,rect_height):
    pygame.draw.rect(screen,rect_color,(x_pos,y_pos,rect_width,rect_height),0,int(rect_height/3))
    font=pygame.font.SysFont("arial",t_size,True,True)
    render=font.render(text,True,t_color)
    screen.blit(render,(x_pos,y_pos))
   
    # (x,y),(x1=x + rect_width,y),(x,y1=y+rect_height),(x1,y1)


def Light_color(*values):
    # ..0......1.....2.......3....4.......5..........6.........7....
    # t_size,text,t_color,x_pos,y_pos,rect_width,rect_height,light_color,
    x1 = values[3] + values[5]
    y1 = values[4] + values[6]
    curser=pygame.mouse.get_pos()
    if (values[3] < curser[0] < x1 and values[4] < curser[1] < y1):
        pygame.draw.rect(screen, values[7], (values[3], values[4], values[5], values[6]),0,int(values[6]/3))
        font = pygame.font.SysFont("arial", values[0], True, True)
        render = font.render(values[1], True, values[2])
        screen.blit(render, (values[3], values[4]))






def is_click(x,y,rect_width,rect_height):
    x1=x + rect_width
    y1=y+rect_height
    curser_pos=pygame.mouse.get_pos()
    click_val=pygame.mouse.get_pressed()
    # time.sleep(.2)
    click=False
    if (x<curser_pos[0]<x1 and y<curser_pos[1]<y1):
        if click_val[0]:
            pygame.mixer.Sound("game_sound/button_pressed.mp3").play()
            click=True
    
    return click



def massage(t_size,mass,t_color,x_pos,y_pos,t_bg=None):
    font= pygame.font.SysFont(None,t_size)
    render=font.render(mass,True,t_color,t_bg)
    screen.blit(render,(x_pos,y_pos))


def add_image(location,l_im,w_im,*pos):
    im=pygame.image.load(location)
    im=pygame.transform.scale(im,(l_im,w_im))
    screen.blit(im,pos)



    
