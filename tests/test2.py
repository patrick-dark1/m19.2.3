import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self,1, 3) == 4

    def test_subtraction_success(self):
        assert self.calc.subtraction(self,1, 1) == 0

    def test_division_success(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_multiply_success(self):
        assert self.calc.multiply(self,20, 2) == 40

    def teardown(self):
        print('Выполнение метода Teardown')