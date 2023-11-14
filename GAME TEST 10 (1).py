import pygame
import random
import os
#muuda
#ekraani seaded
WIDTH=600
HEIGHT=480
FPS=35
bg_image = pygame.image.load('taust3.PNG')
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
#värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0,155,155)
#failide asukohad
game_folder= os.path.dirname(__file__)  
img_folder=os.path.join(game_folder, "img")

#mängu init
pygame.init() 
pygame.mixer.init() #helide jaoks
screen=pygame.display.set_mode((WIDTH, HEIGHT))#ekraan
screen_rect=screen.get_rect() #ekraani rectangle
pygame.display.set_caption("KANAMÄNG")

#mängu defineerimine, mängu loop
def main():
    clock=pygame.time.Clock()
    #game loop
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        all_sprites.update()
        screen.fill(BLACK)
        hits=pygame.sprite.spritecollide(player,mobs,False) #kui saad pihta siis sured
        if hits:
            return
        game_display.blit(bg_image, (0, 0))
        all_sprites.draw(screen) #joonistame sprite
        pygame.display.flip() #flip
        pygame.display.update()


#player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self)
        self.directionality = "right"
        self.image=pygame.Surface((30,37))
        self.image.fill(YELLOW)
        self.image=pygame.image.load(os.path.join(img_folder,"alienYellow_walk1.png")).convert_alpha()
        self.image.set_colorkey(BLACK) #eemaldab foto tausta
        self.rect=self.image.get_rect()
        self.rect.centery=WIDTH #spawnimise asukoht
        self.rect.bottom=HEIGHT/2
        self.x_speed=3 #liigub ise sellel kiirusel 3
        self.y_speed=0
    
    def update(self):
        self.rect.y+=self.y_speed #uuendab sinu liigutud koordinaatidele ennast
        self.rect.x+=self.x_speed
        keystate=pygame.key.get_pressed() #liikumiseks kasutame neid nuppe
        if keystate[pygame.K_UP]:
            self.rect.y+=-4 #saad teda liigutada sel kiirusel
        if keystate[pygame.K_DOWN]:
            self.rect.y+=4
        if self.rect.right>WIDTH: #kui ületab laiuse siis quit
            pygame.quit() #kui eludega teha siis ilmselt siia midagi muud
        self.rect.clamp_ip(screen_rect) #hoiab ekraanil


            
            
#MOB objektid 
class Mob1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self) 
        self.image=pygame.Surface((30,40)) #suurus
        self.image.fill(RED)
        self.image=pygame.image.load(os.path.join(img_folder,"fishGreen_dead.png")).convert_alpha()
        self.image.set_colorkey(BLACK) #jälle tausta eemaldamine
        self.rect=self.image.get_rect()
        self.rect.x=120 #x koordinaat, pmts kus esimene maantee asub
        self.rect.y=random.randrange(1,480,300) #y spawn on random
        self.speedy=random.randrange(1,3) #kiiruse vahemik 1-3
        self.speedx=0
        
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>HEIGHT or self.rect.right>WIDTH:
            self.rect.x=120
            self.rect.y=random.randrange(1,480,300) #saab muuta 
            self.speedy=random.randrange(1,3) #saab muuta idk, kas vajalik

class Mob2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self) 
        self.image=pygame.Surface((30,40))
        self.image.fill(RED)
        self.image=pygame.image.load(os.path.join(img_folder,"fishPink.png")).convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=230
        self.rect.y=random.randrange(1,480,200)
        self.speedy=random.randrange(3,4)
        self.speedx=0
        
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>HEIGHT or self.rect.right>WIDTH:
            self.rect.x=230
            self.rect.y=random.randrange(1,480,200)
            self.speedy=random.randrange(3,4)

class Mob3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self) 
        self.image=pygame.Surface((30,40))
        self.image.fill(RED)
        self.image=pygame.image.load(os.path.join(img_folder,"piranha.png")).convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=400
        self.rect.y=random.randrange(1,480,200)
        self.speedy=random.randrange(-2,-1)
        self.speedx=0
        
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>HEIGHT or self.rect.right>WIDTH:
            self.rect.x=400
            self.rect.y=random.randrange(1,480,200)
            self.speedy=random.randrange(-2,-1)
            
class Mob4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self) 
        self.image=pygame.Surface((30,43))
        self.image.fill(RED)
        self.image=pygame.image.load(os.path.join(img_folder,"ghost_dead.png")).convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=490
        self.rect.y=random.randrange(1,480,200)
        self.speedy=random.randrange(-3,-1)
        self.speedx=0
        
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>HEIGHT or self.rect.right>WIDTH:
            self.rect.x=490
            self.rect.y=random.randrange(1,480,200) #????????
            self.speedy=random.randrange(-3,-1)


#sprite grupeerimine
all_sprites=pygame.sprite.Group()
player=Player()
mobs=pygame.sprite.Group()
all_sprites.add(player)

for i in range(6): #siin ta teeb 8 vaenlast iga MOB klassi kohta
    a=Mob1()
    b=Mob2()
    c=Mob3()
    d=Mob4()
    all_sprites.add(a,b,c,d)
    mobs.add(a,b,c,d)


if __name__ == '__main__':
    main()
    pygame.quit()    

