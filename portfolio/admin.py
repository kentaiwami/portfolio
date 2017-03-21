from django.contrib import admin
from .models import Identifier, Product, ProductDetail, Comment, ImageFile
# Register your models here.


class IdentifierAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sort_id', 'identifier', 'product_name', 'product_alphabet_name', 'product_short_concept',
                    'top_image', 'link', 'votes')


class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_feature_concept',
                    'product_feature_detail', 'product_background_concept',
                    'product_background_detail', 'product_development_environment',
                    'product_development_language', 'product_creation_time')
    fieldsets = (
        ('Feature', {
            'fields': ('product_feature_concept', 'product_feature_detail')
        }),
        ('Background', {
            'fields': ('product_background_concept', 'product_background_detail')
        }),
        ('Another', {
            'fields': ('product_development_environment', 'product_development_language', 'product_creation_time')
        }),
        ('Relation', {
            'fields': ('product',)
        })
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'pub_date', 'product')


class ImageFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'image')

admin.site.register(Identifier, IdentifierAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ImageFile, ImageFileAdmin)
