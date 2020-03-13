# test/nulls_test.py

import unittest

from package.nulls import nulls

data = [['tom', 10], ['nick', 15], ['juli', 14], ['jason', 0]] 

df = pd.DataFrame(data, columns = ['name', 'age'])

class TestNull(unittest.TestCase):

    #def test_null(self):
    #    sefl.assertTrue('name', 'age')

if __name__ == '__main__':
    unittest.ma