
import random
import os

print("동전확률 계산기")

def validate(a):

    if a.isdigit() == True:

        return(True)

    else:
        print('입력값이 숫자가 아닙니다')

        exit

coins = input('동전 개수를 입력하세요:')

if validate(coins) == True:

    coins = int(coins)

    repeat = input('반복 횟수를 입력하세요:')

    if validate(repeat) == True:

        repeat = int(repeat)

        def algorithm():

            counter = 0

            for i in range (0, repeat):

                list = []

                for i in range (0, coins):

                    list.append (random.randint(1,2))
                    
                    c = list.count(1)

                print(list)

                counter = (counter+c)

            psg = round((counter/(repeat*coins))*100,3)

            print("앞면이 나온 횟수:",counter)

            print("뒷면이 나온 횟수:",(repeat*coins)-counter)

            print("앞면이 나올 확률:",psg,"%")

        algorithm()

os.system("pause")
