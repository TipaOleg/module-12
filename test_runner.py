from unittest import TestCase, main
from runner import Runner

def repeat_method(obj, method_name, times):
    method = getattr(obj, method_name)
    for _ in range(times):
        method()


class RunnerTest(TestCase):
    def test_walk(self):
        boris = Runner('Boris')
        repeat_method(boris, 'walk', 10)
        self.assertEqual(boris.distance, 50)

    def test_run(self):
        denis = Runner('Denis')
        repeat_method(denis, 'run', 10)
        self.assertEqual(denis.distance, 100)

    def test_challenge(self):
        boris, denis = Runner('Boris'), Runner('Denis')
        repeat_method(boris, 'walk', 10)
        repeat_method(denis, 'run', 10)
        self.assertNotEqual(denis.distance, boris.distance)


if __name__ == '__main__':
    main()