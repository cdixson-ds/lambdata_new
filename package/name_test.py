#test/name_test.py

import unittest

#from package.name import get_first
from name import Person, Student

class TestFirst(unittest.TestCase):

    def test_first(self):
        """
        test to see if the get_first function works
        """
        jack = Student('jack', 1990, 'Art')
        #self.assertEqual(jack.first.islower(), 'jack')
        self.assertEqual(jack.first, 'jack')

if __name__ == '__main__':
    unittest.main()

  
