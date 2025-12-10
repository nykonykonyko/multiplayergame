import pygame, pyautogui
pygame.init()
WIDTH,HEIGHT = pyautogui.size()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Projcontrol")
hueco = pygame.transform.scale(pygame.image.load("hueco.jpg"),(WIDTH,HEIGHT))
primera = pygame.transform.scale(pygame.image.load("starrk.png"),(150,200))
cuatro = pygame.transform.scale(pygame.image.load("ulq.webp"),(150,200))
border = pygame.Rect(WIDTH/2-10,0,20,HEIGHT)


def display():
    screen.blit(hueco,(0,0))
    screen.blit(primera,(WIDTH-300,HEIGHT/2))
    screen.blit(cuatro,(300,HEIGHT/2))
    pygame.draw.rect(screen,"black",border)



while True:
    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            pygame.quit()

    display()
    pygame.display.update()