from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('about/', views.about),
    # path('contact/', views.contact),
     path('', views.footer, name='footer'),
     path('<int:id>/', views.footer_detile, name='article_detile'),
]
