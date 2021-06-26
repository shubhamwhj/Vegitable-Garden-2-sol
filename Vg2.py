
import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))

#Load the images
carrot_img = pygame.image.load("carrot.png").convert_alpha()
brinjal_img = pygame.image.load("brinjal.png").convert_alpha()
mushroom_img = pygame.image.load("mushroom.png").convert_alpha()
pumpkin_img = pygame.image.load("pumpkin.png").convert_alpha()
tomato_img = pygame.image.load("tomato.png").convert_alpha()

#creating objects of game
tomatoes=[]
mushrooms=[]
carrots=[]
brinjals=[]
pumpkins=[]

for i in range(1,6):
    tomatoes.append(pygame.Rect(i*60,50,40,40))

for i in range(1,6):
    mushrooms.append(pygame.Rect(i*60,150,40,40))

for i in range(1,6):
    carrots.append(pygame.Rect(i*60,250,40,40))

for i in range(1,6):
    brinjals.append(pygame.Rect(i*60,350,40,40))

for i in range(1,6):
    pumpkins.append(pygame.Rect(i*60,450,40,40))

                       
while True:    
    screen.fill((30,80,20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
             
    for tomato in tomatoes:        
        #pygame.draw.rect(screen,(223,80,50),tomato)
        screen.blit(tomato_img,tomato)
        
    for mushroom in mushrooms:        
        #pygame.draw.rect(screen,(220,220,220),mushroom)
        screen.blit(mushroom_img,mushroom)
    
    for carrot in carrots:        
        #pygame.draw.rect(screen,(250,20,20),carrot)
        screen.blit(carrot_img,carrot)
    
    for brinjal in brinjals:        
        #pygame.draw.rect(screen,(150,50,220),brinjal)
        screen.blit(brinjal_img,brinjal)
    
    for pumpkin in pumpkins:        
        #pygame.draw.rect(screen,(223,250,20),pumpkin)
        screen.blit(pumpkin_img,pumpkin)
    
    
    pygame.display.update()
    clock.tick(30)

