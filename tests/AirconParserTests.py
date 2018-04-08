import unittest

from AirconParser import PassengerParser


class AirconParserTests(unittest.TestCase):

    def test_can_recognize_man(self):
        passenger = PassengerParser("1ACARREGUI/MARIADOLORESMR")
        assert passenger.gender is "MR"

    def test_can_recognize_woman(self):
        passenger = PassengerParser("1ACARREGUI/MARIADOLORESMRS")
        assert passenger.gender is "MRS"

    def test_can_recognize_missing_gender(self):
        passenger = PassengerParser("1ACARREGUI/MARIADOLORES")
        assert passenger.gender is "?"


if __name__ == '__main__':
    unittest.main()
