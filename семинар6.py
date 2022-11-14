board = list(range(1,10))

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board [2+i*3], "|")
        print ("|"*13)
        
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим" + player_token+"?")
        try:
            player_answer = int(player_answer)
        except :
            print ("Некорректный ввод.")
            continue
        if player_answer >=1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ('Место занято')
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить")


def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False        

def main(bord):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("0")
        counter += 1 
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True 
                break
        if counter ==9:
            print ("Ничья")
            break
    draw_board(board)

main(board)         

#игра конфеты

from random import *
import os



def player_vs_player():
    candies_total = 120
    max_take = 28
    count = 0
    player_1 = input("Ваше имя?: ")
    player_2 = input("Имя соперника?: ")

    print('Первым ходить будет...')

    x = randint(1,2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'поздравляю {lucky} ты ходишь первым !')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'Сколько же вы возьмете {lucky} =  '))
            if step > candies_total or step > max_take:
                step = int(input(f'Можно взять не больше {max_take}, пробуй еще раз'))
            candies_total = candies_total - step
        if candies_total> 0:
            print(f'на кону еще {candies_total}')
            count = 1
        else:
            print('Конец игры')

        if count == 1:
            step = int(input(f'Сколько же вы возьмете {lucky} =  '))
            if step > candies_total or step > max_take:
                step = int(input(f'Можно взять не больше {max_take}, пробуй еще раз'))
            candies_total = candies_total - step
        if candies_total> 0:
            print(f'на кону еще {candies_total}')
            count = 0
        else:
            print(f'Конец игры')            
    if count == 1:
        print(f'{loser} победил') 
    if count == 0:
        print(f'{lucky} победил') 

player_vs_player   


import random 

def coding(text):
    if len(text) < 1:
        return ""
    count = 0
    el = text[0]
    result = ""
    for elem in text:
        if elem == el:
            count += 1
        else:
            result += str(count) + el
            count = 1
            el = elem
    else:
        result += str(count) + el
    return result


def decoding(text: str) -> str:
    if len(text) < 1:
        return""
    num = ""
    result = ""
    for elem in text:
        if elem.isdigit():
            num += elem
        else:
            num = ""
    return result


print("Кодирование")
print(coding("aaabbbcccbbb"))
print ("Декодирование")
print (decoding("3a3b3c3b"))                                           

