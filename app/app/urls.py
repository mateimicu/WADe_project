from django.urls import include, path
from disyo import views
from django.conf.urls import url

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view


router = routers.DefaultRouter()
router.register(r'dsapplications', views.UserViewSet)

schema_view = get_swagger_view(title='Disyo API')

urlpatterns = [
    url(r'^api-demo/$', schema_view),
    path(r'api/', include(router.urls)),
]
