import pygame
import random #used for randomness of food to be generated on scrren 
pygame.init()
#setting up game window 
window_width=800
window_height=600
window=pygame.display.set_mode((window_width,window_height))         #display module helps us to create a window
pygame.display.set_caption("snake game") 
white=(255,255,255)       #rgb value of white to be passed below 
black=(0,0,0)
red=(255,0,0)  #255 for red 0 for green 0 for blue
game_over=False
score=0
x1=window_width/2
y1=window_height/2
x1_change=0
y1_change=0
snake_body=[]   # used when snake has eaten the food and so as to increment the snake's body
length_of_snake=1

foodx=round(random.randrange(0,window_width-10)/10)*10.0
foody=round(random.randrange(0,window_height-10)/10)*10.0

clock=pygame.time.Clock()    #for frame rate

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        #check for arrow key is pressed 
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x1_change=-10    # since we are going to left there we have set the x coordinate to -10 
                y1_change=0
            elif event.key==pygame.K_RIGHT:
                x1_change=10
                y1_change=0
            elif event.key==pygame.K_UP:
                x1_change=0
                y1_change=-10
            elif event.key==pygame.K_DOWN:
                x1_change=0
                y1_change=10          
    x1=x1+x1_change
    y1=y1+y1_change 

    if x1>=window_width or x1<0 or y1>=window_height or y1<0:  # conditoin if snake hits the width and height of the frame game should end     x1<0 is for the condition in left because left goes to negative direction
        game_over=True
    
    window.fill(black) # this is used because we dont want a series of white line when snake is moving so it fills the colour black as soon as the snake position is changed
    snake_head=[]
    snake_head.append(x1)
    snake_head.append(y1)
    snake_body.append(snake_head)

    if len(snake_body)>length_of_snake:
        del snake_body[0]

    for segemnt in snake_body[:-1]:
        if segment==snake_head:
            game_over=True

    font_style=pygame.font.SysFont(None,50)
    score_text=font_style.render("score:"+str(score),True,white)
    window.blit(score_text,(10,10)) # blit adds score_text to window at the coordinates mentioned

    if x1==foodx and y1==foody:
        foodx=round(random.randrange(0,window_width-10)/10)*10.0
        foody=round(random.randrange(0,window_height-10)/10)*10.0  
        length_of_snake+=1
        score+=1


    pygame.draw.rect(window,red,(foodx,foody,10,10))   #this is for the food             

   #pygame.draw.rect(window,white,[x1,y1,10,10])  # 400 is the x pos and 300 is the y position
    for segment in snake_body:
        pygame.draw.rect(window,white,[segment[0],segment[1],10,10])
    pygame.display.update()
    clock.tick(20) # speed of the game or frame rate so as to move our snake slow 