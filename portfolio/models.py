from django.db import models
import os.path
from django.db.models.signals import pre_delete, post_save
from django.dispatch.dispatcher import receiver
from model_utils import FieldTracker
from django.conf import settings


def get_e_work_str():
    return 'e_work'


def get_p_work_str():
    return 'p_work'


def get_p_work_main_str():
    return 'main'


def get_p_work_thumbnail_str():
    return 'thumbnail'


class EngineerProduct(models.Model):
    """
    Model of engineer and photographer works

    :param product_name: Product name
    :param product_alphabet_name: Product name(alphabet version)
    :param product_short_concept: One sentence concept
    :param product_location: photographer works only
    :param product_shooting_date_year: photographer works only
    :param product_shooting_date_month: photographer works only
    :param top_image: Show index.html works image file
    :param votes: Good counts to a product
    :param sort_id: use sort
    :param identifier: Identifier ForeignKey

    :type product_name: str
    :type product_alphabet_name: str
    :type product_short_concept: str
    :type product_location: str
    :type product_shooting_date_year: str
    :type product_shooting_date_month: str
    :type top_image: file
    :type votes: int
    :type sort_id: int
    :type identifier: int
    """

    def get_top_file_name(self, filename):
        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.engineer_product_alphabet_name, '_top', ext])
        return '/'.join(['images', get_e_work_str(), self.engineer_product_alphabet_name, joined_filename])

    def get_col1_file_name(self, filename):
        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.engineer_product_alphabet_name, '_col1', ext])
        return '/'.join(['images', get_e_work_str(), self.engineer_product_alphabet_name, joined_filename])

    def get_col2_file_name(self, filename):
        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.engineer_product_alphabet_name, '_col2', ext])
        return '/'.join(['images', get_e_work_str(), self.engineer_product_alphabet_name, joined_filename])

    def get_col3_file_name(self, filename):
        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.engineer_product_alphabet_name, '_col3', ext])
        return '/'.join(['images', get_e_work_str(), self.engineer_product_alphabet_name, joined_filename])

    engineer_product_name = models.CharField(max_length=20, default='', unique=True)
    engineer_product_alphabet_name = models.CharField(max_length=40, default='', unique=True)
    engineer_product_short_concept = models.CharField(max_length=30, default='')

    top_image = models.ImageField(upload_to=get_top_file_name, blank=True)
    col1_image = models.ImageField(upload_to=get_col1_file_name, blank=True)
    col2_image = models.ImageField(upload_to=get_col2_file_name, blank=True)
    col3_image = models.ImageField(upload_to=get_col3_file_name, blank=True)

    link = models.URLField(max_length=200, blank=True, default='')
    votes = models.IntegerField(default=0)
    sort_id = models.IntegerField(default=0)

    tracker = FieldTracker()

    def __str__(self):
        return self.engineer_product_alphabet_name


class EngineerProductDetail(models.Model):
    """
    Model of Product Detail

    :param product_feature_concept: Product feature concept(short one sentence)
    :param product_feature_detail: Product feature detail sentences
    :param product_background_concept: Product background concept(short one sentence)
    :param product_background_detail: Product background detail sentences
    :param product_development_environment: ex.) used tools, frameworks
    :param product_development_language: used language
    :param product_creation_time: creation time
    :param product: Product ForeignKey

    :type product_feature_concept: str
    :type product_feature_detail: str
    :type product_background_concept: str
    :type product_background_detail: str
    :type product_development_environment: str
    :type product_development_language: str
    :type product_creation_time: str
    :type product: int
    """
    engineer_product_feature_concept = models.TextField(max_length=30, default='', blank=True)
    engineer_product_feature_detail = models.TextField(max_length=300, default='', blank=True)

    engineer_product_background_concept = models.TextField(max_length=30, default='', blank=True)
    engineer_product_background_detail = models.TextField(max_length=300, default='', blank=True)

    engineer_product_development_environment = models.TextField(max_length=300, default='', blank=True)
    engineer_product_development_language = models.TextField(max_length=300, default='', blank=True)
    engineer_product_creation_time = models.TextField(max_length=50, default='', blank=True)
    engineer_product = models.ForeignKey(EngineerProduct, on_delete=models.CASCADE)

    def __str__(self):
        return self.engineer_product.__str__() + ' Detail'


class PhotographerProduct(models.Model):
    """

    """

    def get_main_image_file_name(self, filename):
        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.photographer_product_alphabet_name, '_main', ext])
        return '/'.join(['images', get_p_work_str(), get_p_work_main_str(), joined_filename])

    def get_thumbnail_image_file_name(self, filename):
        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.photographer_product_alphabet_name, '_thumbnail', ext])
        return '/'.join(['images', get_p_work_str(), get_p_work_thumbnail_str(), joined_filename])

    photographer_product_name = models.CharField(max_length=100, default='', unique=True)
    photographer_product_alphabet_name = models.CharField(max_length=200, default='', unique=True)
    photographer_main_image = models.ImageField(upload_to=get_main_image_file_name, blank=True)
    photographer_thumbnail_image = models.ImageField(upload_to=get_thumbnail_image_file_name, blank=True)

    photographer_product_location = models.CharField(max_length=30, default='', blank=True)
    photographer_product_shooting_year = models.CharField(max_length=4, default='', blank=True)
    photographer_product_shooting_month = models.CharField(max_length=2, default='', blank=True)
    photographer_product_shooting_day = models.CharField(max_length=2, default='', blank=True)
    photographer_product_shooting_hour = models.CharField(max_length=2, default='', blank=True)
    photographer_product_shooting_minute = models.CharField(max_length=2, default='', blank=True)
    sort_id = models.IntegerField(default=0)

    tracker = FieldTracker()

    def __str__(self):
        return self.photographer_product_name


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
    engineer_product = models.ForeignKey(EngineerProduct, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text


@receiver(pre_delete, sender=EngineerProduct)
def product_top_image_delete(sender, instance, **kwargs):
    """
    When delete EngineerProduct record, delete four images that relation self instance

    :param sender:
    :param instance: EngineerProduct record
    :param kwargs:
    """
    instance.top_image.delete(False)
    instance.col1_image.delete(False)
    instance.col2_image.delete(False)
    instance.col3_image.delete(False)


@receiver(post_save, sender=EngineerProduct)
def product_clear_image_field_delete_file(sender, instance, **kwargs):
    """
    When image field's clear and save, delete an image that relation self instance
    :param sender:
    :param instance: Product record
    :param kwargs:
    """

    column_list = ['top_image', 'col1_image', 'col2_image', 'col3_image']
    path_list = []
    for column_name in column_list:
        path_list.append(settings.MEDIA_ROOT + '/' + str(instance.tracker.previous(column_name)))

    if os.path.isfile(path_list[0]) and instance.top_image == '':
            os.remove(path_list[0])

    if os.path.isfile(path_list[1]) and instance.col1_image == '':
        os.remove(path_list[1])

    if os.path.isfile(path_list[2]) and instance.col2_image == '':
        os.remove(path_list[2])

    if os.path.isfile(path_list[3]) and instance.col3_image == '':
        os.remove(path_list[3])


@receiver(pre_delete, sender=PhotographerProduct)
def photographer_image_delete(sender, instance, **kwargs):
    """
    When delete EngineerProduct record, delete four images that relation self instance

    :param sender:
    :param instance: EngineerProduct record
    :param kwargs:
    """
    instance.photographer_main_image.delete(False)
    instance.photographer_thumbnail_image.delete(False)


@receiver(post_save, sender=PhotographerProduct)
def photographerProduct_clear_image_field_delete_file(sender, instance, **kwargs):
    """
    When image field's clear and save, delete an image that relation self instance
    :param sender:
    :param instance: Product record
    :param kwargs:
    """

    column_list = ['photographer_main_image', 'photographer_thumbnail_image']
    path_list = []
    for column_name in column_list:
        path_list.append(settings.MEDIA_ROOT + '/' + str(instance.tracker.previous(column_name)))

    if os.path.isfile(path_list[0]) and instance.photographer_main_image == '':
            os.remove(path_list[0])

    if os.path.isfile(path_list[1]) and instance.photographer_thumbnail_image == '':
        os.remove(path_list[1])
