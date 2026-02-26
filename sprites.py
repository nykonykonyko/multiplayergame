import pygame, pyautogui, random
pygame.init()
WIDTH,HEIGHT = pyautogui.size()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Projcontrol")
hueco = pygame.transform.scale(pygame.image.load("hueco.jpg"),(WIDTH,HEIGHT))
primera = pygame.transform.scale(pygame.image.load("starrk.png"),(150,200))
cuatro = pygame.transform.scale(pygame.image.load("ulq.webp"),(150,200))

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = primera

        self.rect = self.image.get_rect()
    def movement(self,keys):
        if keys[pygame.K_UP]:
            self.rect.move_ip(0,-10)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0,10)    
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-10,0)    
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(10,0)
spritegroup = pygame.sprite.Group()
p = Player() 
spritegroup.add(p)
while True:
    for e in pygame.event.get():

            if e.type == pygame.QUIT:
                pygame.quit()
    pressedkeys = pygame.key.get_pressed()

    p.movement(pressedkeys)

    spritegroup.draw(screen)
    pygame.display.update()
