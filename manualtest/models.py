from django.db import models

# Create your models here.

class ProductName(models.Model):
    product = models.CharField(max_length=64)
    user =  models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.product}"

class ProductTestCase(models.Model):
    testcase = models.CharField(max_length=64)
    teststep = models.CharField(max_length=64)
    product =  models.ForeignKey(ProductName, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.testcase} belongs to product name {self.product.product}"


class TestRun(models.Model):
    result = models.CharField(max_length=64)
    observation = models.CharField(max_length=64)
    testcasemapper = models.ForeignKey(ProductTestCase, on_delete=models.CASCADE)
    date = models.CharField(max_length=64)
    def __str__(self):
        return f"Product name {self.testcasemapper} has testcase {self.testcasemapper.testcase} with result {self.result}"