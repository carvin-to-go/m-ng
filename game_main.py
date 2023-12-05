import pygame
import random
import os
import math 

#ekraani seaded
clock = pygame.time.Clock() 
WIDTH=590
HEIGHT=480
FPS=35
bg_image = pygame.image.load('ookean.jpg')
bg_x = 0
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
scroll = 0
tiles = math.ceil(WIDTH / bg_image.get_width()) + 1

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
#pygame.mixer.init() #helide jaoks
screen=pygame.display.set_mode((WIDTH, HEIGHT))#ekraan
screen_rect=screen.get_rect() #ekraani rectangle
pygame.display.set_caption("KALAMÄNG")

score = 0
successful_passes = 0


#mängu defineerimine, mängu loop
def main():
    
    global successful_passes
    global score
    clock=pygame.time.Clock()
    
    #game loop
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        global bg_x
        bg_x -= 3
        
        if bg_x <= -bg_image.get_width():
            bg_x = 0
            
        all_sprites.update()
        screen.fill(BLACK)
        for i in range(tiles):
            game_display.blit(bg_image, (bg_x + i * bg_image.get_width(), 0))


        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            running=False
            
        if not hits:  
            successful_passes += 1
            if successful_passes % 15 == 0: #loeb punkte
                score += 1
        
        #kuvab punktid 
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(score), True, WHITE)
        text_rect = text.get_rect()
        text_rect.topleft = (10, 10)
        screen.blit(text, text_rect)      
        all_sprites.draw(screen)
        pygame.display.flip()
        pygame.display.update()


         
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
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            # ring peale
            self.rect.left = 0 
            self.rect.centery = HEIGHT // 2           

class Mob1(pygame.sprite.Sprite):
    def __init__(self, mobs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))# suurus 
        self.image = pygame.image.load(os.path.join(img_folder, "fishGreen_dead.png")).convert_alpha() 
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        random1=random.sample(range(0, 480, 45), 4)
        taken1=[]
        for value in random1:
            current_value1=value
        if current_value1 not in taken1:
            self.rect.y = current_value1
            taken1.append(current_value1)
        
        self.rect.x = 120
        self.speedy = 2 #kiirus
        self.speedx = 0 #x teljel ei liigu
 
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom > HEIGHT+40:
            self.rect.y=0


class Mob2(pygame.sprite.Sprite):
    def __init__(self, mobs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))# suurus 
        self.image = pygame.image.load(os.path.join(img_folder, "fishPink.png")).convert_alpha() # mis visuaal on 
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        random2=random.sample(range(0, 480, 45), 4)
        taken2=[]
        for value in random2:
            current_value2=value
        if current_value2 not in taken2:
            self.rect.y = current_value2
            taken2.append(current_value2)
        self.rect.x = 240
        self.speedy = 3
        self.speedx = 0 
 
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom > HEIGHT+40:
            self.rect.y=0

class Mob3(pygame.sprite.Sprite):
    def __init__(self, mobs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))# suurus 
        self.image = pygame.image.load(os.path.join(img_folder, "piranha.png")).convert_alpha()  
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        random3=random.sample(range(0, 480, 45), 4)
        taken3=[]
        for value in random3:
            current_value3=value
        if current_value3 not in taken3:
            self.rect.y = current_value3
            taken3.append(current_value3)
        self.rect.x = 350
        self.speedy = -2
        self.speedx = 0 # x teljel ei liigu
 
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom<0:
            self.rect.y=480

 
        
class Mob4(pygame.sprite.Sprite):
    def __init__(self, mobs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image = pygame.image.load(os.path.join(img_folder, "ghost_dead.png")).convert_alpha() 
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        random4=random.sample(range(0, 480, 50), 4)
        taken4=[]
        for value in random4:
            current_value4=value
        if current_value4 not in taken4:
            self.rect.y = current_value4
            taken4.append(current_value4)
        self.rect.x = 490
        self.speedy = -3 
        self.speedx = 0 
 
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  
        if self.rect.bottom<0:
            self.rect.y=480



#sprite grupeerimine
all_sprites=pygame.sprite.Group()
player=Player()
mobs=pygame.sprite.Group()
all_sprites.add(player)

#võib siia ka random vahemikus Mobe teha
for i in range(4): 
    a=Mob1(mobs)
    b=Mob2(mobs)
    c=Mob3(mobs)
    d=Mob4(mobs)
    all_sprites.add(a,b,c,d)
    mobs.add(a,b,c,d)


if __name__ == '__main__':
    main()
    pygame.quit()    


