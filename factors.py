class WTypes:
    def pistol(self):
        dmg_factor = 1
        speed_factor = 1
        accuracy_factor = 20
        ammo_factor = 10
        return dmg_factor, speed_factor, accuracy_factor, ammo_factor, 'pistol'

    def smg(self):
        dmg_factor = 1.4
        speed_factor = 1.5
        accuracy_factor = 10
        ammo_factor = 25
        return dmg_factor, speed_factor, accuracy_factor, ammo_factor, 'smg'

    def assault_rifle(self):
        dmg_factor = 0.9
        speed_factor = 1.3
        accuracy_factor = 30
        ammo_factor = 20
        return dmg_factor, speed_factor, accuracy_factor, ammo_factor, 'assault_rifle'

    def sniper_rifle(self):
        dmg_factor = 1.7
        speed_factor = 0.3
        accuracy_factor = 43
        ammo_factor = -5
        return dmg_factor, speed_factor, accuracy_factor, ammo_factor, 'sniper_rifle'

    def shotgun(self):
        dmg_factor = 4
        speed_factor = 0.2
        accuracy_factor = 5
        ammo_factor = -10
        return dmg_factor, speed_factor, accuracy_factor, ammo_factor, 'shotgun'


class NameDmgSpeedAccuracyAmmo:
    def __init__(self, element, level = "1"):

        import random
        self.element = element
        self.level = int(level[:2])
        types = ['pistol', 'smg', 'assault_rifle', 'sniper_rifle', 'shotgun']
        bonuses = ('dmg1', 'speed1', 'accuracy1', 'ammo1',
                   'dmg2', 'speed2', 'accuracy2', 'ammo2')
        sub_bonus = random.randint(0, 16)
        self.w_type = types[random.randint(0, 4)]
        if sub_bonus <= 7:
            self.bonus = bonuses[sub_bonus]
        else:
            self.bonus = 0
        w = WTypes()

        if self.w_type == 'pistol':
            self.p = w.pistol()

        if self.w_type == 'smg':
            self.p = w.smg()

        if self.w_type == 'assault_rifle':
            self.p = w.assault_rifle()

        if self.w_type == 'sniper_rifle':
            self.p = w.sniper_rifle()

        if self.w_type == 'shotgun':
            self.p = w.shotgun()
        self.element = element
        self.level = level

    def name(self):
        import random
        kind = random.randint(0, 1)

        def first_part():
            if kind == 1:
                n = open('adjective/3rd_namepm.txt', 'r', encoding='utf8')
                names = n.read().split(' ')
                name_number = random.randint(0, len(names) - 1)
                first_namep = names[name_number]
            else:
                n = open('adjective/3rd_namepfem.txt', 'r', encoding='utf8')
                names = n.read().split(' ')
                name_number = random.randint(0, len(names) - 1)
                first_namep = names[name_number]
            return first_namep

        if self.bonus != 0:
            def second_part():
                bon_names = {'dmg1': 'strength', 'speed1': 'speed', 'accuracy1': 'accuracy', 'ammo1': 'ammo',
                             'dmg2': 'strength', 'speed2': 'speed', 'accuracy2': 'accuracy', 'ammo2': 'ammo'}
                b = open('adjective/{}_namep.txt'.format(bon_names[self.bonus]), 'r', encoding='utf8')
                bonus_names = b.read().split(' ')
                bonus_namep = bonus_names[random.randint(0, len(bonus_names) - 1)]
                if kind == 0:
                    bonus_namep = bonus_namep[:-2] + 'ая' + ' '
                else:
                    bonus_namep = bonus_namep + ' '
                return bonus_namep
        if self.element != 'none':
            def third_part():
                e = open('adjective/2st_{}namep.txt'.format(self.element), 'r', encoding='utf8')
                elements = e.read().split(' ')
                element_namep = elements[random.randint(0, len(elements) - 1)]
                if kind == 0:
                    element_namep = element_namep[:-2] + 'ая' + ' '
                else:
                    element_namep = element_namep + ' '
                return element_namep
        if self.element != 'none':
            if self.bonus != 0:
                name = second_part().title() + third_part().title() + first_part().title()
            else:
                name = third_part().title() + first_part().title()
        else:
            if self.bonus != 0:
                name = second_part().title() + first_part().title()
            else:
                name = first_part().title()
        return name

    def dmg(self):
        import random
        self.level = int(self.level)
        dmg_factor = self.p[0]
        if self.p[-1] != 'shotgun':
            if self.bonus == 'dmg1':
                damage = ((self.level / 2) * (random.randint(100, 150) // 10) * dmg_factor) * 1.2

            elif self.bonus == 'dmg2':
                damage = ((self.level / 2) * (random.randint(100, 150) // 10) * dmg_factor) * 1.5

            else:
                damage = ((self.level / 2) * (random.randint(100, 150) // 10) * dmg_factor)
            return round(damage)
        else:
            dr = random.randint(2, 26)
            if self.bonus == 'dmg1':

                damage = (((self.level / 2) * (random.randint(100, 150) / 10) * dmg_factor) * 1.2) // dr
                damage = str(int(damage)) + 'x' + str(dr)

            elif self.bonus == 'dmg2':
                damage = (((self.level / 2) * (random.randint(100, 150) / 10) * dmg_factor) * 1.5) // dr
                damage = str(int(damage)) + 'x' + str(dr)
            else:
                damage = ((self.level / 2) * (random.randint(100, 150) / 10) * dmg_factor) // dr
                damage = str(int(damage)) + 'x' + str(dr)
        return damage

    def speed(self):
        import random
        speed_factor = self.p[1]
        if self.bonus == 'speed1':
            speed = round((((random.randint(5, 10) + 5) * speed_factor) / 10) * 1.1, 1)

        elif self.bonus == 'speed2':
            speed = round((((random.randint(5, 10) + 5) * speed_factor) / 10) * 1.2, 1)

        else:
            speed = round(((random.randint(5, 10) + 5) * speed_factor) / 10, 1)
        return speed

    def accuracy(self):
        import random
        accuracy_factor = self.p[2]
        if self.bonus == 'accuracy1':
            accuracy = round((random.randint(40, 50) + accuracy_factor) * 1.05)
        elif self.bonus == 'accuracy2':
            accuracy = round((random.randint(40, 50) + accuracy_factor) * 1.1)
        else:
            accuracy = random.randint(40, 50) + accuracy_factor
        return accuracy

    def ammo(self):
        import random
        ammo_factor = self.p[3]
        if self.bonus == 'ammo1':
            ammo = round((random.randint(11, 16) + ammo_factor) + 5)
        elif self.bonus == 'ammo2':
            ammo = round((random.randint(11, 16) + ammo_factor) + 10)
        else:
            ammo = random.randint(11, 16) + ammo_factor
        return ammo

    def element_damage(self):
        if self.element != 'none':
            import random
            level = self.level
            element_damage = round(level * random.randint(1, 5) * 1.5)
            return element_damage
        else:
            return 0

    def w_type(self):
        return self.w_type

    def Bonus(self):
        return self.bonus
