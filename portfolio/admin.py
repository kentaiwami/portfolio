from django.contrib import admin
from .models import Identifier, Product, ProductDetail, Comment, ImageFile
# Register your models here.


class IdentifierAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'product_short_concept', 'top_image', 'votes', 'identifier')


class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_feature_concept', 'product_feature_detail', 'product_background_concept', 'product_background_detail', 'product')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'pub_date', 'product')


class ImageFileAdmin(admin.ModelAdmin):
    fields = ('title', 'image')

admin.site.register(Identifier, IdentifierAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ImageFile, ImageFileAdmin)
