import pytest
from BaseFool import Durack, Make_players

class TestFool:

    def setup(self):
        self.game = Durack(card4plaer=6, humans=0, robots=4)
        self.kozir = None
        self.game.players = None
        self.game.playcoloda = None
        print('Start test!')

    def teardown(self):
        self.players, self.playcoloda, self.kozir = self.game.init_game()
        var = type(self.kozir) == str
        var = type(self.players) == list
        var = type(self.playcoloda) == object
        print('Test init_game completed!')
        print()
        self.game.go_game(self.players, self.playcoloda, self.kozir)
        print('Test game completed!')

    def test_init(self):
        assert self.game.CARDS_4PLAYER == 6
        assert self.game.humans == 0
        assert self.game.robots == 4

