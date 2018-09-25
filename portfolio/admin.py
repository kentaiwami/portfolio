from django.contrib import admin
from .models import EngineerProduct, PhotographerProduct, Comment


class EngineerProductAdmin(admin.ModelAdmin):
    list_display = (
        'sort_id',
        'name',
        'alphabet_name',
        'short_concept',
        'feature_concept',
        'feature_detail',
        'background_concept',
        'background_detail',
        'development_environment',
        'development_language',
        'creation_time',
        'top_image',
        'col1_image',
        'col2_image',
        'col3_image',
        'github',
        'store'
    )

    fieldsets = (
        ('Product_main', {
            'fields': ('name',
                       'alphabet_name',
                       'short_concept',
                       'feature_concept',
                       'feature_detail',
                       'background_concept',
                       'background_detail',
                       'development_environment',
                       'development_language',
                       'creation_time',
                       )
        }),
        ('Image', {
            'fields': ('top_image', 'col1_image', 'col2_image', 'col3_image')
        }),
        ('Another', {
            'fields': ('github', 'store', 'sort_id')
        })
    )


class PhotographerProductAdmin(admin.ModelAdmin):
    list_display = ('sort_id', 'photographer_product_location', 'photographer_product_shooting_year',
                    'photographer_product_shooting_month', 'photographer_product_shooting_day',
                    'photographer_product_shooting_hour', 'photographer_product_shooting_minute',
                    'photographer_main_image', 'photographer_thumbnail_image'
                    )

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
    list_display = ('name', 'comment_text', 'pub_date', 'engineer_product')


admin.site.register(EngineerProduct, EngineerProductAdmin)
admin.site.register(PhotographerProduct, PhotographerProductAdmin)
admin.site.register(Comment, CommentAdmin)
