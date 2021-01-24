import pygame

screen_width = 640
screen_height = 480
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

board = pygame.image.load("images//board.jpg")

pisXPos = [[]] # [[xpos, yops, setpos]]


run = True
order = 1
pieces = []

clock = pygame.time.Clock()

def setWindow():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("omok!!!")
    screen.fill((165, 138, 0))
    screen.fill((204, 102, 0), (10, 10, 460, 460))
    for i in range(19):
        pygame.draw.line(screen, BLACK, [10 + (460 / 18) * i, 10], [10 + (460 / 18) * i, 470])
        pygame.draw.line(screen, BLACK, [10, 10 + (460 / 18) * i], [470, 10 + (460 / 18) * i])
    return screen

def whereClick(xpos):
    if xpos <= 475:
        return 'board'
    else:
        return 'menu'

def setPiecePos(xpos, ypos): # 바둑알 위치 조정 함수
    pass

def drawPiece(xpos, ypos, order):
    if order % 2 != 0:
        pygame.draw.circle(screen, BLACK, [xpos, ypos], 10)
    else:
        pygame.draw.circle(screen, WHITE, [xpos, ypos], 10)

if __name__ == '__main__':
    pygame.init()

    clock.tick(30)

    screen = setWindow()

    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            elif e.type == pygame.MOUSEBUTTONUP:
                pos = list(pygame.mouse.get_pos())
                if whereClick(pos[0]) == 'board':
                    pieces.append([pos[0], pos[1], order])
                    # drawPiece(pos[0], pos[1])
                    order += 1
                else:
                    try:
                        del pieces[-1]
                        order -= 1
                    except:
                        pass
            setWindow()
            for p in pieces:
                drawPiece(p[0], p[1], p[2])

        pygame.display.update()