import pygame
import time
import random
pygame.init()

branco = (255, 255, 255)
amarelo = (255, 255, 102)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
azul = (50, 153, 213)
verde = (0, 255, 0)

largura_dis = 800
altura_dis = 600
dis = pygame.display.set_mode((largura_dis, altura_dis))

pygame.display.set_caption('Jogo da Cobra por Nathan')

clock = pygame.time.Clock()

tamanho_bloco_cobra = 10
velocidade_cobra = 15

fonte_estilo = pygame.font.SysFont("bahnschrift", 25)
fonte_pontuacao = pygame.font.SysFont("comicsansms", 35)

def mostrar_pontuacao(pontuacao):
    valor = fonte_pontuacao.render("Sua Pontuação: " + str(pontuacao), True, amarelo)
    dis.blit(valor, [0, 0])

def nossa_cobra(tamanho_bloco_cobra, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(dis, preto, [x[0], x[1], tamanho_bloco_cobra, tamanho_bloco_cobra])

def mensagem(msg, cor):
    mesg = fonte_estilo.render(msg, True, cor)
    dis.blit(mesg, [largura_dis/2 - mesg.get_width()/2, altura_dis/2 - mesg.get_height()/2])

def gameLoop():
    jogo_acabou = False
    jogo_fechado = False

    x1 = largura_dis / 2
    y1 = altura_dis / 2

    x1_mudanca = 0
    y1_mudanca = 0
    lista_cobra = []
    tamanho_cobra = 1
    foodx = round(random.randrange(0, largura_dis - tamanho_bloco_cobra) / 10.0) * 10.0
    foody = round(random.randrange(0, altura_dis - tamanho_bloco_cobra) / 10.0) * 10.0

    while not jogo_acabou:

        while jogo_fechado == True:
            dis.fill(vermelho)
            mensagem("Você Perdeu! Pressione Q-Para Sair ou C-Jogar Novamente", preto)
            mostrar_pontuacao(tamanho_cobra - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        jogo_acabou = True
                        jogo_fechado = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo_acabou = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_bloco_cobra
                    y1_mudanca = 0
                elif event.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_bloco_cobra
                    y1_mudanca = 0
                elif event.key == pygame.K_UP:
                    x1_mudanca = 0
                    y1_mudanca = -tamanho_bloco_cobra
                elif event.key == pygame.K_DOWN:
                    x1_mudanca = 0
                    y1_mudanca = tamanho_bloco_cobra
        
        if x1 >= largura_dis or x1 < 0 or y1 >= altura_dis or y1 < 0:
            jogo_fechado = True
        
        x1 += x1_mudanca
        y1 += y1_mudanca
        dis.fill(azul)
        pygame.draw.rect(dis, verde, [foodx, foody, tamanho_bloco_cobra, tamanho_bloco_cobra])
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > tamanho_cobra:
            del lista_cobra[0]
        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                jogo_fechado = True
        nossa_cobra(tamanho_bloco_cobra, lista_cobra)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, largura_dis - tamanho_bloco_cobra) / 10.0) * 10.0
            foody = round(random.randrange(0, altura_dis - tamanho_bloco_cobra) / 10.0) * 10.0
            tamanho_cobra += 1
            print('Yummy!!')
        clock.tick(velocidade_cobra)

    pygame.quit()
    quit()

gameLoop()
