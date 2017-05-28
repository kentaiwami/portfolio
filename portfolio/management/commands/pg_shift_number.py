from django.core.management.base import BaseCommand, CommandError
from portfolio.models import PhotographerProduct
from portfolio.management.commands import functions


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
                if insert_sort_id == 0:
                    new_number = product.sort_id + insert_count
                    functions.renames(product, new_number)
                else:
                    if insert_sort_id < count:
                        new_number = product.sort_id + insert_count
                        functions.renames(product, new_number)

                count -= 1
        else:
            raise CommandError('引数が異なります')
