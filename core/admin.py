from django.contrib import admin

from .models import Article, Category, Page, Media, Tag


class ArticleAdmin(admin.ModelAdmin):
    exclude = ('author',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_display = ('title', 'category', 'creation_date', 'pub_date',
                    'last_modified', 'status', 'is_public',
                    'protected_with_password', 'slug')
    list_filter = ('author', 'pub_date', 'status', 'category', 'tags')
    filter_horizontal = ('tags',)
    fieldsets = [
        ('Article info', {'fields': ['title', 'slug', 'content']}),
        ('Visibility', {'fields': ['is_public', 'status'],
                        'classes': ['collapse']}),
        ('Meta', {'fields': ['pub_date', 'allow_comments',
                             'protected_with_password', 'post_password'],
                  'classes': ['collapse']}),
        ('Taxonomy', {'fields': ['category', 'tags']})
    ]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(ArticleAdmin, self).save_model(request, obj, form, change)

    def post_url(self, obj):
        return obj.slug


class PageAdmin(admin.ModelAdmin):
    exclude = ('author',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_display = ('title', 'creation_date', 'pub_date', 'last_modified',
                    'status', 'is_public', 'protected_with_password', 'slug')
    list_filter = ('author', 'pub_date', 'status', 'tags')
    filter_horizontal = ('tags',)
    fieldsets = [
        ('Page info', {'fields': ['title', 'slug', 'content']}),
        ('Visibility', {'fields': ['is_public', 'status'],
                        'classes': ['collapse']}),
        ('Meta', {'fields': ['parent', 'pub_date', 'allow_comments',
                             'protected_with_password', 'post_password'],
                  'classes': ['collapse']}),
        ('Taxonomy', {'fields': ['tags']})
    ]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(PageAdmin, self).save_model(request, obj, form, change)

    def post_url(self, obj):
        return obj.slug


class MediaAdmin(admin.ModelAdmin):
    list_display = ('image_thumb', 'name', 'pub_date', 'media_file')
    list_display_links = ('image_thumb', 'name')
    list_filter = ('pub_date', 'last_modified')
    prepopulated_fields = {'name': ('media_file',)}
    fieldsets = [
        ('Media info', {'fields': ['name', 'media_file', 'content']}),
        ('Meta', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Tag, TagAdmin)
