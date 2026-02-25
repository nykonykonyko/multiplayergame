import pygame, pyautogui, random
pygame.init()
WIDTH,HEIGHT = pyautogui.size()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Projcontrol")
hueco = pygame.transform.scale(pygame.image.load("hueco.jpg"),(WIDTH,HEIGHT))
primera = pygame.transform.scale(pygame.image.load("starrk.png"),(150,200))
cuatro = pygame.transform.scale(pygame.image.load("ulq.webp"),(150,200))
border = pygame.Rect(WIDTH/2-10,0,20,HEIGHT)
gamestate = "start"

lanceimage = pygame.transform.scale(pygame.image.load("thorn.webp"),(50,50))
ceroimage = pygame.transform.scale(pygame.image.load("darkk.png"),(50,50))
lanceimage = pygame.transform.rotate(lanceimage,-45)

titlefont = pygame.font.SysFont("arial",70)
font = pygame.font.SysFont("arial",35)
starttext = titlefont.render("Bleach Battleground",True,"orange")
instructiontext = font.render("You are the character on the right. Fight to survive \n" 
"Space to shoot",1,"purple")
gameovertext = titlefont.render("GAME OVER",0,"red")
rayshi = 10
reishi = 10


def  handlebullets(rectleft,rectright,lance,cero):
    global rayshi,reishi
    print(rayshi,reishi)
    for i in lance:
        i.x += 10
         
        if i.x > WIDTH:
            lance.remove(i)
        if i.colliderect(rectright):
            lance.remove(i)
            rayshi -= 1 
            continue 
        for j in cero:
            if i.colliderect(j):
                lance.remove(i)
                cero.remove(j)

                break 

    

    for j in cero:
        j.x -= 10
        if j.x < 0:
            cero.remove(j)            
        if j.colliderect(rectleft):
            cero.remove(j)
            print(reishi,"bullet")
            reishi -= 1     

def display(rectleft,rectright,lance,cero,winner):
    print(gamestate)

    screen.blit(hueco,(0,0))
    screen.blit(primera,(rectright.x,rectright.y))
    screen.blit(cuatro,(rectleft.x,rectleft.y))
    if gamestate == "start":
        screen.blit(starttext,(WIDTH/2-100,HEIGHT/3))
        screen.blit(instructiontext,(WIDTH/3,HEIGHT/3+200))
    elif gamestate == "play":       
        pygame.draw.rect(screen,"black",border)

        for i in lance:
            #pygame.draw.rect(screen,"green",i)
            screen.blit(lanceimage,(i.x,i.y))
        for i in cero:
            #pygame.draw.rect(screen,"cyan",i)  
            screen.blit(ceroimage,(i.x,i.y))
        
        rayshitext = titlefont.render(f"Lives:{rayshi}",0,"cyan" )
        reishitext = titlefont.render(f"Lives:{reishi}",0,"purple" )

        screen.blit(rayshitext,(WIDTH-250,50))
        screen.blit(reishitext,(50,50))
    else:
        screen.blit(gameovertext,(WIDTH/2-50,HEIGHT/2))
        winnertext = titlefont.render(f"{winner} wins the game",0,"purple")
        screen.blit(winnertext,(WIDTH/3-200,HEIGHT/2+200))

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
        if rectleft.bottom > HEIGHT:
            rectleft.y = HEIGHT - rectleft.height
        if rectleft.top < 50:
            rectleft.y = 50
        if rectleft.right > border.x:
            rectleft.x = border.x - rectleft.width    
            
def main():
    global gamestate, reishi, rayshi
    rectleft = pygame.Rect(300,HEIGHT/2,150,200)
    rectright = pygame.Rect(WIDTH-300,HEIGHT/2,150,200)
    cero = []
    lance = []
    winner = None

    
    while True:
        
        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    if gamestate == "play":
                        r = pygame.Rect(rectright.x+20,rectright.y+40,50,20)
                        cero.append(r)
                    else:
                        gamestate = "play"
                        reishi = 10
                        rayshi = 10
        if reishi == 0:
            winner = "Primera" 
        if rayshi == 0:
            winner = "Cuatro"
        if winner:
            gamestate = "end"    
        print(reishi,rayshi,winner)                   
        if random.randint(1,100)< 5 and gamestate == "play" :
            r = pygame.Rect(rectleft.x+40,rectleft.y-20,50,20)
            lance.append(r)

        display(rectleft,rectright,lance,cero,winner)   
        if gamestate == "play" :
            handlebullets(rectleft,rectright,lance,cero)
        
            keypressed = pygame.key.get_pressed()
            controlPlayers(rectleft,rectright,keypressed)
        pygame.display.update()
main()        