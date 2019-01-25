from django.contrib import admin
from django.urls import include, path
from disyo.schema import schema
from graphene_django.views import GraphQLView


urlpatterns = [
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]