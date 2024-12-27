from django.urls import path
from . import views


urlpatterns = [
    path('h',views.home,name='add'),
    path('d/<int:pk>/',views.detail,name='detail'),
    path('search',views.search,name='search'),
    path('sign',views.sign,name='sign'),
    path('login',views.loginn,name='login'),
    path('',views.index,name='index'),
    path('u',views.usercar,name='usercar'),
    path('<int:category_id>/',views.home,name='categoryid'),
    path('delete/<int:delete_id>/',views.delete,name='delete'),

    
]