import random
import numpy as np
import pandas as pd
from BaseFool import Durack

"""
Количество карт, людей и роботов уже задано.
Вам нужно указать имя при опросе
Далее нужно смотреть на сообщения и отвечать на вопросы в игре

Вы сыграете со случайным роботом,
"""

# Инициализация игры
game = Durack(card4plaer=6, humans=1, robots=1)
gaimers, playcoloda, kozir = game.init_game()

# Запуск игрового цикла
game.go_game(gaimers, playcoloda, kozir)