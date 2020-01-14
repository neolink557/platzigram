from django.contrib import admin
from posts.models import Posts
# Register your models here.

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user','profile','title','photo')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'title'
    )

    list_filter = (
    'created',
    'modified',
    'user__is_active',
    'user__is_staff'
    )

    fieldsets = (
        ('Post',{
            'fields':(('user','profile'),('title','photo')),
        }),

        ('Metadata',{
            'fields':(('created','modified'),),
        })
        )
    readonly_fields = ('created', 'modified')
