from pytest_file_1 import *

class TestClass:

    def test_1(self):
        assert func_return_true() == True
    
    def test_2(self):
        assert func_return_false() == False

    def test_3(self):
        assert func_return_123() == 123

    def test_4(self):
        assert func_return_prime(3) == True