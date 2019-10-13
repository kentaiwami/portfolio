from django.contrib import admin
from .models import EngineerProduct, PhotographerProduct, Comment, PrivacyPolicy, Contact


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
    list_display = (
        'sort_id',
        'location',
        'shooting_date',
        'main_image',
        'thumbnail_image'
    )

    fieldsets = (
        ('Product_main', {
            'fields': ('name', 'alphabet_name',
                       'sort_id', 'location')
        }),
        ('Image', {
            'fields': ('main_image', 'thumbnail_image')
        }),
        ('Daytime', {
            'fields': ('shooting_date',)
        })
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'pub_date', 'engineer_product')


class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('sort_id', 'information', 'usage', 'updated_at', 'engineer_product')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'content', 'created_at')


admin.site.register(EngineerProduct, EngineerProductAdmin)
admin.site.register(PhotographerProduct, PhotographerProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
admin.site.register(Contact, ContactAdmin)
