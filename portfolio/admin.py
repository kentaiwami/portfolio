from django.contrib import admin
from .models import EngineerProduct, EngineerProductDetail, PhotographerProduct, Comment
# Register your models here.


class EngineerProductAdmin(admin.ModelAdmin):
    list_display = ('sort_id', 'engineer_product_name', 'engineer_product_alphabet_name',
                    'engineer_product_short_concept', 'top_image', 'col1_image',
                    'col2_image', 'col3_image', 'link', 'votes')

    fieldsets = (
        ('Product_main', {
            'fields': ('engineer_product_name', 'engineer_product_alphabet_name', 'engineer_product_short_concept')
        }),
        ('Image', {
            'fields': ('top_image', 'col1_image', 'col2_image', 'col3_image')
        }),
        ('Another', {
            'fields': ('link', 'votes', 'sort_id')
        })
    )


class EngineerProductDetailAdmin(admin.ModelAdmin):
    list_display = ('engineer_product', 'engineer_product_feature_concept',
                    'engineer_product_feature_detail', 'engineer_product_background_concept',
                    'engineer_product_background_detail', 'engineer_product_development_environment',
                    'engineer_product_development_language', 'engineer_product_creation_time')
    fieldsets = (
        ('Feature', {
            'fields': ('engineer_product_feature_concept', 'engineer_product_feature_detail')
        }),
        ('Background', {
            'fields': ('engineer_product_background_concept', 'engineer_product_background_detail')
        }),
        ('Another', {
            'fields': ('engineer_product_development_environment', 'engineer_product_development_language',
                       'engineer_product_creation_time')
        }),
        ('Relation', {
            'fields': ('engineer_product',)
        })
    )


class PhotographerProductAdmin(admin.ModelAdmin):
    list_display = ('sort_id', 'photographer_product_name', 'photographer_product_alphabet_name',
                    'photographer_main_image', 'photographer_thumbnail_image',
                    'photographer_product_location', 'photographer_product_shooting_year',
                    'photographer_product_shooting_month', 'photographer_product_shooting_day',
                    'photographer_product_shooting_hour', 'photographer_product_shooting_minute')

    fieldsets = (
        ('Product_main', {
            'fields': ('photographer_product_name', 'photographer_product_alphabet_name',
                       'sort_id', 'photographer_product_location')
        }),
        ('Image', {
            'fields': ('photographer_main_image', 'photographer_thumbnail_image')
        }),
        ('Daytime', {
            'fields': ('photographer_product_shooting_year', 'photographer_product_shooting_month',
                       'photographer_product_shooting_day', 'photographer_product_shooting_hour',
                       'photographer_product_shooting_minute')
        })
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'pub_date', 'engineer_product')


admin.site.register(EngineerProduct, EngineerProductAdmin)
admin.site.register(EngineerProductDetail, EngineerProductDetailAdmin)
admin.site.register(PhotographerProduct, PhotographerProductAdmin)
admin.site.register(Comment, CommentAdmin)
