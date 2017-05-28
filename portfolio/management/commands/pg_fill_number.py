from django.core.management.base import BaseCommand
from portfolio.management.commands import functions
from portfolio.models import PhotographerProduct


class Command(BaseCommand):
    help = 'Fill PhotographerProduct number'

    def handle(self, *args, **options):
        products = PhotographerProduct.objects.order_by('sort_id')
        count = 1

        for i, product in enumerate(products):
            if product.sort_id != count:
                functions.renames(product, count)

            count += 1
