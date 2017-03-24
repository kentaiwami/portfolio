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
    Model of engineer works

    :param engineer_product_name: Product name
    :param engineer_product_alphabet_name: Product name(alphabet version)
    :param engineer_product_short_concept: One sentence concept
    :param top_image: Top image file of index.html
    :param col1_image: Row1 col1 image file of engineer_work_detail.html
    :param col2_image: Row1 col2 image file of engineer_work_detail.html
    :param col3_image: Row2 col image file of engineer_work_detail.html
    :param link: Product link
    :param votes: Good counts to a product
    :param sort_id: use sort

    :type engineer_product_name: str
    :type engineer_product_alphabet_name: str
    :type engineer_product_short_concept: str
    :type top_image: file
    :type col1_image: file
    :type col2_image: file
    :type col3_image: file
    :type link: str
    :type votes: int
    :type sort_id: int
    """

    def get_top_file_name(self, filename):
        """
        Get top image file path

        :param filename: Upload filename
        :return: media/images/e_work/PRODUCT_NAME/PRODUCT_NAME_top.*
        """

        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.engineer_product_alphabet_name, '_top', ext])
        return '/'.join(['images', get_e_work_str(), self.engineer_product_alphabet_name, joined_filename])

    def get_col1_file_name(self, filename):
        """
        Get col1 image file path

        :param filename: Upload filename
        :return: media/images/e_work/PRODUCT_NAME/PRODUCT_NAME_col1.*
        """

        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.engineer_product_alphabet_name, '_col1', ext])
        return '/'.join(['images', get_e_work_str(), self.engineer_product_alphabet_name, joined_filename])

    def get_col2_file_name(self, filename):
        """
        Get col2 image file path

        :param filename: Upload filename
        :return: media/images/e_work/PRODUCT_NAME/PRODUCT_NAME_col2.*
        """

        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.engineer_product_alphabet_name, '_col2', ext])
        return '/'.join(['images', get_e_work_str(), self.engineer_product_alphabet_name, joined_filename])

    def get_col3_file_name(self, filename):
        """
        Get col3 image file path

        :param filename: Upload filename
        :return: media/images/e_work/PRODUCT_NAME/PRODUCT_NAME_col3.*
        """

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
    sort_id = models.IntegerField(default=0, unique=True)

    tracker = FieldTracker()

    def __str__(self):
        return self.engineer_product_alphabet_name


class EngineerProductDetail(models.Model):
    """
    Model of engineer product Detail

    :param engineer_product_feature_concept: Product feature concept(short one sentence)
    :param engineer_product_feature_detail: Product feature detail sentences
    :param engineer_product_background_concept: Product background concept(short one sentence)
    :param engineer_product_background_detail: Product background detail sentences
    :param engineer_product_development_environment: ex.) used tools, frameworks
    :param engineer_product_development_language: used language
    :param engineer_product_creation_time: creation time
    :param engineer_product: Product ForeignKey

    :type engineer_product_feature_concept: str
    :type engineer_product_feature_detail: str
    :type engineer_product_background_concept: str
    :type engineer_product_background_detail: str
    :type engineer_product_development_environment: str
    :type engineer_product_development_language: str
    :type engineer_product_creation_time: str
    :type engineer_product: int
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
    Model of photographer product

    :param photographer_product_name: Product name
    :param photographer_product_alphabet_name: Product alphabet name
    :param photographer_main_image: Product origin image
    :param photographer_thumbnail_image: Product thumbnail image
    :param photographer_product_location: Product location
    :param photographer_product_shooting_year: Product shooting year
    :param photographer_product_shooting_month: Product shooting month
    :param photographer_product_shooting_day: Product shooting day
    :param photographer_product_shooting_hour: Product shooting hour
    :param photographer_product_shooting_minute: Product shooting minute
    :param sort_id: Use sort

    :type photographer_product_name: str
    :type photographer_product_alphabet_name: str
    :type photographer_main_image: file
    :type photographer_thumbnail_image: file
    :type photographer_product_location: str
    :type photographer_product_shooting_year: str
    :type photographer_product_shooting_month: str
    :type photographer_product_shooting_day: str
    :type photographer_product_shooting_hour: str
    :type photographer_product_shooting_minute: str
    :type sort_id: int
    """

    def get_main_image_file_name(self, filename):
        """
        Get main image file path

        :param filename: Upload filename
        :return: media/images/p_work/main/PRODUCT_NAME_main.*
        """

        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.photographer_product_alphabet_name, '_main', ext])
        return '/'.join(['images', get_p_work_str(), get_p_work_main_str(), joined_filename])

    def get_thumbnail_image_file_name(self, filename):
        """
        Get thumbnail image file path

        :param filename: Upload filename
        :return: media/images/p_work/thumbnail/PRODUCT_NAME_thumbnail.*
        """
        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.photographer_product_alphabet_name, '_thumbnail', ext])
        return '/'.join(['images', get_p_work_str(), get_p_work_thumbnail_str(), joined_filename])

    photographer_product_name = models.CharField(max_length=100, default='', unique=True)
    photographer_product_alphabet_name = models.CharField(max_length=200, default='', unique=True)
    photographer_main_image = models.ImageField(upload_to=get_main_image_file_name, blank=True)
    photographer_thumbnail_image = models.ImageField(upload_to=get_thumbnail_image_file_name, blank=True)

    photographer_product_location = models.CharField(max_length=30, default='', blank=True)
    photographer_product_shooting_year = models.IntegerField(blank=True, default=2000)
    photographer_product_shooting_month = models.IntegerField(blank=True, default=12)
    photographer_product_shooting_day = models.IntegerField(blank=True, default=31)
    photographer_product_shooting_hour = models.IntegerField(blank=True, default=12)
    photographer_product_shooting_minute = models.IntegerField(blank=True, default=59)
    sort_id = models.IntegerField(default=0, unique=True)

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
        return 'Comment' + str(self.pk)


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
