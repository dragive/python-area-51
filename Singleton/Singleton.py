import unittest


class Singleton:
    _instance = None

    value = 1

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Values put here are initialized everytime
        """
        pass

    def __str__(self):
        return str(self.value)


class SingletonTest(unittest.TestCase):
    def test_instance(self):
        a = Singleton()
        a.value = 1
        assert a.value == 1
        a.value = 2
        assert a.value == 2

        b = Singleton()

        assert a == b

        assert b.value == 2

        b.value = 10
        assert a.value == 10 and b.value == 10
