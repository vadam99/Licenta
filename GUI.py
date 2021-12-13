from main import *
from Btn import *

# (Pentru folosirea gratuita a fisierului "sudoku.png") -> Icons made by https://www.freepik.com from www.flaticon.com
# (Butoanele QuitBtn si StartBtn au fost create cu ajutorul https://www.imagefu.com/create/button
""" Sursa imaginii din background: 
https://www.stiridinlume.ro/cand-unde-cum/sudoku-reguli-ce-este-sudoku-cine-l-a-inventat-si-cum-se-joaca-43587.html"""

pygame.init()

screenSize = 1000  # default = 1000

boardSize = screenSize // 1.302  # default = 768

screenOffset = screenSize // 10  # Distanta dintre marginea ecranului si tabla de joc.

screen = pygame.display.set_mode((screenSize, screenSize))  # Window
font = pygame.font.Font(None, screenSize // 12)
bg = pygame.image.load("sudokubackground.jpg")

pygame.display.set_caption("SUDOKU!")  # Titlul
icon = pygame.image.load("sudoku.png")  # Iconita
pygame.display.set_icon(icon)

StartImg = pygame.image.load('StartBtn.png')
StartBtn = Btn(screenSize // 5, screenSize // 4, StartImg, screenSize / 1000)  # Scale = screenSize / 1000

SolveImg = pygame.image.load('SolveBtn.png')

PlayImg = pygame.image.load('PlayBtn.png')
#  StartPlayingBtn = Btn(screenOffset + 610 * screenSize / 3000, screenSize / 1.11, PlayImg, screenSize / 3000)
StartPlayingBtn = Btn(screenSize // 5, screenSize // 2, PlayImg, screenSize / 1000)  # Scale = screenSize / 1000

BackImg = pygame.image.load('BackBtn.png')
BackBtn = Btn(boardSize / 2, screenSize / 1.11, BackImg, screenSize / 3000)

QuitImg = pygame.image.load('QuitBtn.png')
QuitBtn = Btn(screenSize // 5, screenSize // 1.33, QuitImg, screenSize / 1000)  # Scale = screenSize / 1000

exec = True
startClicked = False
startedPlaying = False
solveClicked = False
background = False
backClick = False

#print(copie_tabla2)
copie_tabla2 = genereaza_tabla()
copie_tabla_insert = [[copie_tabla2[i][j] for j in range(len(copie_tabla2[0]))] for i in range(len(copie_tabla2))]  # Folosita pentru update la user_insert

print(bkt())  # Trebuie apelat pentru a genera solutia


def draw_background():
    screen.fill(pygame.Color("white"))
    pygame.draw.rect(screen, pygame.Color("black"), pygame.Rect(screenOffset, screenOffset, boardSize, boardSize), screenSize // 100)  # Cadrul tablei de joc, screenOffset = 100
    i = 1
    while i < 9:
        # 85.3 = 768/9 = n
        n = boardSize / 9
        if i % 3 != 0:
            l_width = screenSize // 200
        else:
            l_width = screenSize // 100  # Marcam zonele prin linii mai groase.
            # boardSize = 768
        pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2((i * n) + screenOffset, screenOffset), pygame.Vector2((i * n) + screenOffset, boardSize + screenOffset), l_width)
        pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2(screenOffset, (i * n) + screenOffset), pygame.Vector2(boardSize + screenOffset, (i * n) + screenOffset), l_width)
        i += 1


def draw_tabla(board, col):
    n = boardSize / 9  # 85.3 = 768 / 9
    offset = screenOffset - screenSize // 62.5 + n // 2  # Formula pentru afisarea in mijloc a numerelor
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                number = font.render(str(board[i][j]), True, pygame.Color(col))
                screen.blit(number, pygame.Vector2((j * n) + offset, (i * n) + offset - 1000 // 166.66))


def draw_solutie():
    print(bkt())  # Trebuie apelat pentru a genera solutia
    n = boardSize / 9  # 111.1 = 1000 / 9
    offset = screenOffset - screenSize // 62.5 + n // 2  # Formula pentru afisarea in mijloc a numerelor
    for i in range(9):
        for j in range(9):
            if copie_tabla2[i][j] == 0:  # Dorim ca numerele care au fost initial pe tabla de joc sa ramana colorate cu "darkgreen", iar cele inserate de solver sa fie "red".
                number = font.render(str(copie_tabla[i][j]), True, pygame.Color("red"))  # Punem solutia din copie_tabla
                screen.blit(number, pygame.Vector2((j * n) + offset, (i * n) + offset - 1000 // 166.66))
            else:
                number = font.render(str(copie_tabla2[i][j]), True, pygame.Color("darkgreen"))
                screen.blit(number, pygame.Vector2((j * n) + offset, (i * n) + offset - 1000 // 166.66))


def quitFunctionality():
    if QuitBtn.draw(screen):  # Afisam butonul de exit + verificam daca e apasat
        print('Exit')
        global exec           # Folosim variabila globala exec
        exec = False


def startFunctionality():
    if StartBtn.draw(screen):
        print('Start')
        global startClicked
        startClicked = True


def startPlayingFunctionality():
    if StartPlayingBtn.draw(screen):
        print('Start Playing')
        global startedPlaying
        startedPlaying = True



def solveFunctionality():
    if SolveBtn.draw(screen):
        print('Solved!')
        global solveClicked
        solveClicked = True


def backFunctionality():
    if BackBtn.draw(screen):
        print('Back')
        global backClick
        backClick = True


def drawMenuText(x, y, txt, color, size):
    menufont = pygame.font.SysFont("lato", size)
    text = menufont.render(txt, True, color)
    textbox = text.get_rect()
    textbox.center = (x, y)
    screen.blit(text, textbox)


def drawMenu():
    screen.blit(bg, (0, 0))
    drawMenuText(x - 2, y - 2, "SUDOKU SOLVER", "darkgreen", screenSize // 7)
    drawMenuText(x + 2, y - 2, "SUDOKU SOLVER", "darkgreen", screenSize // 7)
    drawMenuText(x - 2, y + 2, "SUDOKU SOLVER", "darkgreen", screenSize // 7)
    drawMenuText(x + 2, y + 2, "SUDOKU SOLVER", "darkgreen", screenSize // 7)
    drawMenuText(x, y, "SUDOKU SOLVER", "white", screenSize // 7)


x = screenSize // 2
y = screenOffset - screenOffset // 4

block = False


def user_insert(position):
    global exec
    global QuitBtn
    global BackBtn
    global block
    global copie_tabla_insert
    n = boardSize / 9  # 85.3 = 768 / 9
    offset = screenOffset - screenSize // 62.5 + n // 2  # Formula pentru afisarea in mijloc a numerelor
    i = int((position[1] - screenOffset) // n)
    j = int((position[0] - screenOffset) // n)  # Coordonata y o atribuim liniilor, iar x coloanelor
    while True:
        win = True
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exec = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key <= 48 or event.key > 57:  # 48 = 0 in ASCII, dorim si ca orice alt input dat sa ne stearga inputul anterior
                    copie_tabla_insert[i][j] = 0
                    print("ZERO", copie_tabla_insert[i][j])
                    pygame.draw.rect(screen, "white", (int((j * n) + offset - n // 8), int((i * n) + offset - n // 8), int(n // 1.6), int(n // 1.6)))
                    pygame.display.flip()
                    return
                if 0 < event.key - 48 < 10:  # Numar intre 1 si 9
                    pygame.draw.rect(screen, "white", (int((j * n) + offset - n // 8), int((i * n) + offset - n // 8), int(n // 1.6), int(n // 1.6)))
                    val = font.render(str(event.key - 48), True, "red")
                    screen.blit(val, pygame.Vector2((j * n) + offset, (i * n) + offset - 1000 // 166.66))
                    copie_tabla_insert[i][j] = event.key - 48
                    print("VALOARE", copie_tabla_insert[i][j])
                    pygame.display.flip()
                    if not sudoku_valid(copie_tabla_insert):
                        win = False
                    if win == True:
                        block = True
                        print("WIN!!!")
                        #copie_tabla2 = genereaza_tabla()
                    return
                return


while exec:
    n = boardSize / 9
    offset = screenOffset - screenSize // 62.5 + n // 2
    if startClicked == False and startedPlaying == False:
        drawMenu()
        quitFunctionality()  # Afisam butonul de quit
        startFunctionality()  # Afisam butonul de start
        startPlayingFunctionality()

    if startClicked == True and startedPlaying == False:
        if solveClicked == True and backClick == False:
            draw_background()
            background = True
            draw_solutie()
            backFunctionality()
            quitFunctionality()  # Afisam butonul Quit si pe pagina cu tabla de joc cu solutia generata

        elif backClick == True:
            copie_tabla2 = genereaza_tabla()
            copie_tabla_insert = [[copie_tabla2[i][j] for j in range(len(copie_tabla2[0]))] for i in range(len(copie_tabla2))]
            backClick = False
            startClicked = False
            solveClicked = False
            background = False
            drawMenu()
            QuitBtn = Btn(screenSize // 5, screenSize // 1.33, QuitImg, screenSize / 1000)  # Scale = screenSize / 1000
            quitFunctionality()  # Afisam butonul de quit
            startFunctionality()  # Afisam butonul de start
            startPlayingFunctionality()

        else:
            draw_background()
            background = True
            draw_tabla(copie_tabla2, "darkgreen")
            SolveBtn = Btn(screenOffset, screenSize / 1.11, SolveImg, screenSize / 3000)
            QuitBtn = Btn(boardSize + screenOffset - 610 * screenSize / 3000, screenSize / 1.11, QuitImg, screenSize / 3000)  # 610 = lungimea imaginii, iar screenSize / 3000 e scalarea
            quitFunctionality()  # Afisam butonul Quit si pe pagina cu tabla de joc
            solveFunctionality()
            backFunctionality()
    pygame.display.flip()  # Update la display


    for event in pygame.event.get():
        if startedPlaying == True:  # Daca am ales sa dam pe Play
            if background == False and backClick == False:
                draw_background()
                draw_tabla(copie_tabla2, "darkgreen")
                background = True
                pygame.display.flip()  # Update la display
            QuitBtn = Btn(boardSize + screenOffset - 610 * screenSize / 3000, screenSize / 1.11, QuitImg, screenSize / 3000)  # 610 = lungimea imaginii, iar screenSize / 3000 e scalarea
            quitFunctionality()
            pygame.display.flip()
            backFunctionality()

            if backClick == True:
                copie_tabla2 = genereaza_tabla()
                copie_tabla_insert = [[copie_tabla2[i][j] for j in range(len(copie_tabla2[0]))] for i in range(len(copie_tabla2))]
                block = False
                backClick = False
                startClicked = False
                solveClicked = False
                background = False
                startedPlaying = False
                drawMenu()
                QuitBtn = Btn(screenSize // 5, screenSize // 1.33, QuitImg, screenSize / 1000)  # Scale = screenSize / 1000
                quitFunctionality()  # Afisam butonul de quit
                startFunctionality()  # Afisam butonul de start
                startPlayingFunctionality()

            if block == False:  # Daca nu am castigat jocul, continuam sa cautam un event
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Verificam daca e apasat click stanga
                    position = pygame.mouse.get_pos()
                    i = int((position[1] - screenOffset) // n)
                    j = int((position[0] - screenOffset) // n)
                    if 9 > i >= 0 == copie_tabla2[i][j] and 0 <= j < 9:  # Daca pozitia din tabla nu e libera, nu putem pune nimic
                        pygame.draw.rect(screen, "red", (int((j * n) + offset - n // 8), int((i * n) + offset - n // 8), int(n // 1.6), int(n // 1.6)))
                        pygame.display.flip()
                        user_insert(position)

        if event.type == pygame.QUIT:
            exec = False
