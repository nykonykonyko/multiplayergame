import pygame, pyautogui, random
pygame.init()
WIDTH,HEIGHT = pyautogui.size()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Projcontrol")
hueco = pygame.transform.scale(pygame.image.load("hueco.jpg"),(WIDTH,HEIGHT))
primera = pygame.transform.scale(pygame.image.load("starrk.png"),(150,200))
cuatro = pygame.transform.scale(pygame.image.load("ulq.webp"),(150,200))
border = pygame.Rect(WIDTH/2-10,0,20,HEIGHT)

def  handlebullets(rectleft,rectright,lance,cero,reishi,rayshi):
    for i in lance:
        i.x += 10
        if i.x > WIDTH:
            lance.remove(i)
        for j in cero:
            if i.colliderect(j):
                lance.remove(i)
                cero.remove(j)
                break 
        if i.colliderect(rectright):
            lance.remove(i)
            rayshi -= 1       

def display(rectleft,rectright):
    screen.blit(hueco,(0,0))
    screen.blit(primera,(rectright.x,rectright.y))
    screen.blit(cuatro,(rectleft.x,rectleft.y))
    pygame.draw.rect(screen,"black",border)

def controlPlayers(rectleft,rectright,keypressed):
    if rectleft.right > border.left:
        rectleft.right = border.left
    if keypressed[pygame.K_UP] and rectright.y > 0:
        rectright.y -= 20
    if keypressed[pygame.K_DOWN] and rectright.y < HEIGHT-rectright.height :
        rectright.y += 20     
    if keypressed[pygame.K_RIGHT] and rectright.x <  WIDTH - rectright.width :
        rectright.x += 20
    if keypressed[pygame.K_LEFT] and rectright.x > border.x + border.width: 
        rectright.x -= 20    
    
    if random.randint(1,100)<5:
        rectleft.x += random.randint(-100,100) 
        rectleft.y += random.randint(-100,100)
        if rectleft.x < 0:
            rectleft.x = 50
        if rectleft.y > HEIGHT:
            rectleft.y = 300

            
def main():
    rectleft = pygame.Rect(300,HEIGHT/2,150,200)
    rectright = pygame.Rect(WIDTH-300,HEIGHT/2,150,200)
    cero = []
    lance = []
    reishi = 10
    rayshi = 10

    
    while True:
        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                pygame.quit()
            if e.time == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    r = pygame.Rect(rectright.x+20,rectright.y+40,50,50)
                    cero.append(r)

        if random.randint(1,50)< 5:
            r = pygame.Rect(rectleft.x+40,rectleft.y+40,50,50)
            lance.append(r)
            
        handlebullets(rectleft,rectright,lance,cero,reishi,rayshi)
        display(rectleft,rectright)
        keypressed = pygame.key.get_pressed()
        controlPlayers(rectleft,rectright,keypressed)
        pygame.display.update()
main()        