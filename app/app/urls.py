from django.contrib import admin
from django.urls import path
from disyo import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    url('hello/', views.hello),
]
