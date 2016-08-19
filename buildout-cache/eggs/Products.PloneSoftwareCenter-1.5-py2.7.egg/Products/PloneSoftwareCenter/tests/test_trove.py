"""trove.py tests
$Id: test_trove.py 59742 2008-02-29 16:24:43Z aclark $
"""
import unittest
import os
from Globals import package_home

from Products.PloneSoftwareCenter.trove import TroveClassifier

GLOBALS = globals()

class TestTrove(unittest.TestCase):
   
    def setUp(self):
        self.trove_default = os.path.join(package_home(GLOBALS), 'TROVE.txt')
        self.trove = TroveClassifier(self.trove_default)
    
    def test_makeid(self):
        res = self.trove._make_id('1 - Planning')
        self.assertEquals(res, ('1-planning', '1 - Planning'))

    def test_build(self):
        self.assertEquals(self.trove.get()[0], 
                          'Development Status :: 1 - Planning')
        self.assertEquals(self.trove.get()[-1], 'Topic :: Utilities')

        grid = self.trove.get_datagrid()
        self.assertEquals(grid[0], 
            '1-planning|1 - Planning|Development Status :: 1 - Planning' )
        self.assertEquals(grid[-1], 
            'utilities|Utilities|Topic :: Utilities')

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestTrove))
    return suite

