import pygame

pygame.init()

w = 600
h = 600

screen = pygame.display.set_mode((w,h))

pygame.display.set_caption('Meu jogo em python')

bg = pygame.image.load('./assets/background.png').convert_alpha()
bg = pygame.transform.scale(bg, (w, h))

cat = pygame.image.load('./assets/cat.png').convert_alpha()
cat = pygame.transform.scale(cat, (100, 100))

rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    screen.blit(bg,(0,0))
    screen.blit(cat,(10,10))

    pygame.display.update()