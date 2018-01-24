from django.conf.urls import url
from apis.api_v1.user import views as api_user
from apis.api_v1.scene import views as api_scene
from apis.api_v1.joined_scene import views as api_joined_scene
from apis.api_v1.my import views as api_my
from apis.api_v1.other import views as api_other

urlpatterns = [
    # user
    url(r'^user/$', api_user.user, name='user'),
]

app_name = 'api-v1'
