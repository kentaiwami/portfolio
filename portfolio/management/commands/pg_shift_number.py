import os.path
from django.core.management.base import BaseCommand, CommandError
from portfolio.models import PhotographerProduct
from django.conf import settings


class Command(BaseCommand):
    help = 'Shift PhotographerProduct number'

    def add_arguments(self, parser):
        parser.add_argument('insert_sort_id', nargs='+', type=int)
        parser.add_argument('insert_count', nargs='+', type=int)

    def handle(self, *args, **options):

        if len(options['insert_sort_id']) == 1 and len(options['insert_count']) == 1:
            insert_sort_id = options['insert_sort_id'][0]
            insert_count = options['insert_count'][0]

            products = PhotographerProduct.objects.order_by('-sort_id')
            count = len(products)

            for product in products:
                if insert_sort_id < count:
                    new_number = product.sort_id + insert_count

                    # ファイルのリネーム処理
                    now_path_list = [product.photographer_main_image.path, product.photographer_thumbnail_image.path]
                    folder_list = ['main', 'thumbnail']
                    for i, folder in enumerate(folder_list):
                        title, ext = os.path.splitext(now_path_list[i])
                        new_path_images = 'images/p_work/' + folder + '/' + 'photo' + str(new_number) + '_' + folder + ext
                        new_path = settings.MEDIA_ROOT + '/' + new_path_images
                        os.rename(now_path_list[i], new_path)
                        print('now path: ' + now_path_list[i])
                        print('new path: ' + new_path)

                        if i == 0:
                            product.photographer_main_image = new_path_images
                            print('p_main: ' + new_path)
                        else:
                            product.photographer_thumbnail_image = new_path_images
                            print('p_thumbnail: ' + new_path)

                    # プロダクト名のリネーム処理
                    product.photographer_product_name = 'photo' + str(new_number)
                    product.photographer_product_alphabet_name = 'photo' + str(new_number)
                    print('photo' + str(new_number))

                    # sort_idのリネーム処理
                    product.sort_id = new_number

                    product.save()

                count -= 1
        else:
            raise CommandError('引数が異なります')
