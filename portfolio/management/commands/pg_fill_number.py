import os.path
from django.core.management.base import BaseCommand, CommandError
from portfolio.models import PhotographerProduct
from django.conf import settings


class Command(BaseCommand):
    help = 'Fill PhotographerProduct number'

    def handle(self, *args, **options):
        products = PhotographerProduct.objects.order_by('sort_id')
        count = 1

        for i,product in enumerate(products):
            if product.sort_id != count:
                print(product)
                print(count)
                print('**********')
                # ファイルのリネーム処理
                now_path_list = [product.photographer_main_image.path, product.photographer_thumbnail_image.path]
                folder_list = ['main', 'thumbnail']
                for i, folder in enumerate(folder_list):
                    title, ext = os.path.splitext(now_path_list[i])
                    new_path_images = 'images/p_work/' + folder + '/' + 'photo' + str(count) + '_' + folder + ext
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
                product.photographer_product_name = 'photo' + str(count)
                product.photographer_product_alphabet_name = 'photo' + str(count)
                print('photo' + str(count))

                # sort_idのリネーム処理
                product.sort_id = count

                product.save()

            count += 1
