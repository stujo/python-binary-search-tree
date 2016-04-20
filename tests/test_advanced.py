# -*- coding: utf-8 -*-

from .context import bst

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        bst.hmm()


if __name__ == '__main__':
    unittest.main()