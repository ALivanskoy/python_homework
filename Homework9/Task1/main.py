# Создайте программу для игры в "Крестики-нолики" при помощи виртуального окружения и PIP
import pygame as pg
import sys

def check_win (sign_list, sign):
    zero = 0
    for row in sign_list:
        zero+= row.count(0)
        if row.count(sign) == 3:
            return sign
    for column in range(3):
        if sign_list[0][column] == sign and sign_list[1][column] == sign and sign_list[2][column] == sign:
            return sign
    if sign_list[0][0] == sign and sign_list[1][1] == sign and sign_list[2][2] == sign:
        return sign
    if sign_list[0][2] == sign and sign_list[1][1] == sign and sign_list[2][0] == sign:
        return sign
    if zero == 0:
        return "Draw"

    return False

pg.init()
size_block = 100
margin = 15

window_size = size_block*3 + margin*4
window = (window_size, window_size)

screen = pg.display.set_mode(window)
pg.display.set_caption("Крестики-нолики")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
field = [[0]*3 for i in range(3)]
turn = 0
game_over = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)
        elif event.type == pg.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pg.mouse.get_pos()
            column = x_mouse // (size_block+margin)
            row = y_mouse // (size_block+margin)
            if field[row][column] == 0:
                if turn%2 == 0:
                    field[row][column] = 'x'
                else:
                    field[row][column] = 'o'
                turn+=1
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            game_over = False
            field = [[0] * 3 for i in range(3)]
            turn = 0

    if not game_over:
        for row in range(3):
            for column in range (3):
                if field[row][column] == 'x':
                    color = red
                elif field[row][column] == 'o':
                    color = green
                else:
                    color = white
                x = column*size_block + (column+1)*margin
                y = row*size_block + (row+1)*margin
                pg.draw.rect(screen, color, (x,y,size_block,size_block))

                if field[row][column] == 'x':
                    pg.draw.line(screen, white, (x+10, y+10),(x+size_block-10, y+size_block-10), 10)
                    pg.draw.line(screen, white, (x + size_block - 10, y + 10), (x+10, y + size_block - 10), 10)
                elif field[row][column] == 'o':
                    pg.draw.circle(screen, white, (x+size_block/2, y+size_block/2), size_block/2-10, 10)
    if (turn-1)%2 == 0:
        gameover = check_win(field, 'x')
    else:
        gameover = check_win(field, 'o')

    if gameover:
        screen.fill(black)
        font = pg.font.SysFont('stxingkai', 80)
        text1 = font.render(gameover, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])

    pg.display.update()



