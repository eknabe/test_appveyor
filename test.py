import os
import subprocess
import unittest
import ctypes

def run_app(number, expected_return_code):
    
    result = subprocess.run(['./main', str(number)], \
        cwd=os.path.dirname(os.path.realpath(__file__)))

    assert result.returncode == expected_return_code

class TestSum(unittest.TestCase):

    def test1(self):
        self.assertTrue(2 == 2)

    def test2(self):
        self.assertTrue(1 == 1)

    def test3(self):
        run_app(8, 8)
        run_app(0, 0)
        run_app(1, 1)
    
if __name__ == '__main__':
    unittest.main()