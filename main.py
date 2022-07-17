
import pygame
from pygame import mixer
from sklearn import mixture
#inicilaizamos pygame
pygame.init()
#tamaños de pantalla 
width=1400
height=800

#definimos los colores 
black=(0,0,0)
white=(255,255,255)
gray=(128,128,128)
dark_gray=(50,50,50)
green=(0,255,0)
gold=(212,175,55)
blue=(0,255,255)
#creamos la pantalla 

screen=pygame.display.set_mode([width, height])
#colocamos un titulo
pygame.display.set_caption('dj zerocool')
#establecesmos la fuente 
label_font=pygame.font.Font('freesansbold.ttf', 32)
medium_font=pygame.font.Font('freesansbold.ttf', 24)
#velocidad del fotograma 
fps=60
timer=pygame.time.Clock()
beats=8
instruments=6
boxes=[]
clicked=[[-1 for _ in range(beats)]for _ in range(instruments)]
active_list=[1 for _ in range(instruments)]
bpm=  240
playing=True
active_lenght=0
active_beat=1
beat_charged=True

#load in sounds
hi_hat=mixer.Sound('hi hat.WAV')
snare=mixer.Sound('snare.WAV')
kick=mixer.Sound('kick.WAV')
crash=mixer.Sound('crash.WAV')
clap=mixer.Sound('clap.WAV')     
tom=mixer.Sound('tom.WAV')     
pygame.mixer.set_num_channels(instruments*3)

def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat]==1 and active_list[i]==1:
            if i ==0:
                hi_hat.play()
            if i ==1:
                snare.play()
            if i ==2:
                kick.play()
            if i ==3:
                crash.play()
            if i ==4:
                clap.play()
            if i ==5:
                tom.play()


#esta funcion diseña la pantalla
def draw_grid(clicks,beat, actives):
  left_box=pygame.draw.rect(screen,gray, [0,0,200, height-200],5)
  botton_box=pygame.draw.rect(screen, gray,[0,height-200,width,200 ],5)
  boxes=[]
  colors=[gray, white, gray ]    
  hi_hat_text=label_font.render('hi hat', True, colors[actives[0]] )
  screen.blit(hi_hat_text, (30,30))
  snare_text=label_font.render('snare', True,colors[actives[1]] )
  screen.blit(snare_text, (30,130))
  kick_text=label_font.render('Bass Drum', True,colors[actives[2]] )
  screen.blit(kick_text, (30,230))
  crash_text=label_font.render('Crash', True,colors[actives[3]] )
  screen.blit(crash_text, (30,330))
  kick_text=label_font.render('Clap', True,colors[actives[4]] )
  screen.blit(kick_text, (30,430))
  crash_text=label_font.render('Floor Tom', True,colors[actives[5]] )
  screen.blit(crash_text, (30,530))
  for i in range(instruments):
      pygame.draw.line(screen, gray, (0,(i*100)+100),(200,(i*100)+100),3)
  
  for i in range(beats):
      for j in range(instruments):
          if clicks[j][i]== -1:
              color=gray
          else:
              if actives[j]==1:
                color=green
              else:
                  color=dark_gray
              
          rect=pygame.draw.rect(screen, color,
                                [i*((width-200)//beats)+205,(j*100)+5,
                                              ((width-200)//beats)-10, ((height-200)//instruments)-10],0,3)
          pygame.draw.rect(screen, gold,
                           [i*((width-200)//beats)+200,(j*100),
                                              ((width-200)//beats), ((height-200)//instruments)],5,5)
          
          
          pygame.draw.rect(screen, black,
                           [i*((width-200)//beats)+200,(j*100),
                                              ((width-200)//beats), ((height-200)//instruments)],2,5)
          
          boxes.append((rect, (i,j)))
          
          
          
  active=pygame.draw.rect(screen, blue,[beat*((width-200)//beats)+200,0,((width-200)//beats),instruments*100],5,3)
  return boxes

def draw_save_menu():
    pygame.draw.rect(screen,black,[0,0,width, height])
    exit_btn=pygame.draw.rect(screen, gray,[height-200, height-100,100,90],0,5)
    exit_text=label_font.render('Close', True,white)
    screen.blit(exit_text,(height-160, height-70))
    return exit_btn
def draw_load_menu():
    pygame.draw.rect(screen,black,[0,0,width, height])
    exit_btn=pygame.draw.rect(screen, gray,[height-200, height-100,100,90],0,5)
    exit_text=label_font.render('Close', True,white)
    screen.blit(exit_text,(height-160, height-70))
    return exit_btn


  
   
run =True 
while run:
    timer.tick(fps)
    screen.fill(black)    
    boxes=draw_grid(clicked, active_beat, active_list)
    #lower menu bottons
    play_pause=pygame.draw.rect(screen, gray,[50, height-150,200,100],0,5)
    play_text=label_font.render('Play/Pause', True, white)
    screen.blit(play_text,(70, height-130))
    if playing:
        play_text2=medium_font.render('Playing', True,dark_gray)
    else:
        play_text2=medium_font.render('Pause', True,dark_gray)
    screen.blit(play_text2,(70, height-100))
    #bpm stuff
    bpm_rect=pygame.draw.rect(screen, gray,[300,height-150,200,100],5,5)
    bpm_text=medium_font.render('beats per minutes', True, white)
    screen.blit(bpm_text,(308,height-130))
    bpm_text2=label_font.render(f'{bpm}', True,white)
    screen.blit(bpm_text2, (370,height-100))
    bpm_add_rect=pygame.draw.rect(screen, gray, [510,height-150,48,48],0,5)
    bpm_sub_rect=pygame.draw.rect(screen, gray, [510,height-100,48,48],0,5)
    add_text=medium_font.render('+5', True, white)
    sub_text=medium_font.render('-5', True, white)
    screen.blit(add_text,(520,height-140))
    screen.blit(sub_text,(520,height-90))
    #beats stuff
    beats_rect=pygame.draw.rect(screen, gray,[600,height-150,200,100],5,5)
    beats_text=medium_font.render('beats in loop', True, white)
    screen.blit(beats_text,(618,height-130))
    beats_text2=label_font.render(f'{beats}', True,white)
    screen.blit(beats_text2, (680,height-100))
    beats_add_rect=pygame.draw.rect(screen, gray, [810,height-150,48,48],0,5)
    beats_sub_rect=pygame.draw.rect(screen, gray, [810,height-100,48,48],0,5)
    add_text=medium_font.render('+1', True, white)
    sub_text=medium_font.render('-1', True, white)
    screen.blit(add_text,(820,height-140))
    screen.blit(sub_text,(820,height-90))
    #instrument  rects
    
    instruments_rects=[]
    for i in range(instruments):
        rect=pygame.rect.Rect((0,i*100),(200,100))
        instruments_rects.append(rect)
        
    save_button=pygame.draw.rect(screen, gray,[900,height-150,200,48],0,5)
    save_text=label_font.render('Save Beat', True, white)
    screen.blit(save_text,(920, height-140))
    
    load_button=pygame.draw.rect(screen, gray,[900,height-150,200,48],0,5)
    load_text=label_font.render('Load Beat', True, white)
    screen.blit(load_text,(920, height-90))
    
    clear_botton=pygame.draw.rect(screen, gray,[1150, height-150,200,100],0,5)
    clear_text=label_font.render('Clear Beat', True,white)
    screen.blit(clear_text,(1160,height-130))
    
    
    if beat_charged:
        play_notes()
        beat_charged=False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False
        if event.type== pygame.MOUSEBUTTONDOWN :
            for i in range(len(boxes)):
                
                if boxes[i][0].collidepoint(event.pos):
                    coords= boxes[i][1]
                    clicked[coords[1]][coords[0]]*= -1
        if event.type==pygame.MOUSEBUTTONUP :
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing=False
                elif not playing:
                    playing=True
            elif bpm_add_rect.collidepoint(event.pos):
                bpm +=5
            elif bpm_sub_rect.collidepoint(event.pos):
                bpm-=5
            elif beats_add_rect.collidepoint(event.pos):
                beats +=1
                for i in range(len(clicked)):
                   clicked[i].append(-1) 
            elif beats_sub_rect.collidepoint(event.pos):
                beats-=1
                for i in range(len(clicked)):
                    clicked[i].pop(-1)
            elif clear_botton.collidepoint(event.pos):
                clicked=[[-1 for _ in range(beats)]for _ in range(instruments)]
            for i in range(len(instruments_rects)):
                if instruments_rects[i].collidepoint(event.pos):
                    active_list[i]*=-1
       
            
            
                
    beat_lenght=3600//bpm 
    
    if playing:
        if active_lenght < beat_lenght:    
           active_lenght +=1 
        else:
            active_lenght=0
            if active_beat <beats -1:
                active_beat +=1
                beat_charged =True
            else:
                active_beat =0
                beat_charged=True   
                
                
    pygame.display.flip()
pygame.quit()
        