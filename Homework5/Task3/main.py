# Создайте программу для игры в "Крестики-нолики".


fields = list(range(9))

def draw_board(board):
    print("\n     |     |")
    print(f"  {fields[0]}  |  {fields[1]}  |  {fields[2]}")
    print('_____|_____|_____')
    print("     |     |")
    print(f"  {fields[3]}  |  {fields[4]}  |  {fields[5]}")
    print('_____|_____|_____')
    print("     |     |")
    print(f"  {fields[6]}  |  {fields[7]}  |  {fields[8]}")
    print("     |     |")

def take_input(symbol):

   while True:
      field = int(input(f"Выберите место для {symbol}\n"))
      if field >= 0 and field <= 8:
         if str(fields[field]) != "O" and str(fields[field]) != "X":
            fields[field] = symbol
            break
         else:
            print("Эта клетка занята")
      else:
        print("Введите число от 0 до 8.")

def check_win(board):
   win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
   for i in win_coord:
       if board[i[0]] == board[i[1]] == board[i[2]]:
          return True
   return False


counter = 0

while True:
    draw_board(fields)
    if counter % 2 == 0:
        take_input("X")
    else:
        take_input("O")
    counter += 1

    if check_win(fields):
        draw_board(fields)
        print("Победа!")
        break
    if counter == 9:
        draw_board(fields)
        print("Ничья!")
        break