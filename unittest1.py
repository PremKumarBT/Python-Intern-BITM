class Square:
    def __init__(self, length) -> None:
        if type(length) not in [int, float]:
            raise TypeError('Length must be an integer or float')
        if length < 0:
            raise ValueError('Length must not be negative')

        self.length = length

    def area(self):
        return self.length * self.length
#class Mngo:
    

#print(dir(locals()["__builtins__"]))

#TestSquare

import unittest

#from square import Square

class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)

    def test_length_with_wrong_type(self):
        with self.assertRaises(TypeError):
            square = Square('10')

    def test_length_with_zero_or_negative(self):
        with self.assertRaises(ValueError):
            square = Square(0)
            square = Square(-1)


if __name__ == '__main__':
    unittest.main(verbosity=2)