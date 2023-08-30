from django.contrib import admin
from django.urls import path
from app import views
from app2 import views as view_app2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('app2/',view_app2.home)
]
