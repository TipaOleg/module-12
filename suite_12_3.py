from unittest import TestLoader, TestSuite, TextTestRunner, TextTestResult
from test_runner import RunnerTest
from test_runner_and_tournament import TournamentTest


def frozen_control(method):
    def wrapper(self, *args, **kwargs):
        if getattr(self.__class__, "is_frozen", False):
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return method(self, *args, **kwargs)
    return wrapper


class RunnerTest(RunnerTest):
    is_frozen = False

    @frozen_control
    def test_walk(self):
        super().test_walk()

    @frozen_control
    def test_run(self):
        super().test_run()

    @frozen_control
    def test_challenge(self):
        super().test_challenge()


class TournamentTest(TournamentTest):
    is_frozen = True

    @frozen_control
    def test_usein_and_nick(self):
        super().test_usein_and_nick()

    @frozen_control
    def test_andrey_and_nick(self):
        super().test_andrey_and_nick()

    @frozen_control
    def test_all_runners(self):
        super().test_all_runners()


def suite():
    suite = TestSuite()
    suite.addTest(TestLoader().loadTestsFromTestCase(RunnerTest))
    suite.addTest(TestLoader().loadTestsFromTestCase(TournamentTest))
    return suite

if __name__ == "__main__":
    runner = TextTestRunner(verbosity=2)
    runner.run(suite())
