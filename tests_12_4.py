import logging
from unittest import TestCase, main
from rt_with_exceptions import Runner


logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(levelname)s: %(message)s"
)

def repeat_method(obj, method_name, times):
    method = getattr(obj, method_name)
    for _ in range(times):
        method()


class RunnerTest(TestCase):
    def test_walk(self):
        try:
            boris = Runner('Boris', speed=-5)  # Неверная скорость
            repeat_method(boris, 'walk', 10)
            self.assertEqual(boris.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)

    def test_run(self):
        try:
            denis = Runner(123)  # Неверный тип имени
            repeat_method(denis, 'run', 10)
            self.assertEqual(denis.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)

    def test_challenge(self):
        try:
            boris, denis = Runner('Boris'), Runner('Denis')
            repeat_method(boris, 'walk', 10)
            repeat_method(denis, 'run', 10)
            self.assertNotEqual(denis.distance, boris.distance)
            logging.info('"test_challenge" выполнен успешно')
        except Exception as e:
            logging.error("Ошибка в test_challenge: %s", e)


if __name__ == '__main__':
    main()