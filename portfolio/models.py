from django.db import models


class Identifier(models.Model):
    """
    Model of engineer or photographer identifiers
    :param name: Name of a identifier
    :type name: str
    """
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model of engineer and photographer works
    :param product_name: Name of a product
    :param votes: Good counts to a product
    :param identifier: Identifier ForeignKey
    :type product_name: str
    :type votes: int
    :type identifier: int
    """
    product_name = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
    identifier = models.ForeignKey(Identifier, on_delete=models.CASCADE)


    def __str__(self):
        return self.product_name


class Comment(models.Model):
    """
    Model of Comments to products
    :param comment_text: Text of comment to products
    :param pub_date: publish date of comment
    :param product: Product ForeignKey
    :type comment_text: str
    :type pub_date: date
    :type product: int
    """
    comment_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return self.comment_text
