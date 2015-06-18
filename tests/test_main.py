__author__ = 'alexander'

import unittest
from maker import find_intervals_in_variables,\
    remove_chars_from_string, make_output_file, adress_register,\
    make_div_by_sixteen


class test_find_intervals(unittest.TestCase):
    def setUp(self):
        self.test_list = {'CR': [
            1, 2, 3, 4, 64, 65, 128
        ],
        'AI': [
            1, 2, 3, 10, 20, 64, 256, 257, 276
        ]}
        self.test_result = {
            'CR': [
                adress_register(1, 16),
                adress_register(64, 16),
                adress_register(128, 16)
            ],
            'AI': [
                adress_register(1, 32),
                adress_register(64, 16),
                adress_register(256, 32),
            ]
        }

    def test_variables_1(self):
        self.assertDictEqual(find_intervals_in_variables(self.test_list), self.test_result)

class test_remove_function(unittest.TestCase):
    def setUp(self):
        self.test_str_1 = [
            'CR12', 'CR13', 'MO449', 'LEET1337'
        ]
        self.test_result_1 = {
            'CR': [12, 13],
            'MO': [449],
            'LEET': [1337]
        }
    def test_func_1(self):
        self.assertDictEqual(remove_chars_from_string(self.test_str_1), self.test_result_1)


'''
class test_output_function(unittest.TestCase):
    def test_output(self):
        self.test_dict_input = {
            'CR': [
                adress_register(1152, 128),
                adress_register(2152, 256),
            ],
            'MO': [
                adress_register(2, 32),
                adress_register(222, 64),                
            ]
        }
        self.test_str_output = 7    2        32  2    2        2    2        5        0        5        0        1|7    222      64  2    222      2    222      5        1        5        1        1|3    1152     128 1    1152     1    1152     5        0        5        0        1|3    2152     256 1    2152     1    2152     5        1        5        1        1|
        self.assertEqual(make_output_file(self.test_dict_input), self.test_str_output)
'''


class test_make_it_div_by_sixteen(unittest.TestCase):
    def setUp(self):
        self.testcase1 = 49
        self.testcase1_result = 64
        self.testcase2 = 127
        self.testcase2_result = 128
        self.testcase3 = 256
        self.testcase3_result = 256

    def test_output(self):
        self.assertEqual(make_div_by_sixteen(self.testcase1), self.testcase1_result)
        self.assertEqual(make_div_by_sixteen(self.testcase2), self.testcase2_result)
        self.assertEqual(make_div_by_sixteen(self.testcase3), self.testcase3_result)

if __name__ == '__main__':
    unittest.main()
