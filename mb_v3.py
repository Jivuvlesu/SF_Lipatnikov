import os
from random import randrange

class Pole:
    def __init__(self):
        self.pl = [['-' for _ in range(6)] for _ in range(6)]
        self.ai = [['-' for _ in range(6)] for _ in range(6)]

    def get_pole(self, pl_ai):
        if pl_ai == 'Player':
            return self.pl
        if pl_ai == 'AI':
            return self.ai

    def print_pole(self, pl_ai):
        pole = self.get_pole(pl_ai)
        print('---', pl_ai, '---')
        print('  1 2 3 4 5 6')
        num = 0
        for i in pole:
            num += 1
            print(num, end = ' ')
            for j in i:
                print(j, end = ' ')
            print()
        print()

    def add_ship(self, ship, pl_ai):
        pole = self.get_pole(pl_ai)
        if ship.name == 1:
            pole[ship.xy1[0]][ship.xy1[1]] = ship
        if ship.name == 2:
            pole[ship.xy1[0]][ship.xy1[1]] = ship
            pole[ship.xy2[0]][ship.xy2[1]] = ship
        if ship.name == 3:
            pole[ship.xy1[0]][ship.xy1[1]] = ship
            if (ship.xy1[0] == ship.xy2[0]) and (abs(ship.xy1[1] - ship.xy2[1]) == (ship.xy1[1] - ship.xy2[1])):
                pole[ship.xy1[0]][ship.xy1[1] - 1] = ship
            if (ship.xy1[0] == ship.xy2[0]) and (abs(ship.xy1[1] - ship.xy2[1]) != (ship.xy1[1] - ship.xy2[1])):
                pole[ship.xy1[0]][ship.xy1[1] + 1] = ship
            if ship.xy1[1] == ship.xy2[1]:
                pole[ship.xy1[0]+1][ship.xy1[1]] = ship
            pole[ship.xy2[0]][ship.xy2[1]] = ship

    def input_ships(self, pl_ai):

        if pl_ai == 'Player':
            for class_ship in pl_.player_ships:
                prov = True
                while prov:
                    self.print_pole(pl_ai)
                    x3y3 = [0, 0]
                    print('Введите координаты', class_ship, '-х палубного корабля.')
                    try_ = True
                    while try_:
                        try:
                            if class_ship > 1:
                                x1y1 = list(map(int, input('Начало корабля (X Y)').split(' ')))
                                x2y2 = list(map(int, input('Конец корабля  (X Y)').split(' ')))
                            else:
                                x1y1 = list(map(int, input('Координаты корабля (X Y)').split(' ')))
                                x2y2 = list.copy(x1y1)
                            try_ = False
                        except:
                            print('Ввод не корректный. Попробуйте снова.')
                            try_ = True
                    if (1 <= x1y1[0] <= 6) and (1 <= x1y1[1] <= 6) and (1 <= x2y2[0] <= 6) and (1 <= x2y2[1] <= 6):
                        if (x1y1[0] == x2y2[0]) and (abs(x1y1[1] - x2y2[1]) == (class_ship - 1)):
                            if (class_ship == 3) and (abs(x1y1[1] - x2y2[1]) == x1y1[1] - x2y2[1]):
                                x3y3[1] = x1y1[1] - 1
                            elif (class_ship == 3) and (abs(x1y1[1] - x2y2[1]) != x1y1[1] - x2y2[1]):
                                x3y3[1] = x1y1[1] + 1
                            good = True
                        elif (x1y1[1] == x2y2[1]) and (abs(x1y1[0] - x2y2[0]) == (class_ship - 1)):
                            if (class_ship == 3) and (abs(x1y1[0] - x2y2[0]) == x1y1[0] - x2y2[0]):
                                x3y3[0] = x1y1[0] - 1
                            elif (class_ship == 3) and (abs(x1y1[0] - x2y2[0]) != x1y1[0] - x2y2[0]):
                                x3y3[0] = x1y1[0] + 1
                            good = True
                        else:
                            good = False
                            print('Длина корабля не верна')
                        x1y1[0] -= 1
                        x1y1[1] -= 1
                        x2y2[0] -= 1
                        x2y2[1] -= 1
                        x3y3[0] -= 1
                        x3y3[1] -= 1
                        for i in -1, 0, 1:
                            for j in -1, 0, 1:
                                if (0 <= x1y1[0]+i <= 5) and (0 <= x2y2[1]+j <= 5) \
                                        and (self.get_pole(pl_ai)[x1y1[0]+i][x1y1[1]+j] != '-') and good:
                                    print('Соседние ячейки должны быть свободными')
                                    good = False
                        for i in -1, 0, 1:
                            for j in -1, 0, 1:
                                if (0 <= x2y2[0]+i <= 5) and (0 <= x2y2[1]+j <= 5) \
                                        and (self.get_pole(pl_ai)[x2y2[0]+i][x2y2[1]+j] != '-') and good:
                                    print('Соседние ячейки должны быть свободными')
                                    good = False
                        if (self.get_pole(pl_ai)[x1y1[0]][x1y1[1]] == '-') \
                                and (self.get_pole(pl_ai)[x2y2[0]][x2y2[1]] == '-') \
                                and (self.get_pole(pl_ai)[x3y3[0]][x3y3[1]] == '-') and good:
                            ship = Ship(class_ship, x1y1, x2y2, pl_ai)
                            self.add_ship(ship, pl_ai)
                            self.print_pole(pl_ai)
                            prov = False
                        elif (self.get_pole(pl_ai)[x1y1[0]][x1y1[1]] != '-') \
                                and (self.get_pole(pl_ai)[x2y2[0]][x2y2[1]] != '-') \
                                and (self.get_pole(pl_ai)[x3y3[0]][x3y3[1]] != '-'):
                            print('Клетка поля занята')
                    else:
                        print('Указанные координаты вне поля боя')

        if pl_ai == 'AI':
            count = 100
            all_ships = len(ai_.player_ships)
            while count > 0 and all_ships != 0:
                pole = Pole()
                all_ships = len(ai_.player_ships)
                for class_ship in ai_.player_ships:
                    count2 = 30
                    prov = True
                    while prov and count2 > 0:
                        count2 -= 1
                        xy1 = [0, 0]
                        xy2 = list.copy(xy1)
                        xy3 = list.copy(xy1)
                        xy1[0] = randrange(0, 6, 1)
                        xy1[1] = randrange(0, 6, 1)
                        hv = randrange(0, 2, 1)
                        if class_ship == 3 and hv == 0:
                            xy2[0] = xy1[0] + 1
                            xy2[1] = xy1[1]
                            xy3[0] = xy1[0] - 1
                            xy3[1] = xy1[1]
                        elif class_ship == 3 and hv == 1:
                            xy2[1] = xy1[1] + 1
                            xy2[0] = xy1[0]
                            xy3[1] = xy1[1] - 1
                            xy3[0] = xy1[0]
                        elif class_ship == 2 and hv == 0:
                            xy2[0] = xy1[0] + 1
                            xy2[1] = xy1[1]
                            xy3 = list.copy(xy1)
                        elif class_ship == 2 and hv == 1:
                            xy2[1] = xy1[1] + 1
                            xy2[0] = xy1[0]
                            xy3 = list.copy(xy1)
                        elif class_ship == 1:
                            xy2 = list.copy(xy1)
                            xy3 = list.copy(xy1)
                        #print(xy3, xy1, xy2, hv)
                        if (0 <= xy1[0] <= 5) and (0 <= xy1[1] <= 5) \
                            and (0 <= xy2[0] <= 5) and (0 <= xy2[1] <= 5) \
                            and (0 <= xy3[0] <= 5) and (0 <= xy3[1] <= 5):
                            good = True
                        else:
                            xy2 = list.copy(xy1)
                            xy3 = list.copy(xy1)
                            good = False

                        for i in -1, 0, 1:
                             for j in -1, 0, 1:
                                 if (0 <= xy3[0]+i <= 5) and (0 <= xy3[1]+j <= 5) \
                                        and (pole.get_pole(pl_ai)[xy3[0]+i][xy3[1]+j] != '-') and good:
                                    #print('Соседние ячейки должны быть свободными')
                                    good = False
                        for i in -1, 0, 1:
                            for j in -1, 0, 1:
                                if (0 <= xy2[0]+i <= 5) and (0 <= xy2[1]+j <= 5) \
                                        and (pole.get_pole(pl_ai)[xy2[0]+i][xy2[1]+j] != '-') and good:
                                    #print('Соседние ячейки должны быть свободными')
                                    good = False

                        if (pole.get_pole(pl_ai)[xy1[0]][xy1[1]] == '-') \
                                and (pole.get_pole(pl_ai)[xy2[0]][xy2[1]] == '-') \
                                and (pole.get_pole(pl_ai)[xy3[0]][xy3[1]] == '-') and good:
                            ship = Ship(class_ship, xy3, xy2, pl_ai)
                            pole.add_ship(ship, pl_ai)
                            all_ships -= 1
                            if all_ships == 0:
                                self.ai = pole.get_pole(pl_ai)
                                self.print_pole(pl_ai)
                            #print('Добавлен', class_ship, '-x палубный корабль')
                            prov = False
                count -= 1
                #pole.print_pole(pl_ai)
            if count == 0:
                print('У AI не получилось расставить корабли')

    def fire_ships(self, pl_ai):

        if pl_ai == 'Player':
             good = False
             while not good:
                self.print_pole('AI')
                try_ = True
                while try_:
                    try:
                        xy_fire = list(map(int, input('Введите координаты выстрела (X Y):').split(' ')))
                        try_ = False
                    except:
                        print('Ввод не кореектный.')
                        try_ = True

                if (1 <= xy_fire[0] <= 6) and (1 <= xy_fire[1] <= 6):
                    xy_fire[0] -= 1
                    xy_fire[1] -= 1
                    if type(self.get_pole('AI')[xy_fire[0]][xy_fire[1]]) is Ship:
                        self.get_pole('AI')[xy_fire[0]][xy_fire[1]].hp -= 1
                        #print(self.get_pole('AI')[xy_fire[0]][xy_fire[1]].hp)
                        if self.get_pole('AI')[xy_fire[0]][xy_fire[1]].hp != 0:
                            self.get_pole('AI')[xy_fire[0]][xy_fire[1]] = '□'
                            print('Корабль поврежден. Стреляйте еще.')
                        elif self.get_pole('AI')[xy_fire[0]][xy_fire[1]].hp == 0:
                            ai_.del_ship(self.get_pole('AI')[xy_fire[0]][xy_fire[1]].name)
                            self.get_pole('AI')[xy_fire[0]][xy_fire[1]] = '□'
                            print('Корабль уничтожен! Стреляйте еще.')
                            print(ai_.live_ships)
                    elif self.get_pole('AI')[xy_fire[0]][xy_fire[1]] == '•':
                        print('Вы сюда уже стреляли. Стреляйте заново.')
                    else:
                        self.get_pole('AI')[xy_fire[0]][xy_fire[1]] = '•'
                        print('Вы промазали.')
                        good = True
                else:
                    print('Координата вне поля боя')

        if pl_ai == 'AI':
            good = False
            xy_fire = [0, 0]
            while not good:
                xy_fire[0] = randrange(0, 6, 1)
                xy_fire[1] = randrange(0, 6, 1)
                if type(self.get_pole('Player')[xy_fire[0]][xy_fire[1]]) == Ship:
                    self.get_pole('Player')[xy_fire[0]][xy_fire[1]].hp -= 1
                    if self.get_pole('Player')[xy_fire[0]][xy_fire[1]].hp > 0:
                        self.get_pole('Player')[xy_fire[0]][xy_fire[1]] = '□'
                        print('Ваш корабль поврежден.')
                    elif self.get_pole('Player')[xy_fire[0]][xy_fire[1]].hp == 0:
                        pl_.del_ship(self.get_pole('Player')[xy_fire[0]][xy_fire[1]].name)
                        self.get_pole('Player')[xy_fire[0]][xy_fire[1]] = '□'
                        print('Ваш корабль уничтожен!')
                        print(pl_.live_ships)
                elif self.get_pole('Player')[xy_fire[0]][xy_fire[1]] == '-':
                    self.get_pole('Player')[xy_fire[0]][xy_fire[1]] = '•'
                    print('Компьютер промазал.')
                    self.print_pole('Player')
                    good = True



class Player:
    def __init__(self, name):
        self.name = name
        self.player_ships = [3, 2, 2, 1, 1, 1, 1]
        self.live_ships = [3, 2, 2, 1, 1, 1, 1]

    def del_ship(self, name):
        self.live_ships.remove(name)


class Ship:
    def __init__(self, name, xy1, xy2, pl_ai):
        self.name = name
        self.hp = name
        self.xy1 = xy1
        self.xy2 = xy2
        self.pl_ai = pl_ai
    def __str__(self):
        if self.pl_ai == 'Player': return '■'
        if self.pl_ai == 'AI': return '-'



pole = Pole()

ai_ = Player('AI')
pl_ = Player('Player')

pole.input_ships('AI')
pole.input_ships('Player')

pole.print_pole('Player')

while (len(pl_.live_ships) > 0) or (len(ai_.live_ships) > 0):
    print(len(pl_.live_ships))
    print(len(ai_.live_ships))
    if len(pl_.live_ships) == 0:
        print('Победил компьютер')
        break
    if len(ai_.live_ships) == 0:
        print('Вы победили!')
        break
    pole.fire_ships('Player')
    pole.fire_ships('AI')

