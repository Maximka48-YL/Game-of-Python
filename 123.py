import os
import sys

import pygame

LEVEL = ["M                                                        K",
         "",
         "",
         "",
         "             -----                                      --",
         "",
         "",
         "",
         "             -----                                      --",
         "",
         "",
         "",
         "             -----                                      --",
         "",
         "----                                                      ",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "                   ---------         --------------",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "                                                 ---------",
         "          -----",
         "                                   M",
         "",
         "                                 -----",
         "",
         "",
         "",
         "",
         "                           ------",
         "",
         "                                      --------------",
         "",

         "",
         "           ---------",
         "                             ---------",
         "",
         "",
         "              P",
         "                                              ------",
         "",
         "                             M",
         "           -------         ------        --    -----------",
         "",
         "",
         "                                  ----",
         "+"]
LEVEL2 = ["",
          "              P                                  K",
          "                                              ------",
          "",
          "                             M",
          "           -------         ------        --    -----------",
          "",
          "",
          "                                  ----",
          "+"]
LEVEL3 = ["",
          "                                                K",
          "                                              ------",
          "",
          "                                                     M",
          "           -------         --------    -----------",
          "",
          "                                    P",
          "                                  ----",
          "+"]
LEVEL4 = ["M                                                        K",
          " ---          -",
          "",
          "",
          "               -                                     --",
          "",
          "               -               -               -               -",
          "               -",
          "               -                                      --",
          "               -",
          "               -",
          "               -",
          "               -                                      --",
          "",
          "----                                                      ",
          "",
          "",
          "",
          "                ---------------                        ----------",
          "",
          "",
          "",
          "                                       -",
          "                                       -",
          "                                       -",
          "                                       -             M",
          "                                       -",
          "                                       -",
          "                                       -",
          "                                       -",
          "",
          "",
          "                                                 ---------",
          "          -------------------",
          "                                   M",
          "                                                                          M",
          "                                                  ---------------                    --------",
          "",
          "                             ------------------",
          "",
          "",
          "                 ------",
          "",
          "                    ------------------                  --------------",
          "",
          "",
          "           ---------",
          "                                        ---------",
          "",
          "",
          "                P",
          "                                                    ------",
          "",
          "                                                M",
          "           ------------           -----------                 ----",
          "",
          "+"]
LEVEL5 = [" M"
          "                                                        ",
          "  ---------------------------------",
          "",
          "",
          "                           ---------------                 --",
          "",
          "               -                      ",
          "                    -",
          "                         -                                      --",
          "                -",
          "                          -",
          "                      -",
          "               -                                      -",
          "",
          "----                                                      ",
          "",
          "",
          "                                                              K",
          "                ---------------                        ----------",
          "",
          "",
          "",
          "                                 -",
          "                           -",
          "                                      -",
          "                                           -             M",
          "                                 -",
          "                                        -",
          "                         -",
          "                                            -",
          "",
          "",
          "                                                 ---------",
          "          -------------------",
          "                  M",
          "                                                      M",
          "                                                  ---------------                    --------",
          "",
          "                             ----           -----              ---------",
          "",
          "",
          "                 ------",
          "",
          "                    -------     --- ----   ----                  --------------",
          "",
          "",
          "           ---------",
          "                                        ---------",
          "",
          "",
          "                P",
          "                                                    ---        ---",
          "",
          "                                                                M",
          "        -    -----------           -----------                 ----",
          "",
          "+"]
HEALTH = 3
FPS = 60
pygame.init()
size = WIDTH, HEIGHT = 1280, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
start_screens_buttons = pygame.sprite.Group()
plats = pygame.sprite.Group()
players = pygame.sprite.GroupSingle()
n = pygame.display.set_mode(size)
end = pygame.sprite.Group()
money = pygame.sprite.Group()
again = pygame.sprite.Group()
hearts = pygame.sprite.Group()
LVL_N = 1
EXIT = False
GRAVITY = 5
ON_GROUND = False
DEATH_ZONE = 0
X = 0
Y = 0
SCORE = 0
NEW = False
C = 0
H = 0
K = 0
J = 0
F = 0
FLIP = 0


def terminate():
    pygame.quit()
    sys.exit()


class Again(pygame.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__(again)
        self.image = sheet
        self.rect = pygame.Rect(x, y, sheet.get_width(), sheet.get_height())


class Start(pygame.sprite.Sprite):
    def __init__(self, image, number, coords, width, height):
        super().__init__(start_screens_buttons)
        self.image = image
        self.rect = self.image.get_rect().move(coords[0], coords[1])
        self.button_number = number
        self.width = width
        self.height = height

    def update(self, *args):
        if self.rect.x <= args[0][0] <= self.rect.x + self.width:
            if self.rect.y <= args[0][1] <= self.rect.y + self.height:
                if self.button_number == 1:
                    global EXIT
                    EXIT = True
                elif self.button_number == 3:
                    terminate()


class Platform(pygame.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__(plats)
        self.image = sheet
        self.rect = pygame.Rect(x, y, 30, 30)


class Monetka(pygame.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__(money)
        self.image = sheet
        self.rect = pygame.Rect(x, y, 25, 30)


def update(target, group):
    global DEATH_ZONE
    global C
    global H
    if target.rect.x >= WIDTH:
        for obj in group:
            obj.rect.x -= WIDTH
        for obj in money:
            obj.rect.x -= WIDTH
        for obj in end:
            obj.rect.x -= WIDTH
        target.rect.x = 0
    if target.rect.y >= HEIGHT:
        DEATH_ZONE -= HEIGHT
        for obj in group:
            obj.rect.y -= HEIGHT
        for obj in money:
            obj.rect.y -= HEIGHT
        for obj in end:
            obj.rect.y -= HEIGHT
        target.rect.y = 0
    if target.rect.x < 0:
        for obj in group:
            obj.rect.x += WIDTH
        for obj in money:
            obj.rect.x += WIDTH
        for obj in end:
            obj.rect.x += WIDTH
        target.rect.x = WIDTH
    if target.rect.y < 0:
        DEATH_ZONE += HEIGHT
        for obj in group:
            obj.rect.y += HEIGHT
        for obj in money:
            obj.rect.y += HEIGHT
        for obj in end:
            obj.rect.y += HEIGHT
        target.rect.y = HEIGHT
    if H % 5 == 0:
        for i in end:
            i.image = hole[C % 3]
            C += 1
            if C > 50:
                C = 0
    H += 1
    if H > 100:
        H = 0
    for lu in hearts:
        if lu.number > HEALTH:
            lu.rect.y -= 51
        else:
            if lu.rect.y < 0:
                lu.rect.y = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, sheet, x, y, width, height):
        super().__init__()
        self.start_x = x
        self.start_y = y
        self.velosity_x = 10
        self.velosity_y = 0.2
        self.image = sheet[0]
        self.rect = pygame.Rect(x, y, width, height)

    def update(self, *args):
        global SCORE
        global HEALTH
        global K
        global J
        global F
        global FLIP
        if args[0][1]:
            self.rect.x += self.velosity_x
        elif args[0][0]:
            self.rect.x -= self.velosity_x
        elif ON_GROUND and args[1]:
            self.velosity_y = 10
        if not ON_GROUND:
            self.rect.y += GRAVITY
            if self.velosity_y > 0.5:
                self.velosity_y -= self.velosity_y / GRAVITY ** 3
            if self.velosity_y < 0.5 and self.velosity_y != 0 and not ON_GROUND:
                self.velosity_y = -(self.velosity_y + self.velosity_y / GRAVITY ** 3)
        if ON_GROUND and not args[1]:
            self.velosity_y = 0
        self.rect.y -= self.velosity_y
        if self.rect.y > DEATH_ZONE:
            plats.empty()
            create_level(plats, args[2])
            self.rect.x, self.rect.y = self.start_x, self.start_y
            HEALTH -= 1
            prov()
        a = pygame.sprite.spritecollideany(self, money)
        if a:
            money.remove(a)
            a.kill()
            SCORE += 1
        if args[0][0] or args[0][1]:
            if J % 5 == 0:
                if args[0][0]:
                    self.image = pygame.transform.flip(holst[2 + K % 2], -1, 0)
                    FLIP = 1
                else:
                    self.image = pygame.transform.flip(holst[2 + K % 2], 0, 0)
                    FLIP = 0
                K += 1
                if K >= 50:
                    K = 0
            J += 1
            if J >= 100:
                J = 0
        if not args[0][0] and not args[0][1]:
            if J % 5 == 0:
                if FLIP:
                    self.image = pygame.transform.flip(holst[F % 2], -1, 0)
                else:
                    self.image = pygame.transform.flip(holst[F % 2], 0, 0)
                F += 1
                if F >= 50:
                    F = 0
            J += 1
            if J >= 100:
                J = 0


def start_screen():
    fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    play = pygame.transform.scale(load_image('play.png'), (400, 125))
    quit = pygame.transform.scale(load_image('quit.png'), (400, 125))
    start_screens_buttons.add(Start(play, 1, (WIDTH // 3, HEIGHT // 5), 400, 125),
                              Start(quit, 3, (WIDTH // 3, HEIGHT // 1.5), 400, 125))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONUP:
                start_screens_buttons.update(pygame.mouse.get_pos())
        start_screens_buttons.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
        if EXIT:
            break


class Heart(pygame.sprite.Sprite):
    def __init__(self, sheet, number, x, y):
        super().__init__(hearts)
        self.image = sheet
        self.number = number + 1
        self.rect = pygame.Rect(x, y, 50, 50)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class End(pygame.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__(end)
        self.image = sheet[0]
        self.rect = pygame.Rect(x, y, 30, 30)


platf = pygame.transform.scale(load_image('platf.png'), (30, 30))
mon = pygame.transform.scale(load_image('mon.png'), (25, 30))
hole = [pygame.transform.scale(load_image('hole_1.png'), (50, 50)),
        pygame.transform.scale(load_image('hole_2.png'), (50, 50)),
        pygame.transform.scale(load_image('hole_3.png'), (50, 50))]


def create_level(group, lvl):
    global DEATH_ZONE
    global ON_GROUND
    global X
    global Y
    end.empty()
    money.empty()
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            if lvl[i][j] == '-':
                group.add(Platform(platf, j * 30, i * 30))
            elif lvl[i][j] == '+':
                DEATH_ZONE = i * 30
            elif lvl[i][j] == 'P':
                X = j * 30
                Y = i * 30
            elif lvl[i][j] == 'K':
                end.add(End(hole, j * 30, i * 30))
            elif lvl[i][j] == 'M':
                money.add(Monetka(mon, j * 30, i * 30))


def prov():
    if player.rect.y > HEIGHT:
        y = player.rect.y // HEIGHT
        player.rect.y = player.rect.y % HEIGHT
        for i in range(y):
            for obj in plats:
                obj.rect.y -= HEIGHT
            for obj in money:
                obj.rect.y -= HEIGHT
            for obj in end:
                obj.rect.y -= HEIGHT
    if player.rect.y < 0:
        y = (HEIGHT - player.rect.y) // HEIGHT
        player.rect.y = (HEIGHT - player.rect.y) % HEIGHT
        for i in range(y):
            for obj in plats:
                obj.rect.y += HEIGHT
            for obj in money:
                obj.rect.y -= HEIGHT
            for obj in end:
                obj.rect.y -= HEIGHT


pygame.display.set_icon(load_image('icon.png'))
pygame.display.set_caption('Game of Python')
start_screen()
hea = pygame.transform.scale(load_image('heart.png'), (50, 50))
for i in range(3):
    hearts.add(Heart(hea, i, i * 50, 0))
g_o = pygame.transform.scale(load_image('game_over.png'), (WIDTH, HEIGHT))
ag = pygame.transform.scale(load_image('ag.png'), (375, 100))
again.add(Again(ag, WIDTH // 3, HEIGHT // 2))
holst = [pygame.transform.scale(load_image('player_1.png'), (50, 75)),
         pygame.transform.scale(load_image('player_2.png'), (50, 75)),
         pygame.transform.scale(load_image('player_3.png'), (50, 75)),
         pygame.transform.scale(load_image('player_4.png'), (50, 75))]


def pusk(lbl):
    global ON_GROUND
    global DEATH_ZONE
    global LVL_N
    global player
    players.empty()
    plats.empty()
    money.empty()
    end.empty()
    create_level(plats, lbl)
    ON_GROUND = False
    player = Player(holst, X, Y, 50, 75)
    players.add(player)
    prov()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        if pygame.key.get_pressed()[pygame.K_d]:
            players.update((False, True), False, [])
        if pygame.key.get_pressed()[pygame.K_a]:
            players.update((True, False), False, [])
        if pygame.key.get_pressed()[pygame.K_w]:
            players.update((False, False), True, [])
        if pygame.sprite.spritecollideany(player, plats):
            ON_GROUND = True
        else:
            ON_GROUND = False
        players.update((False, False), False, lbl)
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))
        update(player, plats)
        plats.draw(screen)
        players.draw(screen)
        money.draw(screen)
        end.draw(screen)
        b = pygame.sprite.spritecollideany(player, end)
        if b:
            break
        if HEALTH < 1:
            screen.fill((0, 0, 0))
            screen.blit(g_o, (0, 0))
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    if event.type == pygame.MOUSEBUTTONUP:
                        for i in again:
                            if i.rect.x <= event.pos[0] <= i.rect.x + i.rect.width:
                                if i.rect.y <= event.pos[1] <= i.rect.y + i.rect.height:
                                    LVL_N = 0
                                    return
                again.draw(screen)
                pygame.display.flip()
                clock.tick(FPS)
        hearts.draw(screen)
        pygame.display.update()
        clock.tick(FPS)


def proverka(s=0):
    global LVL_N
    global HEALTH
    global SCORE
    if LVL_N == 0:
        LVL_N = 1
        SCORE = 0
        HEALTH = 3
        return 1
    if LVL_N == 1 and s == 1:
        return 0
    elif LVL_N == 1:
        return None


fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
screen.blit(fon, (0, 0))
while True:
    pusk(LEVEL)
    if proverka() == 1:
        continue
    pusk(LEVEL2)
    if proverka() == 1:
        continue
    pusk(LEVEL3)
    if proverka() == 1:
        continue
    pusk(LEVEL4)
    if proverka() == 1:
        continue
    pusk(LEVEL5)
    if proverka() == 1:
        continue
    if proverka(1) == 0:
        break
fon_win = pygame.transform.scale(load_image('win.png'), (WIDTH, HEIGHT))
font = pygame.font.Font(None, 125)
text = font.render(str(SCORE), 1, (18, 211, 91))
screen.fill((0, 0, 0))
screen.blit(fon_win, (0, 0))
screen.blit(text, (675, 450))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
pygame.quit()
