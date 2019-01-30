from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from graphene_django.views import GraphQLView
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from disyo.schema import schema
from disyo import views



router = routers.DefaultRouter()
router.register(r'dsapplications', views.UserViewSet)

schema_view = get_swagger_view(title='Disyo API')

urlpatterns = [
    url(r'^demo/$', schema_view),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    path(r'', include(router.urls)),
]
