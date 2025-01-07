from unittest import TestCase
from runner_and_tournament import Runner, Tournament

class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = Runner('Usein', 10)
        self.andrey = Runner('Andrey', 9)
        self.nick = Runner('Nick', 3)

    @classmethod
    def tearDownClass(cls):
        for test_num, results in cls.all_results.items():
            print(f'Test {test_num}: {results}')

    def test_usein_and_nick(self):
        tournament = Tournament(90, self.usein, self.nick)
        results = tournament.start()
        self.__class__.all_results[1] = results
        self.assertTrue(list(results.values())[-1] == 'Nick')

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results[2] = results
        self.assertTrue(list(results.values())[-1] == 'Nick')

    def test_all_runners(self):
        tournament = Tournament(90, self.usein, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results[3] = results
        self.assertTrue(list(results.values())[-1] == 'Nick')