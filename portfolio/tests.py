from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from .models import EngineerProduct
import os
import shutil
import copy


# Create your tests here.


def get_test_file():
    module_dir = os.path.dirname(__file__)
    test_file_path = os.path.join(module_dir, 'static', 'portfolio', 'img', 'profile.jpg')

    return SimpleUploadedFile(name='profile.jpg', content=open(test_file_path, 'rb').read(),
                              content_type='image/jpg')


def get_test_model():
    e_product = EngineerProduct()
    e_product.engineer_product_name = 'test'
    e_product.engineer_product_alphabet_name = 'test'
    e_product.engineer_product_short_concept = 'test concept'
    e_product.link = 'test link'
    e_product.sort_id = 1
    e_product.top_image = get_test_file()
    e_product.col1_image = get_test_file()
    e_product.col2_image = get_test_file()
    e_product.col3_image = get_test_file()

    return e_product


def delete_tmp_files():
    media_root_path = settings.MEDIA_ROOT + '/'
    shutil.rmtree(media_root_path + 'images/e_work/test')


def get_media_root_path():
    return settings.MEDIA_ROOT + '/'


class EngineerProductTests(TestCase):

    def test_engineer_product_image_save(self):
        e_product = get_test_model()
        e_product.save()

        # Equal uploaded file name and field value
        self.assertEquals(e_product.top_image, 'images/e_work/test/test_top.jpg')
        self.assertEquals(e_product.col1_image, 'images/e_work/test/test_col1.jpg')
        self.assertEquals(e_product.col2_image, 'images/e_work/test/test_col2.jpg')
        self.assertEquals(e_product.col3_image, 'images/e_work/test/test_col3.jpg')

        # Exist uploaded files and directory
        media_root_path = settings.MEDIA_ROOT + '/'
        self.assertEquals(os.path.exists(media_root_path + str(e_product.top_image)), True)
        self.assertEquals(os.path.exists(media_root_path + str(e_product.col1_image)), True)
        self.assertEquals(os.path.exists(media_root_path + str(e_product.col2_image)), True)
        self.assertEquals(os.path.exists(media_root_path + str(e_product.col3_image)), True)
        self.assertEquals(os.path.isdir(media_root_path + 'images/e_work/test'), True)

        delete_tmp_files()

    def test_engineer_product_image_change(self):
        # check image field clear and delete image file

        media_root_path = get_media_root_path()
        e_product = get_test_model()
        e_product.save()

        e_product_tmp = copy.deepcopy(e_product)

        top_tmp = e_product.top_image
        col1_tmp = e_product_tmp.col1_image
        col2_tmp = e_product_tmp.col2_image
        col3_tmp = e_product_tmp.col3_image

        e_product.top_image = ''
        e_product.col1_image = ''
        e_product.col2_image = ''
        e_product.col3_image = ''
        e_product.save()

        self.assertEquals(os.path.exists(media_root_path + str(top_tmp)), False)
        self.assertEquals(os.path.exists(media_root_path + str(col1_tmp)), False)
        self.assertEquals(os.path.exists(media_root_path + str(col2_tmp)), False)
        self.assertEquals(os.path.exists(media_root_path + str(col3_tmp)), False)

        delete_tmp_files()

    def test_engineer_product_delete(self):
        # check delete record when directory and image files
        media_root_path = get_media_root_path()
        e_product = get_test_model()
        e_product.save()

        e_product_tmp = copy.deepcopy(e_product)

        top_tmp = e_product_tmp.top_image
        col1_tmp = e_product_tmp.col1_image
        col2_tmp = e_product_tmp.col2_image
        col3_tmp = e_product_tmp.col3_image

        e_product.delete()

        self.assertEquals(os.path.exists(media_root_path + str(top_tmp)), False)
        self.assertEquals(os.path.exists(media_root_path + str(col1_tmp)), False)
        self.assertEquals(os.path.exists(media_root_path + str(col2_tmp)), False)
        self.assertEquals(os.path.exists(media_root_path + str(col3_tmp)), False)
        self.assertEquals(os.path.isdir(media_root_path + 'images/e_work/test'), False)

        delete_tmp_files()
