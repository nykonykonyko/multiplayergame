import random,pgzrun
enemies = []
slashes = []
WIDTH,HEIGHT =  1000,600
TITLE = "Galaga game"
character = Actor("shinji")
character.pos = 300,550
character.dead = False
character.countdown = 90
def draw():
    screen.blit("innerworld",(0,0))
    if not character.dead:
        character.draw()
    for s in slashes:
        s.draw()
    for i in enemies:
        i.draw()
def update():
    if not character.dead:
      character.x = character.x + 1
      if keyboard.left:
        character.x -= 10
      if keyboard.right:
        character.x += 10
      if character.x < 0:
        character.x = WIDTH
      if character.x > WIDTH:
        character.x = 0
      character.y = character.y + 1
      if keyboard.up:
        character.y -= 10
      if keyboard.down:
        character.y += 10
      if character.y < 0:
        character.y = HEIGHT
      if character.y > HEIGHT:
        character.y = 0
    for e in enemies:
        e.x += 5
        for s in slashes:
            if e.colliderect(s):
                enemies.remove(e)
                slashes.remove(s)
                break 
        if e.colliderect(character):
            character.dead = True
    if character.dead:
        character.countdown -= 1
    if character.countdown == 0:
        character.dead = False
        character.countdown = 90        
    if keyboard.space and not character.dead :
          slash = Actor("slash")
          slash.pos = character.x,character.y-50
          slashes.append(slash)
    for i in slashes:
            i.x = i.x-10


def create_enemy():
    enemy = Actor("bug")
    enemy.pos = 0,random.randint(50,950)    
    enemies.append(enemy)
clock.schedule_interval(create_enemy,1.0) 
pgzrun.go()