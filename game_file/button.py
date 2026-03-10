from game_file.all_function import button,Light_color,is_click
# button(......t_size,.......text,.....t_color,......x_pos,.....y_pos,......rect_color,.....rect_width,....rect_height)
# light_color(...t_size......,text......,t_color.......,x_pos.....,y_pos......,rect_width......,rect_height.......,light_color)

def start_button():
    button(30,"New Game",(239, 235, 19),400,470,(255,0,0),150,40)
    Light_color(31,"New Game",(239, 235, 19),400,470,150,40,(155,0,0))

def highscore_button():
    button(30,"High Score",(239, 235, 19),570,470,(255,0,0),150,40)
    Light_color(31,"High Score",(239, 235, 19),570,470,150,40,(155,0,0))


def continue_bt():
    button(30,"continue",(239, 235, 19),750,470,(255,0,0),110,40)
    Light_color(31,"continue",(239, 235, 19),750,470,110,40,(155,0,0))

def level():
    button(30,"level",(239, 235, 19),900,470,(255,0,0),100,40)
    Light_color(31,"level",(239, 235, 19),900,470,100,40,(155,0,0))

def back_button():
    button(25,"<-back",(0,0,0),10,10,(250,250,250),90,30)
    Light_color(25,"<-back",(0,0,0),10,10,90,30,(200,200,200))

def easy():
    button(25,"easy",(0,0,0),550,350,(250,250,250),90,30)
    Light_color(25,"easy",(0,0,0),550,350,90,30,(200,200,200))
    