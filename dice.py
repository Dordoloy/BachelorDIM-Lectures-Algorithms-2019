import random

"""
    Code moche non fini à réfactoriser
"""
def shuffle():
    lauch = 0
    lauch2 = 0
    res = 0
    diff = 0
    diff2 = 0
    res2 = 0
    interact = 1
    party = True
    keep = 1
    while(party):
        while(interact == 1 and lauch != 1):
            keep = 1
            lauch = random.randrange(1,6)
            diff += lauch
            if(lauch == 1):
                res -= diff - 1
                diff = 0
            else:
                res += lauch
            interact = input("Voulez vous continuer ? (1 to continue)")
            print('res = ',res)
            lauch2 = 0
            if(res >= 100):
                interact = 2
                party = False
                print('J1 winner')
        while(lauch2 != 1 and keep == 1):
            lauch2 = random.randrange(1,6)
            diff2 += lauch2
            keep = random.randrange(0,1)
            if(lauch2 == 1):
                res2 -= diff2 - 1
                diff2 = 0
            else:
                res2 += lauch2
            print('res2 = ',res2)
            lauch = 0
            interact = 1
            if (res2 >= 100):
                interact = 2
                lauch2 = 0
                party = False
                print('Bot winner')

    return res

print('dice game : = {0}'.format(shuffle()))