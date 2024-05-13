import pygame 
import random 
pygame.font.init()
win_windth=1200 
win_height=700 
 
FPS=pygame.time.Clock() 
window=pygame.display.set_mode((win_windth,win_height)) 
pygame.display.set_caption("Лабіринт") 
game=True 
finish=False 
 
class Settings: 
    def __init__(self,image,x,y,w,h): 
        self.image=pygame.transform.scale(pygame.image.load(image),(w,h)) 
        self.rect=self.image.get_rect() 
        self.rect.x=x 
        self.rect.y=y 
         
 
    def draw(self): 
        window.blit(self.image,(self.rect.x,self.rect.y)) 
class Player(Settings): 
    def __init__(self, image, x, y, w, h,s): 
        super().__init__(image, x, y, w, h) 
        self.speed=s 
        self.direction=True 
        self.image_right=self.image 
        self.image_left=pygame.transform.flip(self.image,True,False) 
 
 
    def move(self): 
        keys=pygame.key.get_pressed() 
        if keys[pygame.K_UP] and self.rect.y>0: 
            self.rect.y-=self.speed 
        if keys[pygame.K_DOWN] and self.rect.y< win_height-self.rect.height: 
            self.rect.y+=self.speed 
        if keys[pygame.K_LEFT] and self.rect.x>0: 
            self.rect.x-=self.speed 
            self.direction=False 
        if keys[pygame.K_RIGHT] and self.rect.x<win_windth-self.rect.height: 
            self.rect.x+=self.speed 
            self.direction=True 
        if self.direction: 
            self.image=self.image_right 
        else: 
            self.image=self.image_left 
 
class Enemy(Player): 
    def __init__(self, image, x, y, w, h, s): 
        super().__init__(image, x, y, w, h, s) 
 
    def move(self,x1,x2): 
        if self.rect.x>x2: 
            self.direction=False 
 
        if self.rect.x<x1: 
            self.direction=True 
 
        if self.direction==True: 
            self.image=self.image_left 
            self.rect.x+=self.speed 
         
        if self.direction==False: 
            self.rect.x-=self.speed 
            self.image=self.image_right
 
class Wall: 
    def __init__(self,x,y,w,h,color): 
        self.rect=pygame.Rect(x,y,w,h) 
        self.color=color 
    def draw(self): 
        pygame.draw.rect(window,self.color,self.rect) 
class Text: 
    def __init__(self,x,y,text,size,color): 
        self.x=x 
        self.y=y 
        self.text=text 
        self.color=color 
        self.size=size 
    def set_text(self): 
        self.txt=pygame.font.SysFont("verdana",self.size).render(self.text,True,self.color) 
    def draw(self): 
        self.set_text() 
        window.blit(self.txt,(self.x,self.y)) 
class Button: 
    def __init__(self,x,y,w,h,t_color,color): 
        self.rect=pygame.Rect(x,y,w,h) 
        self.t_color=t_color 
        self.color=color 
    def set_text(self,size,text): 
        self.txt=pygame.font.SysFont("verdana",size).render(text,True,self.t_color) 
    def draw(self,_x,_y): 
        pygame.draw.rect(window,self.color,self.rect) 
        pygame.draw.rect(window,(0,0,0),self.rect,width=4) 
        window.blit(self.txt,(self.rect.x+_x,self.rect.y+_y)) 
 
 
reset=Button(win_windth//2.5,win_height-200,250,150,(0,0,0),"grey") 
zoloto=Settings("gold.png",win_windth-150,win_height-200,100,100) 
enemy=Enemy("enemy.png",600,win_height//2,100,100,7) 
player=Player("player.png",0,10,100,100,10) 
fon=Settings("background.jpg",0,0,win_windth,win_height) 
pygame.font.init() 
win=Text(win_windth//7,win_height//3,"You win!",150,"blue") 
lose=Text(win_windth//7,win_height//3,"Game over!",150,"green") 
pygame.mixer.init() 
pygame.mixer.music.load("Jungle_sfx.mp3") 
pygame.mixer.music.play() 
pygame.mixer.music.set_volume(0.8) 
 
 
 
walls=[ 
    Wall(150,0,10,600,(random.randint(0,255),random.randint(0,255),random.randint(0,255))), 
    Wall(150,0,1500,10,(random.randint(0,255),random.randint(0,255),random.randint(0,255))), 
    Wall(150,590,300,10,(random.randint(0,255),random.randint(0,255),random.randint(0,255))),
    Wall(600,150,10,600,(random.randint(0,255),random.randint(0,255),random.randint(0,255))),
    Wall(300,450,300,10,(random.randint(0,255),random.randint(0,255),random.randint(0,255))),
    Wall(300,150,750,10,(random.randint(0,255),random.randint(0,255),random.randint(0,255))),
    Wall(150,300,300,10,(random.randint(0,255),random.randint(0,255),random.randint(0,255))),
    Wall(1000,300,200,10,(random.randint(0,255),random.randint(0,255),random.randint(0,255))),
    Wall(600,300,250,10,(random.randint(0,255),random.randint(0,255),random.randint(0,255))),
    Wall(1000,500,200,10,(random.randint(0,255),random.randint(0,255),random.randint(0,255))),
    Wall(600,500,250,10,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
] 

while game:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            game = False 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos 
            if reset.rect.collidepoint(x, y):
                player.rect.y = 10 
                player.rect.x = 0
                finish = True  
    if not finish: 
        window.blit(fon.image, (0, 0)) 
        for w in walls: 
            if player.rect.colliderect(w.rect): 
                player.rect.x = 0 
                player.rect.y = 10 
            w.draw() 
        window.blit(player.image, (player.rect.x, player.rect.y)) 
        player.move() 
        window.blit(enemy.image, (enemy.rect.x, enemy.rect.y)) 
        enemy.move(600, win_windth-enemy.rect.width) 
        zoloto.draw() 
    if player.rect.colliderect(enemy.rect): 
        fon.draw() 
        lose.draw() 
        finish=True 
    if player.rect.colliderect(zoloto.rect): 
        fon.draw() 
        win.draw() 
        finish=True 
    pygame.display.flip() 
    FPS.tick(60)

