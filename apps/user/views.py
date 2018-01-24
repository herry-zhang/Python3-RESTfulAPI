"""
用户表
"""
from django.shortcuts import render_to_response
from apps.user.models import User


def add(request, id):
    """
    add
    """
    uid = id
    return render_to_response('user/user_add.html', locals())
