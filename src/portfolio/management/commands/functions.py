import os.path
from django.conf import settings


def renames(product, new_number):
    print('*********************')
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
    print('*********************')
