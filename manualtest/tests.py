from django.test import TestCase

from manualtest.models import ProductName, ProductTestCase

class OrderEntryTestCase(TestCase):
    def setUp(self):
        tradingProduct = ProductName.objects.create(product="Trading")
        ProductTestCase.objects.create(testcase="orderEntry", product=tradingProduct)

    def test_case_name_properly_set(self):
        testCase = ProductTestCase.objects.get(testcase="orderEntry")
        self.assertEqual(testCase.product.product, 'Trading')
