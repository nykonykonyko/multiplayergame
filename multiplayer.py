import pygame, pyautogui
pygame.init()
WIDTH,HEIGHT = pyautogui.size()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Projcontrol")
hueco = pygame.transform.scale(pygame.image.load("hueco.jpg"),(WIDTH,HEIGHT))
primera = pygame.transform.scale(pygame.image.load("starrk.png"),(150,200))
cuatro = pygame.transform.scale(pygame.image.load("ulq.webp"),(150,200))
border = pygame.Rect(WIDTH/2-10,0,20,HEIGHT)


def display(rectleft,rectright):
    screen.blit(hueco,(0,0))
    screen.blit(primera,(rectright.x,rectright.y))
    screen.blit(cuatro,(rectleft.x,rectleft.y))
    pygame.draw.rect(screen,"black",border)

def controlPlayers(rectleft,rectright,keypressed):
    if keypressed[pygame.K_UP] and rectright.y > 0:
        rectright.y -= 20
    if keypressed[pygame.K_DOWN] and rectright.y < HEIGHT-rectright.height :
        rectright.y += 20     
    if keypressed[pygame.K_RIGHT] and rectright.x <  WIDTH - rectright.width :
        rectright.x += 20
    if keypressed[pygame.K_LEFT] and rectright.x > border.x + border.width: 
        rectright.x -= 20    

def main():
    rectleft = pygame.Rect(300,HEIGHT/2,150,200)
    rectright = pygame.Rect(WIDTH-300,HEIGHT/2,150,200)
    
    while True:
        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                pygame.quit()

        display(rectleft,rectright)
        keypressed = pygame.key.get_pressed()
        controlPlayers(rectleft,rectright,keypressed)
        pygame.display.update()
main()        