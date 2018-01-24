from django.conf.urls import url
from apps.user import views

urlpatterns = [
    url(r'^user-add/(?P<id>\d+)/$', views.add, name='user-add'),
]


app_name = 'user'
