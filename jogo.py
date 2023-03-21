from pygame import display, init, time as pytime, font, draw, event, quit as pyquit
from pygame import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, K_UP, K_s, K_j
import random
from PIL import ImageColor

init()

# aqui passamos o nome de uma cor e pegamos o código rgb
# rgb é uma forma de criar cores no computador a partir de 3 cores
# rgb = red, green, blue
branco = ImageColor.getrgb("white")
amarelo = ImageColor.getrgb("yellow")
preto = ImageColor.getrgb("black")
vermelho = ImageColor.getrgb("red")
verde = ImageColor.getrgb("green")
azul = ImageColor.getrgb("blue")

largura = 600
altura = 400
# a função display cria uma janela
dis = display.set_mode((largura, altura))
# nome do jogo
display.set_caption("Snake Game")
# tempo de atualização da tela
clock = pytime.Clock()
# medida inicial da cobra
snake_body = 10
# criando funções para reutiliza-las
# score printa a pontuação na tela


def score(s): return dis.blit(
    font.SysFont("arial.ttf", 35).render(f'Pontuação: {s - 1}', True, azul),
    [0, 0])
# coloca alguma mensagem na tela
# usamos a font Sysfont para a mensagem ter uma fonte especifica


def message(m, c, pos): return dis.blit(
    font.SysFont("Segoe UI", 25).render(m, True, c), pos)

# aqui criamos a comida para a cobra comer
# passamos alguns parametros, como a posição e o espaço que vai ter da tela
# a comida irá aparecer aleatoriamente na tela, porém existe a tela de score na parte de cima, por isso precisamos passar o esp


def criar_comida(esp, pos): return round(
    random.randrange(esp, pos - 10) / 10) * 10
# aqui iniciamos o loop do jogo


def jogo():
    # começa carregando algumas informações
    game_over = False
    fechar = False

    x1 = largura / 2
    y1 = altura / 2

    x1_change = 0
    y1_change = 0
    # o tamanho da cobra e quanto deve ser acrescentado
    corpo = []
    tamanho = 1
    level = 10
    # aqui utilizamos a função criada acima
    # damos um espaçamento de 30 para desconsiderar a parte do score
    comida_x = criar_comida(0, largura)
    comida_y = criar_comida(30, altura)
    # loop while, enquanto não houver game over o loop continua
    while not game_over:
        # aqui é o loop para fechar o jogo
        while fechar:
            dis.fill(branco)
            message("Game Over", vermelho, [250, 60])
            message("Aperte J para jogar novamente ou S para sair",
                    preto, [50, 100])
            score(tamanho)
            display.update()

            for e in event.get():
                if e.type == KEYDOWN:
                    if e.type == QUIT:
                        game_over = True
                        fechar = False
                    # a tecla 's' é usado para sair do jogo
                    if e.key == K_s:
                        game_over = True
                        fechar = False
                    # a tecla 'j' é usado para continar no jogo
                    if e.key == K_j:
                        jogo()
            # aqui criamos a movimentação do jogo
            # toda vez ele atualiza e ve se algum desses movimentos aconteceu
        for e in event.get():
            if e.type == QUIT:
                game_over = True
            if e.type == KEYDOWN:
                if e.key == K_LEFT:
                    # quando clicamos para esquerda o eixo y não muda, pois é um movimento horizontal
                    # porém o x vai decrementar o tamanho do corpo da cobra, no caso 10
                    x1_change = -snake_body
                    y1_change = 0
                elif e.key == K_RIGHT:
                    # para direita o x aumenta 10
                    x1_change = snake_body
                    y1_change = 0
                elif e.key == K_UP:
                    y1_change = -snake_body
                    x1_change = 0
                elif e.key == K_DOWN:
                    y1_change = snake_body
                    x1_change = 0
        # se uma dessas condições for verdade o jogo fecha
        if any([x1 >= largura, x1 < 0, y1 >= altura, y1 < 0]):
            fechar = True
        # as alterações na movimentação feitas acima serão somadas
        x1 += x1_change
        y1 += y1_change
        # aqui definimos o fundo como branco
        dis.fill(branco)
        # aqui desenhamos a comida
        draw.rect(dis, vermelho, [comida_x, comida_y, snake_body, snake_body])
        # aqui é a cobra
        cabeca = []
        cabeca.append(x1)
        cabeca.append(y1)
        corpo.append(cabeca)
        # se o tamanho do corpo for maior que o tamanho o corpo vai deletar o primeiro elemento da cobra
        if len(corpo) > tamanho:
            del corpo[0]
        # pega todos os elementos do corpo e verifica se a cabeça está no mesmo lugar que o corpo
        # ou seja, se a pessoa apertou para baixo com a cobra subindo
        for x in corpo[:-1]:
            if x == cabeca:
                fechar == True
        # desenhando a cobra
        [draw.rect(dis, verde, [x[0], x[1], snake_body, snake_body])
         for x in corpo]
        score(tamanho)  # passando a função criada no inicio e indicando o valor
        # mostrando tudo isso no display
        display.update()
        # mecanismo para verificar se a cobra passou pela mação e aumentar o tamanho dela
        if x1 == comida_x and y1 == comida_y:
            comida_x = criar_comida(0, largura)
            comida_y = criar_comida(30, altura)
            tamanho += 1
            # a velocidade vai aumentar para aumentar a dificuldade
            level += 2

        clock.tick(level)
    # encerrando o jogo
    pyquit()
    quit()


jogo()
