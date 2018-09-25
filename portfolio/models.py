from django.db import models
from django.db.models.signals import pre_delete, post_save
from django.dispatch.dispatcher import receiver
from model_utils import FieldTracker
from django.conf import settings
import os.path
import shutil


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

    :param name: Product name
    :param alphabet_name: Product name(alphabet version)
    :param short_concept: One sentence concept
    :param feature_concept: Product feature concept(short one sentence)
    :param feature_detail: Product feature detail sentences
    :param background_concept: Product background concept(short one sentence)
    :param background_detail: Product background detail sentences
    :param development_environment: ex.) used tools, frameworks
    :param development_language: used language
    :param creation_time: creation time
    :param top_image: Top image file of index.html
    :param col1_image: Row1 col1 image file of engineer_work_detail.html
    :param col2_image: Row1 col2 image file of engineer_work_detail.html
    :param col3_image: Row2 col image file of engineer_work_detail.html
    :param github: Product GitHub link
    :param store: Product store link
    :param sort_id: use sort

    :type name: str
    :type alphabet_name: str
    :type short_concept: str
    :type feature_concept: str
    :type feature_detail: str
    :type background_concept: str
    :type background_detail: str
    :type development_environment: str
    :type development_language: str
    :type creation_time: str
    :type top_image: file
    :type col1_image: file
    :type col2_image: file
    :type col3_image: file
    :type github: str
    :type store: str
    :type sort_id: int
    """

    def get_top_file_name(self, filename):
        """
        Get top image file path

        :param filename: Upload filename
        :return: media/images/e_work/PRODUCT_NAME/PRODUCT_NAME_top.*
        """

        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.alphabet_name, '_top', ext])
        return '/'.join(['images', get_e_work_str(), self.alphabet_name, joined_filename])

    def get_col1_file_name(self, filename):
        """
        Get col1 image file path

        :param filename: Upload filename
        :return: media/images/e_work/PRODUCT_NAME/PRODUCT_NAME_col1.*
        """

        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.alphabet_name, '_col1', ext])
        return '/'.join(['images', get_e_work_str(), self.alphabet_name, joined_filename])

    def get_col2_file_name(self, filename):
        """
        Get col2 image file path

        :param filename: Upload filename
        :return: media/images/e_work/PRODUCT_NAME/PRODUCT_NAME_col2.*
        """

        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.alphabet_name, '_col2', ext])
        return '/'.join(['images', get_e_work_str(), self.alphabet_name, joined_filename])

    def get_col3_file_name(self, filename):
        """
        Get col3 image file path

        :param filename: Upload filename
        :return: media/images/e_work/PRODUCT_NAME/PRODUCT_NAME_col3.*
        """

        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.alphabet_name, '_col3', ext])
        return '/'.join(['images', get_e_work_str(), self.alphabet_name, joined_filename])

    name = models.CharField(max_length=20, default='', unique=True)
    alphabet_name = models.CharField(max_length=40, default='', unique=True)
    short_concept = models.CharField(max_length=30, default='')
    feature_concept = models.TextField(max_length=30, default='', blank=True)
    feature_detail = models.TextField(max_length=300, default='', blank=True)
    background_concept = models.TextField(max_length=30, default='', blank=True)
    background_detail = models.TextField(max_length=300, default='', blank=True)
    development_environment = models.TextField(max_length=300, default='', blank=True)
    development_language = models.TextField(max_length=300, default='', blank=True)
    creation_time = models.TextField(max_length=50, default='', blank=True)

    top_image = models.ImageField(upload_to=get_top_file_name, blank=True)
    col1_image = models.ImageField(upload_to=get_col1_file_name, blank=True)
    col2_image = models.ImageField(upload_to=get_col2_file_name, blank=True)
    col3_image = models.ImageField(upload_to=get_col3_file_name, blank=True)

    github = models.URLField(max_length=200, blank=True, default='')
    store = models.URLField(max_length=200, blank=True, default='')
    sort_id = models.IntegerField(default=0, unique=True)

    tracker = FieldTracker()

    def __str__(self):
        return self.alphabet_name


class PhotographerProduct(models.Model):
    """
    Model of photographer product

    :param name: Product name
    :param alphabet_name: Product alphabet name
    :param main_image: Product origin image
    :param thumbnail_image: Product thumbnail image
    :param location: Product location
    :param shooting_date: Product shooting date
    :param sort_id: Use sort

    :type name: str
    :type alphabet_name: str
    :type main_image: file
    :type thumbnail_image: file
    :type location: str
    :type shooting_date: datetime
    :type sort_id: int
    """

    def get_main_image_file_name(self, filename):
        """
        Get main image file path

        :param filename: Upload filename
        :return: media/images/p_work/main/PRODUCT_NAME_main.*
        """

        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.alphabet_name, '_main', ext])
        return '/'.join(['images', get_p_work_str(), get_p_work_main_str(), joined_filename])

    def get_thumbnail_image_file_name(self, filename):
        """
        Get thumbnail image file path

        :param filename: Upload filename
        :return: media/images/p_work/thumbnail/PRODUCT_NAME_thumbnail.*
        """
        path, ext = os.path.splitext(filename)
        joined_filename = ''.join([self.alphabet_name, '_thumbnail', ext])
        return '/'.join(['images', get_p_work_str(), get_p_work_thumbnail_str(), joined_filename])

    name = models.CharField(max_length=100, default='', unique=True)
    alphabet_name = models.CharField(max_length=200, default='', unique=True)
    main_image = models.ImageField(upload_to=get_main_image_file_name, blank=True)
    thumbnail_image = models.ImageField(upload_to=get_thumbnail_image_file_name, blank=True)

    location = models.CharField(max_length=30, default='', blank=True)
    shooting_date = models.DateTimeField(null=True, default=None)
    sort_id = models.IntegerField(default=0, unique=True)

    tracker = FieldTracker()

    def __str__(self):
        return self.name


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
    name = models.CharField(max_length=50, default='名無し', blank=True)
    comment_text = models.TextField(max_length=300, default='', blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
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

    media_root = settings.MEDIA_ROOT
    path = '/'.join([media_root, 'images', get_e_work_str(), str(instance)])

    if os.path.isdir(path):
        shutil.rmtree(path)


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
    When delete EngineerProduct record, delete two images(main, thumbnail) that relation self instance

    :param sender:
    :param instance: EngineerProduct record
    :param kwargs:
    """
    instance.main_image.delete(False)
    instance.thumbnail_image.delete(False)


@receiver(post_save, sender=PhotographerProduct)
def photographerProduct_clear_image_field_delete_file(sender, instance, **kwargs):
    """
    When image field's clear and save, delete an image that relation self instance
    :param sender:
    :param instance: Product record
    :param kwargs:
    """

    column_list = ['main_image', 'thumbnail_image']
    path_list = []
    for column_name in column_list:
        path_list.append(settings.MEDIA_ROOT + '/' + str(instance.tracker.previous(column_name)))

    if os.path.isfile(path_list[0]) and instance.main_image == '':
        os.remove(path_list[0])

    if os.path.isfile(path_list[1]) and instance.thumbnail_image == '':
        os.remove(path_list[1])
