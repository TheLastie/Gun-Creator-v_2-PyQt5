import random
from PIL import *
def g_characteristic(st, level, type):
    morf = random.randint(0, 1)
    if morf == 1:

        n = open('3rd_namepm.txt', encoding='UTF8')
        n = n.read()
        n = n.split(' ')
        oname = n[random.randint(0, len(n)-1)]
    else:
        n = open('3rd_namepfem.txt', encoding='UTF8')
        n = n.read()
        n = n.split(' ')
        oname = n[random.randint(0, len(n)-1)]
    firstnamep = ''


    fr = open('1st_namep.txt', encoding='UTF8')
    fr = fr.read()
    fr = fr.split(' ')
    o = random.randint(0, int(len(fr) / 0.9))
    if morf == 1:
        if o < len(fr):
            first_namep = fr[o]
        else:
            first_namep = ''
    elif morf == 0:
        if o < len(fr):
            first_namep = fr[o]
            first_namep = first_namep[:-2] + 'ая'
        else:
            first_namep = ''

    s = ['', 'fire', 'cold', 'elctr', 'rad', 'tox']
    if st != 0:
        stihiya = open('2st_' + s[st] + 'namep.txt', encoding='UTF8')
        stihiya = stihiya.read()
        stihiya = stihiya.split(' ')
        p = random.randint(0, len(stihiya) - 1)
        stihiya = stihiya[p]
        if morf == 0:
            stihiya = stihiya[:-2] + 'ая'
        name = first_namep + ' ' + stihiya + ' ' + oname
    else:
        name = first_namep + ' ' + oname
    dmg = int((level*random.randint(100, 150)/10)*type)
    if type == 3:
        i = random.randint(1, 15)
        dmg = str(int(((level*random.randint(100, 150)/10)*type) / i)) + 'x' + str(i)
    speed = round(((random.randint(5, 20)+5) / type)/10, 1)
    ammo = int(random.randint(5, 20) / type)
    return name, dmg, speed, ammo

