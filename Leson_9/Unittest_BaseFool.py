import unittest
from BaseFool import Durack


class TestFool_unittest(unittest.TestCase):
    def setUp(self):
        self.game = Durack(card4plaer=6, humans=2, robots=3)
        self.players, self.playcoloda, self.kozir = self.game.init_game()
        print('Start test!')

    def tearDown(self):
        print('Test completed!')
        print('_______________________')
        print()
        del self.game.CARDS_4PLAYER,self.game.humans,self.game.robots

    def test_types(self):
        self.assertTrue(type(self.kozir), str)
        self.assertTrue(type(self.players), list)
        print('Test types completed!')
        print('_______________________')
        print()

    def test_init(self):
        self.assertEqual(self.game.CARDS_4PLAYER, 6)
        self.assertEqual(self.game.humans, 2)
        self.assertEqual(self.game.robots, 3)
        print('Test init_game completed!')
        print('_______________________')
        print()

    def test_players(self):
        self.assertEqual(self.game.humans + self.game.robots, len(self.players))
        print('Test players completed!')
        print('_______________________')

    def test_cards(self):
        self.assertEqual(self.game.CARDS_4PLAYER * len(self.players),
                         sum([(player != 0).sum().sum() for player in self.players])
                         )
        print('Test cards completed!')
        print('_______________________')

    def test_game(self):
        # меняем имена игроков на роботов для ухода от input() при тесте игры
        for number, player in enumerate(self.players):
            player.name = f'Robot_{number}(min)'
        self.game.go_game(self.players, self.playcoloda, self.kozir)
        print('Test game completed!')
        print('_______________________')
