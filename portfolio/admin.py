from django.contrib import admin
from .models import Identifier, Product, Comment, ImageFile

# Register your models here.
# admin.site.register(Identifier)
# admin.site.register(Product)
# admin.site.register(Comment)


class IdentifierAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_short_concept', 'top_image', 'votes', 'identifier')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'pub_date', 'product')


class ImageFileAdmin(admin.ModelAdmin):
    fields = ('title', 'image')

admin.site.register(Identifier, IdentifierAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ImageFile, ImageFileAdmin)
