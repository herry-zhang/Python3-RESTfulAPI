from os import path
from django.apps import AppConfig

VERBOSE_APP_NAME = "用户管理"


def get_current_app_name(file):
    path_array = path.dirname(file).replace('\\', '/').split('/')
    return path_array[-2] + '.' + path_array[-1]


class AppVerboseNameConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME


default_app_config = get_current_app_name(
    __file__) + '.__init__.AppVerboseNameConfig'
