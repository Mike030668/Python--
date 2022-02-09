import pytest
from BaseFool import Durack


class TestFool:
    def setup(self):
        self.game = Durack(card4plaer=6, humans=2, robots=3)
        self.players, self.playcoloda, self.kozir = self.game.init_game()
        print('Start test!')

    def test_types(self):
        assert type(self.kozir) == str
        assert type(self.players) == list
        print('Test types completed!')
        print('_______________________')
        print()

    def teardown(self):
        assert self.game.CARDS_4PLAYER == 6
        assert self.game.humans == 2
        assert self.game.robots == 3
        print('Test init_game completed!')
        print('_______________________')
        print()

    def test_players(self):
        assert self.game.humans + self.game.robots == len(self.players)
        print('Test players completed!')
        print('_______________________')

    def test_cards(self):
        assert self.game.CARDS_4PLAYER * len(self.players) == sum(
            [(player != 0).sum().sum() for player in self.players])
        print('Test cards completed!')
        print('_______________________')

    def test_game(self):
        # меняем имена игроков на роботов для ухода от input() при тесте игры
        for number, player in enumerate(self.players):
            player.name = f'Robot_{number}(min)'
        self.game.go_game(self.players, self.playcoloda, self.kozir)
        print('Test game completed!')
        print('_______________________')
