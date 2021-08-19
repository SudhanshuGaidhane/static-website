from django.urls import path
from .import views

urlpatterns = [
   path('',views.index,name='index'),
   path('about',views.about,name='about'),
   path('index2',views.index2,name='index2'),
   path('manu',views.manu,name='manu'),
   path('contact',views.contact,name='contact'),
   path('faq',views.faq,name='faq'),
   path('gallery',views.gallery,name='gallery'),
   path('blog-details',views.blog,name='blog-details'),
   path('blog-standard',views.blog,name='blog-standard'),
   path('restaurant-details',views.restaurant,name='restaurant-details'),
   path('restaurant',views.restaurant,name='restaurant'),
   path('team',views.team,name='team'),
]
