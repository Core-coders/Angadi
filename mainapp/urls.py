from django.urls import path,include
# from .Views import site, provider
from . import views
from .Views import food,ration,user
from . import views

urlpatterns = [
    path('',views.Indexview, name="Home"),
    path('depot/dashboard/', views.depodashview),
    path('shop/dashboard/', views.shopdashview),
    path('accounts/', include('allauth.urls')),
    path('accounts/signup/user/',user.UserView, name = 'user_signup'),
    path('accounts/signup/ration/',ration.RationView, name='Ration_department_signup'),
    path('accounts/signup/depo/',food.FoodView, name='Food_department_signup'),
    # path('api/search/', views.EventAPIView),
    ]