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
    :param product_short_concept: One sentence concept of a product
    :param top_image: Show index.html works image file
    :param votes: Good counts to a product
    :param identifier: Identifier ForeignKey
    :type product_name: str
    :type product_short_concept: str
    :type top_image: file
    :type votes: int
    :type identifier: Int
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
    :type product: Int
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
    title = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='images', blank=True)
    # externalURL = models.URLField(blank=True)

    # def __str__(self):
    # def url(self):
    #     if self.externalURL:
    #         return self.externalURL
    #     else:
    #         return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.image)))
    #
    # def image_tag(self):
    #     return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))
    #
    # def __str__(self):
    #     return self.title
