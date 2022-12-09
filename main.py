import subprocess
import sys

screen_width = 640
screen_height = 480
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

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
numberingRun = False
order = 1
pieces = []

def checkModule():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])

def numbering():
    for i, piece in enumerate(pieces):
        if i % 2 != 0:
            numbering = numberingFont.render(str(i + 1), True, BLACK)
        else:
            numbering = numberingFont.render(str(i + 1), True, WHITE)
        screen.blit(numbering, numbering.get_rect(center=[pieces[i][0], pieces[i][1]]))

def setWindow(): #todo 버튼 그래픽 추가 (undo, redo, numbering, new game, quit)
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("omok!!!")
    screen.fill((165, 138, 0))
    screen.fill((204, 102, 0), (10, 10, 460, 460))
    for i in range(19):
        pygame.draw.line(screen, BLACK, [10 + (460 / 18) * i, 10], [10 + (460 / 18) * i, 470])
        pygame.draw.line(screen, BLACK, [10, 10 + (460 / 18) * i], [470, 10 + (460 / 18) * i])
    return screen

def renderMenu(): #todo undoMenu, (531, 315, 58, 23), redoMenu, (532, 348, 57, 23), numberingMenu, (499, 381, 122, 23), newGameMenu, (504, 414, 112, 23), quit, (536, 447, 48, 23)
    undoMenu = menuFont.render("UNDO", True, BLACK)
    redoMenu = menuFont.render("REDO", True, BLACK)
    numberingMenu = menuFont.render("NUMBERING", True, BLACK)
    newGameMenu = menuFont.render("NEW GAME", True, BLACK)
    quitMenu = menuFont.render("QUIT", True, BLACK)
    screen.blit(undoMenu, (531, 315, 58, 23))
    screen.blit(redoMenu, (532, 348, 57, 23))
    screen.blit(numberingMenu, (499, 381, 122, 23))
    screen.blit(newGameMenu, (504, 414, 112, 23))
    screen.blit(quitMenu, (536, 447, 48, 23))

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
            if tempBoard[y][x] != 0:
                if tempBoard[y][x] == tempBoard[y][x + 1] == tempBoard[y][x + 2] == tempBoard[y][x + 3] == tempBoard[y][x + 4]:
                    return ['win', tempBoard[y][x]]
                else:
                    pass
            else:
                pass
def lShapeWin():
    for y in range(15):
        for x in range(19):
            if tempBoard[y][x] != 0:
                if tempBoard[y][x] == tempBoard[y + 1][x] == tempBoard[y + 2][x] == tempBoard[y + 3][x] == tempBoard[y + 4][x]:
                    return ['win', tempBoard[y][x]]
                else:
                    pass
            else:
                pass

def xShapeWin():
    for y in range(15):
        for x in range(15):
            if tempBoard[y][x] != 0:
                if tempBoard[y][x] == tempBoard[y + 1][x + 1] == tempBoard[y + 2][x + 2] == tempBoard[y + 3][x + 3] == \
                        tempBoard[y + 4][x + 4]:  #todo \방향 검사
                    return ['win', tempBoard[y][x]]
                else:
                    pass
            elif tempBoard[y + 4][x] != 0:
                if tempBoard[y + 4][x] == tempBoard[y + 3][x + 1] == tempBoard[y + 2][x + 2] == \
                        tempBoard[y + 1][x + 3] == tempBoard[y][x + 4]:  # todo /방향 검사
                    return ['win', tempBoard[y + 4][x]]
                else:
                    pass
            else:
                pass

def calResult():
    r = ㅡShapeWin() or lShapeWin() or xShapeWin()
    return r

def resetBoard():
    global pieces
    pieces = []
    for x in range(19):
        for y in range(19):
            charBoard[y][x] = 0

redoList = []

def undo():
    global order
    try:  # undo기능
        x = pisXPos.index(pieces[-1][0])
        y = pisYPos.index(pieces[-1][1])
        charBoard[y][x] = 0
        redoList.append(pieces[-1])
        del pieces[-1]
        order -= 1
    except:
        pass

def redo():
    global order
    try:
        pieces.append(redoList[-1])
        del redoList[-1]
        order += 1
    except:
        pass

def menuClick(ypos):
    global numberingRun
    global tempBoard
    if 315 <= ypos <= 338:
        print("clicked undo")
        undo()
    elif 348 <= ypos <= 371:
        print("clicked redo")
        redo()
    elif 381 <= ypos <= 404:
        print("clicked numbering")
        numberingRun = not numberingRun
    elif 414 <= ypos <= 437:
        print("clicked new game")
        numberingRun = False
        resetBoard() #todo 다시하기 기능 만들기
    elif 447 <= ypos <= 470:
        print("clicked quit")
        global run
        run = False

if __name__ == '__main__':

    checkModule()

    pygame = __import__('pygame')

    clock = pygame.time.Clock()

    pygame.init()

    tempBoard = charBoard

    numberingFont = pygame.font.SysFont("arial", 15, True, False)
    menuFont = pygame.font.SysFont("arial", 20, True, False)

    clock.tick(30)

    screen = setWindow()

    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            elif e.type == pygame.MOUSEBUTTONUP:
                pos = list(pygame.mouse.get_pos())
                if whereClick(pos[0]) == 'board':
                    try:
                        setPos = setPiecePos(pos[0], pos[1])
                        x = pisXPos.index(setPos[0])
                        y = pisYPos.index(setPos[1])
                        if order % 2 != 0 and tempBoard[y][x] == 0:
                            tempBoard[y][x] = 1
                            pieces.append([setPos[0], setPos[1], order])
                            order += 1
                            redoList = []
                        elif order % 2 == 0 and tempBoard[y][x] == 0:
                            tempBoard[y][x] = 2
                            pieces.append([setPos[0], setPos[1], order])
                            order += 1
                            redoList = []
                    except:
                        pass
                    else:
                        pass
                else: #todo 메뉴클릭구현
                        menuClick(pos[1])
            setWindow()
            for p in pieces:
                drawPiece(p[0], p[1], p[2])
            result = calResult()
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
        if numberingRun:
            numbering()
        renderMenu()
        pygame.display.update()
