"""
用户模块
"""
from django.contrib import admin
from apps.user.models import User

class UserAdmin(admin.ModelAdmin):
    """
    用户表
    """
    list_display = ('user_id', 'user_name', 'real_name', 'avatar', 'mobile',
                    'balance', 'available_balance', 'frozen_balance')
    search_fields = ('user_name', 'mobile')

admin.site.register(User, UserAdmin)
