from django.db import models
import os.path
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

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
    :param product_short_concept: One sentence concept of a product
    :param top_image: Show index.html works image file
    :param votes: Good counts to a product
    :param identifier: Identifier ForeignKey
    :type product_name: str
    :type product_short_concept: str
    :type top_image: file
    :type votes: int
    :type identifier: int
    """
    product_name = models.CharField(max_length=20, default='')
    product_short_concept = models.CharField(max_length=20, default='')
    top_image = models.ImageField(upload_to='images', blank=True)
    votes = models.IntegerField(default=0)
    identifier = models.ForeignKey(Identifier, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class ProductDetail(models.Model):
    """
    Model of Product Detail
    :param product_feature_concept: Product feature concept(short one sentence)
    :param product_feature_detail: Product feature detail sentences
    :param product_background_concept: Product background concept(short one sentence)
    :param product_background_detail: Product background detail sentences
    :param product: Product ForeignKey
    :type product_feature_concept: str
    :type product_feature_detail: str
    :type product_background_concept: str
    :type product_background_detail: str
    :type product: int
    """
    product_feature_concept = models.TextField(max_length=100)
    product_feature_detail = models.TextField(max_length=300)
    product_background_concept = models.TextField(max_length=300)
    product_background_detail = models.TextField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_function_concept


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
    comment_text = models.TextField(max_length=300)
    pub_date = models.DateTimeField('date published')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text


class ImageFile(models.Model):
    """
    Model of Image Files
    :param title: Image title name
    :param image: Image file
    :param product: Product ForeignKey
    :type title: str
    :type image: file
    :type product: int
    """
    S1 = 'S1'
    S2 = 'S2'
    S3 = 'S3'
    TITLE_CHOICES = (
        (S1, 'img1'),
        (S2, 'img2'),
        (S3, 'img3'),
    )

    def content_file_name(instance, filename):
        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([instance.title, '_', str(instance.product), ext])
        return '/'.join(['images', joined_filename])


    title = models.CharField(max_length=2, choices=TITLE_CHOICES, default=S1)
    image = models.ImageField(upload_to=content_file_name, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title


@receiver(pre_delete, sender=ImageFile)
def imagefile_delete(sender, instance, **kwargs):
    instance.image.delete(False)

@receiver(pre_delete, sender=Product)
def product_delete(sender, instance, **kwargs):
    instance.top_image.delete(False)
