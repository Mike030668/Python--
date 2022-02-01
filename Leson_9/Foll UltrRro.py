import random
import numpy as np
import pandas as pd
from BaseFool import Durack, Make_game, Razdaza, Make_players

"""
Пройдите опрос перед игрой
- укажите количество карт выдаваемых на руки
- укажите оличество людей, роботов
- Дайте имена людям

- если в игоре люди, то нужно смотреть на сообщения
  и отвечать на вопросы в игре

"""

# Инициализация игры
game = Durack()
gaimers, playcoloda, kozir = game.init_game()

# Запуск игрового цикла
game.go_game(gaimers, playcoloda, kozir)

