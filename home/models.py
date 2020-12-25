from django.db import models


class customer(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class tag(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(tag)

    def __str__(self):
        return self.name


class order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(
        customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    note = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.product.name
