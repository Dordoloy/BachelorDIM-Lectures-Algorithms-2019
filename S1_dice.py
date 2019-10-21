import random

"""
    Code moche non fini à réfactoriser
"""
def shuffle():
    launch = 0
    launch2 = 0
    res = 0
    diff = 0
    diff2 = 0
    res2 = 0
    interact = 'y'
    game = True
    keep = 1
    while(game):
        while(interact == 'y' and launch != 1):
            diff2=0
            keep = 1
            launch = random.randrange(1,7)
            diff += launch
            interact = input("Voulez vous continuer ? (y or n)")
            if(interact == 'q'):
                game = False
            if(interact != 'y'):
                res = res
            elif(launch == 1):
                res -= diff - 1
                diff = 0
                print('dice : ',launch)
            else:
                res += launch
                print('dice : ',launch)
            print('J1 = ',res)
            launch2 = 0
            if(res >= 100):
                interact = 2
                game = False
                keep = 0
                print('------J1 WIN------')            

        while(launch2 != 1 and keep != 0):
            diff = 0
            launch2 = random.randrange(1,7)
            diff2 += launch2
            keep = random.randrange(0,3)
            if(launch2 == 1):
                res2 -= diff2 - 1
                diff2 = 0
            else:
                res2 += launch2
            print('BOT = ',res2)
            launch = 0
            interact = 'y'
            if (res2 >= 100):
                interact = 2
                launch2 = 0
                game = False
                interact='n'
                print('------BOT WIN------')


shuffle()