from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login, name="login"),
    path('query',views.query,name="query"),
    path('edit/<int:x>',views.edit,name="edit"),

    
    # path('first/',views.first,name="first"),
    # path('last',views.last,name="last"),
    # path('lastest',views.lastest,name="lastest"),
    # path('all_details',views.all_details,name="all_details"),
    # path('filter',views.filter,name="filter"),
    # path('exclude', views.exclude,name='exclude'),
    # path('order',views.order,name="order"),
    # path('dis_order',views.dis_order,name="dis_order"),
    # path('slice',views.slice,name="slice")

]
