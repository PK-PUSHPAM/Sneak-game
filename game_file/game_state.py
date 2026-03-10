from random import randrange
intro_run = True

isgame_loop_run = False
level_run=False
setting_run=False
lev=1
speed=.1
x_pos_snake_head=40
y_pos_snake_head=640
score=0
isOut=False
x_pos_food = randrange(20, 1340, 20)
y_pos_food = randrange(60, 640, 20)
direction = "RIGHT"
snake_body=[(x_pos_snake_head,y_pos_snake_head)]
f=open("game_file/highest_score.txt","r")
high_score=int(f.read())
f.close()
