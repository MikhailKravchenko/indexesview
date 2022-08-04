from django.urls import path

from .views import *

urlpatterns = [
    path('v1/refresh/', RefrashIndexes.as_view()),
    path('v1/price/', PriceDetailView.as_view()),
    path('v1/price/coin/<pk>/', PriceCoinDetailView.as_view()),
    path('v1/price/market/<pk>/', PriceMarketDetailView.as_view()),
    path('v1/price/market/<pk1>/coin/<pk2>/', PriceMarketCoinDetailView.as_view()),

]