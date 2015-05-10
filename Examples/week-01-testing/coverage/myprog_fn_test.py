import unittest

from myprog_fn import foo

class TestFooFn(unittest.TestCase):

    def test_true(self):
        foo( False )


