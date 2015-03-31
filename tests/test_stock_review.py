#!/usr/bin/env python
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.tests.test_tryton import test_view, test_depends
import trytond.tests.test_tryton
import unittest


class StockReviewTestCase(unittest.TestCase):
    'Test Stock Review module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('stock_review')

    def test0005views(self):
        'Test views'
        test_view('stock_review')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockReviewTestCase))
    return suite
