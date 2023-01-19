# # №2
# # Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота 
# с интеллектом

print('\033[0m Игра Крестики-нолики ')
firstplayer = input('Введите имя первого игрока: ')
print(f' {firstplayer}, Вы играете за Х ')
secondplayer = input('Введите имя второго игрока: ')
print(f'{secondplayer}, Вы играете за O ')

game_table = list(range(1,10))

def game_board(game_table):
   print('=' * 17)
   for i in range(3):
      print('||', game_table[0+i*3], '||', game_table[1+i*3], '||', game_table[2+i*3], '||')
      print('=' * 17)

def first_player_choice(playerX):  
   valid = False
   while not valid:
      first_player_choice = input('Выберите клетку для ' + playerX + ' ') 
      try:
         first_player_choice = int(first_player_choice)  
      except:
         print('Введите число в диапозоне от 1 до 9')
         continue
      if first_player_choice >= 1 and first_player_choice <= 9:
         if(str(game_table[first_player_choice-1]) not in 'XO'):
            game_table[first_player_choice-1] = playerX
            valid = True
         else:
            print('Вы не можете ничего поставить в эту ячейку, так как она уже занята')
      else:
        print('Введите число в диапозоне от 1 до 9')

def second_player_choice(playerO):  
   valid = False
   while not valid:
      second_player_choice = input('Выберите клетку для ' + playerO + ' ') 
      try:
         second_player_choice = int(second_player_choice) 
      except:
         print('Введите число в диапозоне от 1 до 9')
         continue
      if second_player_choice >= 1 and second_player_choice <= 9:
         if(str(game_table[second_player_choice-1]) not in 'XO'):
            game_table[second_player_choice-1] = playerO
            valid = True
         else:
            print('Вы не можете ничего поставить в эту ячейку, так как она уже занята')
      else:
        print('Введите число в диапозоне от 1 до 9')


def who_win(game_table):
   win_coord = ((0,1,2), (0,3,6), (6,7,8), (2,5,8), (2,4,6), (0,4,8), (3,4,5), (1,4,7))
   for each in win_coord:
       if game_table[each[0]] == game_table[each[1]] == game_table[each[2]]:
          return game_table[each[0]]
   return False

def game(game_table):
    counter = 0
    win = False
    while not win:
        game_board(game_table)
        if counter % 2 == 0:
           first_player_choice('X')
        else:
           second_player_choice('O')
        counter += 1
        if counter > 4:
           tmp = who_win(game_table)
           if tmp:
              print('\033[34m ~' * 7,'\033[31m Победа!', '\033[34m ~' * 7) 
              win = True
              break
        if counter == 9:
            print('\033[33m Ничья')
            break
game(game_table)
game_board(game_table)


