import pygame

screen_width = 640
screen_height = 480
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

board = pygame.image.load("images//board.jpg")
charBoard = [ # 0 : 알 없음 1 : 흑돌 2 : 백돌
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

pisXPos = [10 + (460 / 18) * i for i in range(19)]
pisYPos = [10 + (460 / 18) * i for i in range(19)]

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
    for x in pisXPos:
        for y in pisYPos:
            if x - (460 / 18) / 2 <= xpos < x + (460 / 18) / 2 and y - (460 / 18) / 2 <= ypos < y +(460 / 18) / 2:
                return [x, y]
            else:
                pass

def drawPiece(xpos, ypos, order):
    if order % 2 != 0:
        pygame.draw.circle(screen, BLACK, [xpos, ypos], 10)
    else:
        pygame.draw.circle(screen, WHITE, [xpos, ypos], 10)

def ㅡShapeWin(): # ㅡ모양 검사
    for y in range(19):
        for x in range(15):
            if charBoard[y][x] != 0:
                if charBoard[y][x] == charBoard[y][x + 1] == charBoard[y][x + 2] == charBoard[y][x + 3] == charBoard[y][x + 4]:
                    return ['win', charBoard[y][x]]
                else:
                    pass
            else:
                pass
def lShapeWin(): #todo l모양 승리 조건함수 완성하기
    pass

def xShapeWin(): #todo 대각선 모양 승리조건함수 완성하기
    pass

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
                    setPos = setPiecePos(pos[0], pos[1])
                    pieces.append([setPos[0], setPos[1], order])
                    x = pisXPos.index(setPos[0])
                    y = pisYPos.index(setPos[1])
                    if order % 2 != 0:
                        charBoard[y][x] = 1
                    else:
                        charBoard[y][x] = 2
                    # drawPiece(pos[0], pos[1])
                    order += 1
                else:
                    try:
                        x = pisXPos.index(pieces[-1][0])
                        y = pisYPos.index(pieces[-1][1])
                        charBoard[y][x] = 0
                        del pieces[-1]
                        order -= 1
                    except:
                        pass
            setWindow()
            for p in pieces:
                drawPiece(p[0], p[1], p[2])
            result = ㅡShapeWin()
            try:
                if result[0] == 'win':
                    if result[1] == 1:
                        print('흑 승리')
                    else:
                        print('백 승리')
                    run = False
                else:
                    pass
            except:
                pass

        pygame.display.update()