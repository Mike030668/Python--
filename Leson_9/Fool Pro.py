import random
import numpy as np
import pandas as pd
from BaseFool import Durack, Make_game, Razdaza, Make_players

"""
Количество карт, людей и роботов уже задано

Перед вами сыграют роботы со случайной инициализацией
типа игры, см. сообщение вначале

"""

# Инициализация игры
game = Durack(card4plaer=6, humans=0, robots=4)
gaimers, playcoloda, kozir = game.init_game()

# Запуск игрового цикла
game.go_game(gaimers, playcoloda, kozir)