from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.get_index,name = 'index'),
    path('about/', views.about,name = 'about'),
    path('elements/', views.elements,name = 'elements'),
    path('contact/', views.contact,name = 'contact'),
    path('single-blog/', views.single_blog,name = 'single_blog'),
    path('blog/', views.blog,name = 'blog'),
    
]