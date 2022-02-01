import random
import numpy as np
import pandas as pd


class Make_players():
    def __init__(self,
                 cards4plaer,
                 humans,
                 robots,
                 mincars4plaer,
                 maxcars4plaer,
                 minplaers,
                 sizecoloda,
                 startpole
                 ):
        """
        Вспомогательный класс к классу class Durack()
        для создания игроков через метод maker_players()
        """
        self.MAX_PLAYERS = None
        self.CARDS_4PLAYER = cards4plaer
        self.humans = humans
        self.robots = robots
        self.MINCARDS_4PLAER = mincars4plaer
        self.MAXCARDS_4PLAER = maxcars4plaer
        self.MIN_PLAYERS = minplaers
        self.QQUANTY_COLODA = sizecoloda
        self.START_pole = startpole

    def __call__(self):
        players = self.maker_players()
        return players

    def opros(self):
        """
        Функция опросом устанавливает
        CARDS_4PLAYER - количество карт у игроков по игре
        hum - количество человек в игре
        rob - количество роботов в игре
        """
        err_h = True
        err_r = True
        err_cards = True

        # определение CARDS_4PLAYER
        while err_cards:
            if not self.CARDS_4PLAYER:
                try:
                    self.CARDS_4PLAYER = int(input(
                        f"Укажите количество карт выдаваемых на руки от {self.MINCARDS_4PLAER} до {self.MAXCARDS_4PLAER} включительно: "))
                except:
                    print("Ошибка, укажите число карт")
                    pass
            else:
                if not type(self.CARDS_4PLAYER) == int:
                    print("Ошибка, укажите число карт")
                    self.CARDS_4PLAYER = None
                    pass

            # проверка на вхождение в диапазон rfhn
            if self.CARDS_4PLAYER >= self.MINCARDS_4PLAER and self.CARDS_4PLAYER <= self.MAXCARDS_4PLAER:
                err_cards = False
            else:
                pass

        # определение MAX_PLAYERS
        self.MAX_PLAYERS = self.QQUANTY_COLODA // self.CARDS_4PLAYER
        # если что-то из self.humans or и self.robots не задано

        if (not self.humans and self.humans != 0) or not (self.robots and self.robots != 0):
            # определение self.humans
            while err_h:
                print(
                    f"Количество участников (роботы и люди) должно быть в сумме не менее {self.MIN_PLAYERS} и не более {self.MAX_PLAYERS}")
                if not self.humans and self.humans != 0:  # если self.humans не зздан ранее
                    try:
                        self.humans = int(input('Введите количество игроков людей: '))
                        err_h = False  # выход
                    except:
                        print("Ошибка, укажите число человек")
                        pass
                else:  # если self.humans зздан то проверка
                    if type(self.humans) == int:  # если self.humans число
                        print(f'Количество людей уже задано - {self.humans}')
                        err_h = False  # выход

                    else:  # если self.humans не число
                        print("Ошибка, укажите число человек")
                        self.humans = None  # сброс self.humans

                # определение self.robots
                if not self.robots and self.robots != 0:  # если self.robots не зздан ранее
                    while err_r:
                        try:
                            self.robots = int(input('Введите количество игроков роботов: '))
                            err_r = False  # выход
                        except:
                            print("Ошибка, укажите число роботов")
                            pass
                else:  # если self.robots зздан то проверка
                    if type(self.robots) == int:
                        print(f'Количество роботов уже задано - {self.robots}')
                        err_r = False  # выход

                    else:  # если self.robots не число
                        print("Ошибка, укажите число роботов")
                        self.robots = None  # сброс self.robots

                # проверка на вхождение в диапазон суммарного кол-ва игроков
                if self.humans + self.robots > self.MAX_PLAYERS \
                        or self.humans + self.robots < self.MIN_PLAYERS:  # если не в диапозоне
                    print(
                        f'Ошибка, указано суммарное количество игроков не в диапазоне {self.MIN_PLAYERS} - {self.MAX_PLAYERS}')
                    print()
                    err_h = True  # сброс
                    err_r = True  # сброс
                    if self.humans == 0 and self.robots == 0:
                        self.humans = None  # сброс
                        self.robots = None  # сброс
                else:
                    pass  # выход

        return self.humans, self.robots

    def make_player(self, robot=True, number=0):
        """
        Функция создает игрока
        роботу -  имя с переданным порядковым номером
        человеку - с введенным именем
        """
        player = self.START_pole.copy().astype(int)
        if robot:
            # определяем случайно стиль игры робота
            style = random.choice(('min', 'rand'))
            player.name = f'Robot_{number}({style})'
        else:
            player.name = input('Введите имя человека: ').title()
        return player

    def maker_players(self):
        """
        Функция создает список игроков players
        """
        hum, rob = self.opros()
        players = []
        if rob:
            for i in range(rob):
                players.append(self.make_player(number=i + 1))
        if hum:
            for _ in range(hum):
                print(f'Игрок {_ + 1}:')
                players.append(self.make_player(robot=False))
        return players


class Razdaza():

    def __init__(self,
                 playcoloda,
                 cards4plaer,
                 poleigry,
                 bitta,
                 startcoloda
                 ):
        """
        Вспомогательный класс к классу class Durack()
        раздает карты игрокам методом razdacha_card()
        """

        self.PLAY_coloda = playcoloda
        self.CARDS_4PLAYER = cards4plaer
        self.BITA = bitta
        self.POLE_IGRY = poleigry
        self.START_coloda = startcoloda
        self.PLAY = True

    def __call__(self, players):
        players, self.PLAY = self.razdacha_cards(players)
        return players, self.PLAY

    def perebor(self, df):
        """
        Функция контроля количества карт игрока
        df - входной датафрейм игрока
        """
        qty_card = (df != 0).sum().sum()
        if qty_card < self.CARDS_4PLAYER:
            situation = False
        else:
            situation = True
        return situation

    def random_card(self, vibor, value_card=0):
        """
        Функция определяет случайный выбор
        из vibor с учетом значения value_card
        """
        vibor_ = vibor.to_numpy()
        idx, jdx = np.where(vibor_ > value_card)
        i = random.randint(0, len(idx) - 1)
        return vibor.index[idx[i]], vibor.columns[jdx[i]]

    def take_cards(self, player, take='full'):
        """
        Функция получения карт из колоды
        take - сколько хочет взять карт, по умолчанию
              выдает до CARDS_4PLAYER(константы)
        player - кто берет карты
        """
        take_card = True
        schet = 0
