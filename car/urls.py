from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('provider/', views.RegisterProviderView.as_view(), name='provider_add'),
    path('buyer/', views.RegisterBuyerView.as_view(), name='buyer_add'),
    path('thanks/', views.thanks, name='thanks')
]
