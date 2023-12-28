import sys
import pygame
import random
from .GameModule import objectModule

class gManager:
    #define size variable
    WEIGHT = 1200
    HEIGHT = 600
    screen = pygame.Surface
    bg = pygame.Surface
    
    #define clock variable
    clock = pygame.time.Clock
    #define event variable
    EventFreqence = 3000
    MY_EVENT1 = 0
    MY_EVENT2 = 0
    #define object variable
    allsprite = pygame.sprite.Group
    player = objectModule.PlayerModule
    key = objectModule.KeyModule
    bullet_list = []
    lazer_list = []
    
    #player info
    Score = 0
    Name = "Unkown"
    
    def __init__(self, name):
        self.Name = name
        
        pygame.init()

        #define my event
        self.MY_EVENT1 = pygame.USEREVENT + 1
        self.MY_EVENT2 = pygame.USEREVENT + 2
        self.MY_EVENT3 = pygame.USEREVENT + 3
        pygame.time.set_timer(self.MY_EVENT1, self.EventFreqence)       #set timer for events
        pygame.time.set_timer(self.MY_EVENT2, self.EventFreqence*2)     #
        pygame.time.set_timer(self.MY_EVENT3, self.EventFreqence*3)     #
        
        self.clock = pygame.time.Clock()
        self.allsprite = pygame.sprite.Group()
        
        #modify screen size
        self.screen = pygame.display.set_mode((self.WEIGHT, self.HEIGHT))

        #making back ground
        self.bg = pygame.Surface(self.screen.get_size())                    #create a surface 
        self.bg = self.bg.convert()
        self.bg.fill((0,0,0))                                               #fill the surface with black
        white_bg = pygame.Surface((self.WEIGHT - 100, self.HEIGHT - 100))   #create a sub_surface
        white_bg.fill((150,150,150))                                        #fill the sub_surface with white
        self.bg.blit(white_bg, (50, 50))                                    #merge the sub_surface on the surface
        self.screen.blit(self.bg, (10,10))                                  #merge the surface on the screen

        #object setting's
        self.player = objectModule.PlayerModule(200, 200, 5)
        self.key = objectModule.KeyModule(self.random_pos()[0], self.random_pos()[1])
        self.allsprite.add(self.player)
        self.allsprite.add(self.key)

    #random position for key
    def random_pos(self):
        key_x = random.randint(50, self.WEIGHT-50)
        key_y = random.randint(50, self.HEIGHT-50)
        return key_x, key_y

    #create random bullet
    def create_bullet(self, speed, color):      #create bullets
        for i in range(0,5):
            x_pos = 0 if(random.randint(0,1) == 0) else self.WEIGHT
            y_pos = random.randint(50, self.HEIGHT-50)
            direction = 0 if(x_pos == 0) else 1
            bullet = objectModule.BulletModule(x_pos, y_pos, speed, direction, color)
            self.bullet_list.append(bullet)
            self.allsprite.add(bullet)
            
        for i in range(0,5):
            x_pos = random.randint(50, self.WEIGHT-50)
            y_pos = 0 if(random.randint(0,1) == 0) else self.HEIGHT
            direction = 2 if(y_pos == 0) else 3
            bullet = objectModule.BulletModule(x_pos, y_pos, speed, direction, color)
            self.bullet_list.append(bullet)
            self.allsprite.add(bullet)
    
    def create_bigbullet(self, speed, color):   #create larger bullets
        for i in range(0,5):
            x_pos = 0 if(random.randint(0,1) == 0) else self.WEIGHT
            y_pos = random.randint(50, self.HEIGHT-50)
            direction = 0 if(x_pos == 0) else 1
            bullet = objectModule.BigBulletModule(x_pos, y_pos, speed, direction, color)
            self.bullet_list.append(bullet)
            self.allsprite.add(bullet)
            
        
            
    def play(self):
        #main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == self.MY_EVENT1:
                    self.create_bullet(2, (0, 0, 255))
                elif event.type == self.MY_EVENT2:
                    self.create_bullet(5, (0, 255, 255))
                elif event.type == self.MY_EVENT3:
                    self.create_bigbullet(5, (255, 0, 0))

            #press W A S D to move, this allow player to move diagonally
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and keys[pygame.K_a]:
                self.player.move(-1, -1)
            elif keys[pygame.K_w] and keys[pygame.K_d]:
                self.player.move(1, -1)
            elif keys[pygame.K_s] and keys[pygame.K_a]:
                self.player.move(-1, 1)
            elif keys[pygame.K_s] and keys[pygame.K_d]:
                self.player.move(1, 1)
            elif keys[pygame.K_w]:
                self.player.move(0, -1)
            elif keys[pygame.K_s]:
                self.player.move(0, 1)
            elif keys[pygame.K_a]:
                self.player.move(-1, 0)
            elif keys[pygame.K_d]:
                self.player.move(1, 0)
            
            #interact with key, if player collide with key, key will be removed and a new key will be created
            if self.player.rect.colliderect(self.key.rect):
                self.key.kill()
                self.Score = self.Score+1
                next_pos = self.random_pos()
                self.key = objectModule.KeyModule(next_pos[0], next_pos[1])
                self.allsprite.add(self.key)
                
            #lock player in the gray area
            if self.player.rect.center[0] < 50:
                self.player.move_to(51, self.player.rect.center[1])
            elif self.player.rect.center[0] > 1150:
                self.player.move_to(1149, self.player.rect.center[1])
            if self.player.rect.center[1] < 50:
                self.player.move_to(self.player.rect.center[0], 51)
            elif self.player.rect.center[1] > 550:
                self.player.move_to(self.player.rect.center[0], 549)
            
            #check if player collide with bullet
            for bullet in self.bullet_list:
                #if collide, game will end
                if bullet.rect.colliderect(self.player.rect):
                    self.player.kill()
                    self.bullet_list.clear()
                    pygame.quit()
                    return self.Score
                #if bullet is out of screen, it will be removed
                if(bullet.rect.center[0] < 0 or bullet.rect.center[0] > self.screen.get_size()[0]):
                    bullet.kill()
                    self.bullet_list.remove(bullet)
                    continue
                bullet.update()
                
            self.screen.blit(self.bg, (0,0))    #merge the main background on the screen
            self.allsprite.draw(self.screen)    #merge all sprites on the screen
            self.clock.tick(60)                 #set fps
            pygame.display.update()             #update the screen






