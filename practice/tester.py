import subprocess
import sys
import unittest

from operator   import (truediv, mul, sub)
from random     import (randint, random)
from functools  import (reduce)
from math       import (radians, degrees, sqrt)

PY = 'python3'

def rand(min: int = -sys.maxsize, max: int = sys.maxsize) -> int:
    return randint(min, max)

class unitTests(unittest.TestCase):
    comparison_mapping = {
        1: staticmethod(unittest.TestCase.assertEqual),
        2: staticmethod(unittest.TestCase.assertAlmostEqual)
    }

    def run_test(self, filename, expected, input = None, comparison_key = 1):
        if input:
            input = f'{input}\n'.encode()

        if comparison_key not in self.comparison_mapping:
            raise ValueError('Invalid comparison key')

        process = subprocess.Popen(
            [PY, filename],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        decoded_output, _ = process.communicate(input=input)
        decoded_output = decoded_output.decode().strip()
        conversor = type(expected)
        comparison = self.comparison_mapping[comparison_key]
        comparison(conversor(decoded_output), expected)

    def test_ex01_hello_world(self):
        self.run_test('chapter1/ex1.py', 'Olá mundo')

    def test_ex02_print_number(self):
        process = subprocess.Popen([PY, 'chapter1/ex2.py'], stdout=subprocess.PIPE)
        decoded_output = process.communicate()[0].decode().strip()
        self.assertTrue(decoded_output.isdigit(), True)

    def test_ex03_print_pi(self):
        self.run_test('chapter1/ex3.py', '3.1415')

    def test_ex04_print_char(self):
        self.run_test('chapter1/ex4.py', 'a')

    def test_ex05_print_int(self):
        self.run_test('chapter1/ex5.py', '2')

    def test_ex06_print_div(self):
        self.run_test('chapter1/ex6.py', f'{123 / 456}')

    def test_ex07_read_and_print_char(self):
        expected = 'Testing 123...'
        self.run_test('chapter1/ex7.py', expected, expected)

    def test_ex08_read_nums_and_print_them(self):
        input = '42\n3.14'
        expected = '42 3.14'
        self.run_test('chapter1/ex8.py', expected, input)

    def test_ex09_print_hex_and_octal(self):
        cases = [rand() for _ in range(10)]
        for number in cases:
            expected = '%x %o' % (number, number)
            self.run_test('chapter1/ex9.py', expected, number)

    def test_ex10_print_two_decimal_places(self):
        cases = [random() for _ in range(10)]
        for number in cases:
            expected = '%.2f' % number
            self.run_test('chapter1/ex10.py', expected, number)

    def test_ex11_print_at_least_three_digits(self):
        cases = [rand(-99, 100) for _ in range(10)]
        for number in cases:
            expected = '%03d' % number
            self.run_test('chapter1/ex11.py', expected, number)

    def test_ex12_revert_date(self):
        cases = [
            ('1/1/1970', '1970/1/1'),
            ('1/2/1987', '1987/2/1'),
            ('12/12/2012', '2012/12/12')
        ]
        for input, expected in cases:
            self.run_test('chapter1/ex12.py', expected, input)

    def test_ex13_print_the_square(self):
        cases = [rand() for _ in range(10)]
        for input in cases:
            expected = input ** 2
            self.run_test('chapter1/ex13.py', expected, input)

    def test_ex14_print_tenth_of_number(self):
        cases = [rand() for _ in range(10)]
        for input in cases:
            expected = input / 10
            self.run_test('chapter1/ex14.py', expected, input)

    def test_ex15_print_sum(self):
        cases = [(rand(), rand()) for _ in range(10)]
        for numbers in cases:
            input = '{}\n{}'.format(*numbers)
            expected = sum(numbers)
            self.run_test('chapter1/ex15.py', expected, input)

    def test_ex16_print_multiply(self):
        cases = [(rand(), rand()) for _ in range(10)]
        for numbers in cases:
            input = '{}\n{}'.format(*numbers)
            expected = reduce(mul, numbers)
            self.run_test('chapter1/ex16.py', expected, input)

    def test_ex17_calc_four_basic_operations(self):
        cases = [(rand(), rand()) for _ in range(10)]
        for numbers in cases:
            input = '{}\n{}'.format(*numbers)
            expected = '{}\n{}\n{}\n{}'.format(
                sum(numbers),
                reduce(sub, numbers),
                reduce(mul, numbers),
                reduce(truediv, numbers)
            )
            self.run_test('chapter1/ex17.py', expected, input)

    def test_ex18_sum_three_numbers(self):
        cases = [(rand(), rand(), rand()) for _ in range(10)]
        for numbers in cases:
            input = '{}\n{}\n{}'.format(*numbers)
            expected = sum(numbers)
            self.run_test('chapter1/ex18.py', expected, input)

    def test_ex19_Celcius_to_Fahrenheit(self):
        cases = [rand(-273) + random() for _ in range(10)]
        for number in cases:
            expected = (number * 9 / 5) + 32
            self.run_test('chapter1/ex19.py', expected, number)

    def test_ex20_Fahrenheit_to_Celcius(self):
        cases = [rand(-273) + random() for _ in range(10)]
        for number in cases:
            expected = (number - 32) * 5 / 9
            self.run_test('chapter1/ex20.py', expected, number)

    def test_ex21_Celcius_to_Kelvin(self):
        cases = [rand(-273) + random() for _ in range(10)]
        for number in cases:
            expected = (number + 273.15)
            self.run_test('chapter1/ex21.py', expected, number)

    def test_ex22_Kelvin_to_Celcius(self):
        cases = [rand(0) + random() for _ in range(10)]
        for number in cases:
            expected = (number - 273.15)
            self.run_test('chapter1/ex22.py', expected, number)

    def test_ex23_Fahrenheit_to_Kelvin(self):
        cases = [rand(0) + random() for _ in range(10)]
        for number in cases:
            expected = (number - 32) * 5 / 9 + 273.15
            self.run_test('chapter1/ex23.py', expected, number)

    def test_ex24_Kelvin_to_Fahrenheit(self):
        cases = [rand(0) + random() for _ in range(10)]
        for number in cases:
            expected = (number - 273.15) * 9 / 5 + 32
            self.run_test('chapter1/ex24.py', expected, number)

    def test_ex25_Celcius_to_Kelvin_and_Fahrenheit(self):
        cases = [rand(-273) + random() for _ in range(10)]
        for number in cases:
            kelvin = (number * 9 / 5) + 32
            fahrenheit = number + 273.15
            expected = '{} {}'.format(kelvin, fahrenheit)
            self.run_test('chapter1/ex25.py', expected, number)

    def test_ex26_degrees_to_radians(self):
        cases = [rand(-360, 360) for _ in range(10)]
        for degree in cases:
            self.run_test('chapter1/ex26.py',
                radians(degree), degree,
                comparison_key=2
            )

    def test_ex27_radians_to_degrees(self):
        cases = [radians(rand(-360, 360)) for _ in range(10)]
        for radian in cases:
            self.run_test('chapter1/ex27.py',
                degrees(radian), radian,
                comparison_key=2
            )

    def test_ex28_successor_antecessor(self):
        cases = [float(rand()) for _ in range(10)]
        for number in cases:
            self.run_test('chapter1/ex28.py',
                '{} {}'.format(number - 1, number + 1),
                number
            )

    def test_ex29_square_area(self):
        cases = [float(rand(1, 100)) for _ in range(10)]
        for side in cases:
            self.run_test('chapter1/ex29.py', side ** 2, side)

    def test_ex30_rectangle_area(self):
        cases = [(float(rand(1, 100)) for _ in range(2)) for _ in range(10)]
        for height, width in cases:
            self.run_test('chapter1/ex30.py',
                height * width,
                f'{height}\n{width}'
            )

    def test_ex31_right_triangle_area(self):
        cases = [(float(rand(1, 100)) for _ in range(2)) for _ in range(10)]
        for base, height in cases:
            self.run_test('chapter1/ex31.py',
                base * height / 2,
                f'{base}\n{height}'
            )

    def test_ex32_right_triangle_area(self):
        cases = [[float(rand(50, 99)) for _ in range(3)] for _ in range(10)]

        for sides in cases:
            s = sum(sides) / 2
            area = sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))
            input = '{}\n{}\n{}'.format(*sides)
            self.run_test('chapter1/ex32.py',
                area, input, comparison_key=2
            )

    def test_ex33_square_sum(self):
        cases = [[float(rand(-100, 100)) for _ in range(3)] for _ in range(10)]

        for numbers in cases:
            input = '{}\n{}\n{}'.format(*numbers)
            self.run_test('chapter1/ex33.py',
                reduce(lambda total, x: total + x ** 2, numbers, 0),
                input, comparison_key=2
            )

if __name__ == '__main__':
    unittest.main()
