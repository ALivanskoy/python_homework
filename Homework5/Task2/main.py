# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import *

def Taking_candy (can):
    # Функция принимает оставшееся количество конфет на вход и возвращает количество конфет, после взятия игроком
    # Если игрок жульничает, то берётся рандомное кол-во конфет
    taken_candy = int(input("Сколько конфет взять?\n"))
    if taken_candy <= can and taken_candy < 29 and taken_candy > 0:
        can -= taken_candy
    else:
        if can > 27:
            taken_candy = randint(0,27)
        else:
            taken_candy = randint(0, can)
        print(f"Нет, так дело не пойдёт, я возьму конфеты за тебя, скажем-с {taken_candy} штук")
        can -= taken_candy
    return can

def Smart_taking_candy (can):
    # Функция обдумывания хода ботом
    taken_candy = can % 29
    print(f"Бот немного думает и берёт {taken_candy} штук")
    can -= taken_candy
    return can


print("\nНа столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.")
print("Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.")
print("Все конфеты оппонента достаются сделавшему последний ход.\n")

gamemode = input("Второй игрок будет компьютер(com) или человек(hum)?\n")
autopilot = None
if gamemode == 'com':
    autopilot = True
elif gamemode == 'hum':
    autopilot = False
else:
    print("\nБудем считать, что это было что-то типа 'com'")
    autopilot = True


candys = 2021

player_one_turn = bool (randint(0, 1))

if player_one_turn:
    print("\nПо жеребьёвке первым ходит первый игрок")
else:
    print("\nПо жеребьёвке первым ходит второй игрок")

while candys > 0:
    print(f"\nНа столе осталось {candys} конфет\n")
    if player_one_turn:
        print("Ход первого игрока")
        candys = Taking_candy(candys)
        player_one_turn = False
    else:
        print("Ход второго игрока")
        if autopilot:
            candys = Smart_taking_candy(candys)
        else:
            candys = Taking_candy(candys)
        player_one_turn = True

if player_one_turn:
    print("Второй заслуженно победил")
else:
    print("Первый заслуженно победил")




