import numpy as np
import pytest
from simple_functions import factorial, my_sum
from simple_functions.trig_functions import s


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [([8, 7, 5], 20),
                                                    ((10, -2, 5, -10, 1), 4)])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [(5, 120), (3, 6), (1, 1)])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer == expected

    @pytest.mark.parametrize('number, expected', [(np.pi, 0), (0.5 * np.pi, 1),
                                                  (np.pi/6, 0.5)])
    def test_sin(self, number, expected):
        '''Test our factorial function'''
        answer = s(number)
        assert (answer - expected) < 1e-5
