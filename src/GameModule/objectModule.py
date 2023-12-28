import pygame


class KeyModule(pygame.sprite.Sprite):
    x = 0
    y = 0
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        
        #Draw the key
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        pygame.draw.circle(self.image, (255, 255, 0), (10, 10), 10, 0)
        
        #Set the position of the key
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
class PlayerModule(pygame.sprite.Sprite):
    x = 0
    y = 0
    dx = 0
    dy = 0
    speed = 0
    
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = speed
        
        #Draw the player
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        pygame.draw.circle(self.image, (0, 255, 0), (10, 10), 10, 0)
        
        #Set the position of the player
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.center = (self.x, self.y)
        
    def move(self, dx, dy):
        self.dx = dx * self.speed
        self.dy = dy * self.speed
        self.update()
    
    def move_to(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
    
class BulletModule(pygame.sprite.Sprite):
    posX = 0
    posY = 0
    speed = 0
    direction = 0   #0 = right, 1 = left, 2 = down, 3 = up
    
    def __init__(self, posX, posY, speed, direction, color):
        pygame.sprite.Sprite.__init__(self)
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.direction = direction
        
        #Draw the tower
        self.image = pygame.Surface([10, 10])
        self.image.fill((255, 255, 254))
        self.image.set_colorkey((255, 255, 254))
        pygame.draw.circle(self.image, color, (5, 5), 5, 0)
        
        #Set the position of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)

    def update(self):
        if(self.posX > 1200 or self.posX < 0):
            self.kill()
        elif(self.posY > 800 or self.posY < 0):
            self.kill()
        
        if(self.direction == 0):
            self.posX += self.speed
        elif(self.direction == 1):
            self.posX -= self.speed
        elif(self.direction == 2):
            self.posY += self.speed
        elif(self.direction == 3):
            self.posY -= self.speed
        self.rect.center = (self.posX, self.posY)

class BigBulletModule(pygame.sprite.Sprite):
    posX = 0
    posY = 0
    speed = 0
    direction = 0   #0 = right, 1 = left, 2 = down, 3 = up
    
    def __init__(self, posX, posY, speed, direction, color):
        pygame.sprite.Sprite.__init__(self)
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.direction = direction
        
        #Draw the tower
        self.image = pygame.Surface([40, 40])
        self.image.fill((255, 255, 254))
        self.image.set_colorkey((255, 255, 254))
        pygame.draw.circle(self.image, color, (20, 20), 20, 0)
        
        #Set the position of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)

    def update(self):
        if(self.posX > 1200 or self.posX < 0):
            self.kill()
        elif(self.posY > 800 or self.posY < 0):
            self.kill()
        
        if(self.direction == 0):
            self.posX += self.speed
        elif(self.direction == 1):
            self.posX -= self.speed
        elif(self.direction == 2):
            self.posY += self.speed
        elif(self.direction == 3):
            self.posY -= self.speed
        self.rect.center = (self.posX, self.posY)