import digit, in_num, log

def button_click():
    print('Введите "0" если хотите продолжить')
    print('Введите "1" если хотите закончить')
    flag = int(input())
    while flag == 0:
        primer = digit.parse()
        result = digit.calculate(primer)
        in_num.view_data(result)
        log.loger(result)
        print('Введите "0" если хотите продолжить')
        print('Введите "1" если хотите закончить')
        flag = int(input())
    print("программа завершилась")    

    
    