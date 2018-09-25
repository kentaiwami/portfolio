from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.urls import reverse
from .models import EngineerProduct, PhotographerProduct
from .forms import CommentForm
import os
import shutil
import copy


def get_test_file():
    module_dir = os.path.dirname(__file__)
    test_file_path = os.path.join(module_dir, 'static', 'portfolio', 'img', 'profile.jpg')

    return SimpleUploadedFile(name='profile.jpg', content=open(test_file_path, 'rb').read(),
                              content_type='image/jpg')


def get_engineer_product_test_model():
    e_product = EngineerProduct()
    e_product.name = 'test'
    e_product.alphabet_name = 'test'
    e_product.short_concept = 'test concept'
    e_product.link = 'test link'
    e_product.sort_id = 1
    e_product.top_image = get_test_file()
    e_product.col1_image = get_test_file()
    e_product.col2_image = get_test_file()
    e_product.col3_image = get_test_file()

    return e_product


def get_photographer_product_test_model():
    p_product = PhotographerProduct()
    p_product.photographer_product_name = 'test'
    p_product.photographer_product_alphabet_name = 'test'
    p_product.photographer_main_image = get_test_file()
    p_product.photographer_thumbnail_image = get_test_file()
    p_product.sort_id = 1

    return p_product


def delete_e_work_tmp_files():
    media_root_path = settings.MEDIA_ROOT
    path = '/'.join([media_root_path, 'images', 'e_work', 'test'])
    shutil.rmtree(path)


def delete_p_work_tmp_files(image_type, file_name):
    media_root_path = settings.MEDIA_ROOT
    path = '/'.join([media_root_path, 'images',  'p_work', image_type, file_name])
    os.remove(path)


class EngineerProductTests(TestCase):

    def test_engineer_product_image_save(self):
        e_product = get_engineer_product_test_model()
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

        delete_e_work_tmp_files()

    def test_engineer_product_image_change(self):
        # check image field clear and delete image file
        media_root_path = settings.MEDIA_ROOT + '/'
        e_product = get_engineer_product_test_model()
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

        delete_e_work_tmp_files()

    def test_engineer_product_delete(self):
        # check delete record when directory and image files
        media_root_path = settings.MEDIA_ROOT + '/'
        e_product = get_engineer_product_test_model()
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


class PhotographerProductTests(TestCase):

    def test_photographer_product_image_save(self):
        media_root_path = settings.MEDIA_ROOT + '/'
        p_product = get_photographer_product_test_model()
        p_product.save()

        # Equal uploaded file name and field value
        self.assertEquals(p_product.photographer_main_image, 'images/p_work/main/test_main.jpg')
        self.assertEquals(p_product.photographer_thumbnail_image, 'images/p_work/thumbnail/test_thumbnail.jpg')

        # Exist uploaded files and directory
        self.assertEquals(os.path.exists(media_root_path + str(p_product.photographer_main_image)), True)
        self.assertEquals(os.path.exists(media_root_path + str(p_product.photographer_thumbnail_image)), True)

        delete_p_work_tmp_files('main', 'test_main.jpg')
        delete_p_work_tmp_files('thumbnail', 'test_thumbnail.jpg')

    def test_photographer_product_image_change(self):
        # check image field clear and delete image file
        media_root_path = settings.MEDIA_ROOT + '/'
        p_product = get_photographer_product_test_model()
        p_product.save()

        p_product_tmp = copy.deepcopy(p_product)

        main_tmp = p_product_tmp.photographer_main_image
        thumbnail_tmp = p_product_tmp.photographer_thumbnail_image

        p_product.photographer_main_image = ''
        p_product.photographer_thumbnail_image = ''
        p_product.save()

        self.assertEquals(os.path.exists(media_root_path + str(main_tmp)), False)
        self.assertEquals(os.path.exists(media_root_path + str(thumbnail_tmp)), False)

    def test_photographer_product_delete(self):
        # check delete record when directory and image files
        media_root_path = settings.MEDIA_ROOT + '/'
        p_product = get_photographer_product_test_model()
        p_product.save()

        p_product_tmp = copy.deepcopy(p_product)

        main_tmp = p_product_tmp.photographer_main_image
        thumbnail_tmp = p_product_tmp.photographer_thumbnail_image

        p_product.delete()

        self.assertEquals(os.path.exists(media_root_path + str(main_tmp)), False)
        self.assertEquals(os.path.exists(media_root_path + str(thumbnail_tmp)), False)


class CommentFormTests(TestCase):

    def test_comment_form_data_validation(self):
        # check form data
        form_data1 = {'name': 'test name',
                      'comment_text': 'test comment',
                      'id': 1}
        form_data2 = {'name': '',
                      'comment_text': 'test comment',
                      'id': 1}
        form_data3 = {'name': 'test name',
                      'comment_text': '',
                      'id': 1}
        form_data4 = {'name': '',
                      'comment_text': '',
                      'id': 1}
        form_list = [form_data1, form_data2, form_data3, form_data4]
        expect_form_validation_list = [True, True, False, False]

        for i, form_data in enumerate(form_list):
            form = CommentForm(form_data)
            self.assertEquals(form.is_valid(), expect_form_validation_list[i])

    def test_comment_form_data_submit(self):
        # OK submit pattern
        e_product = get_engineer_product_test_model()
        e_product.save()

        c = Client()
        response = c.post(reverse('portfolio:get_comment'), {'name': '*', 'comment_text': 'test', 'id': 1})
        self.assertRedirects(response, expected_url=reverse('portfolio:thanks'))

        # NG submit pattern
        response = c.post(reverse('portfolio:get_comment'), {'name': '*', 'comment_text': '', 'id': 1})
        self.assertTemplateUsed(response, 'portfolio/form_error.html')

        delete_e_work_tmp_files()


class ErrorTests(TestCase):

    def test_engineer_work_detail_error(self):
        # product not found
        c = Client()
        response = c.get(reverse('portfolio:engineer_work_detail', args=[1]))
        self.assertEquals(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html', 'error_base.html')

        # product found
        e_product = get_engineer_product_test_model()
        e_product.save()
        response = c.get(reverse('portfolio:engineer_work_detail', args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/engineer_work_detail.html')

        delete_e_work_tmp_files()

    def test_engineer_works_all_error(self):
        c = Client()
        response = c.get('/portfolio/engineer_works_all')
        self.assertEquals(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html', 'error_base.html')


class URLconfTests(TestCase):

    def test_urlconfs(self):
        # view index
        url = reverse('portfolio:index')
        self.assertEqual(url, '/portfolio/')

        # view engineer_work_detail
        e_product = get_engineer_product_test_model()
        e_product.save()
        url = reverse('portfolio:engineer_work_detail', args=[1])
        self.assertEqual(url, '/portfolio/1/')
        delete_e_work_tmp_files()

        # view photographer_all
        url = reverse('portfolio:all_photographer_works')
        self.assertEquals(url, '/portfolio/all_photographer_works/')

        # view get_comment
        url = reverse('portfolio:get_comment')
        self.assertEquals(url, '/portfolio/get_comment/')

        # view thanks
        url = reverse('portfolio:thanks')
        self.assertEquals(url, '/portfolio/thanks/')
