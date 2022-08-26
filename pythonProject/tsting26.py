import unittest
from day2.rpsfun import rps
class rpsTest(unittest.TestCase):
    def testrps(self):
        self.assertEqual('r',rps('r','p'))

    def testrps1(self):
            self.assertEqual('r', rps('r', 'p'))

