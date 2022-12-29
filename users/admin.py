from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('last_name', 'first_name', 'email', 'is_staff', 'is_active',)
    list_display_links = ('email',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        ('Информация', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'date_joined', 'photo', 'show_photo')}),
        ('Права доступа', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff',
                       'is_active')}
         ),
    )
    search_fields = ('last_name',)
    ordering = ('last_name',)
    readonly_fields = ('show_photo', 'date_joined')


admin.site.register(User, CustomUserAdmin)
