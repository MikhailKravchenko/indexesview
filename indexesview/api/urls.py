from django.urls import path

from .views import *

urlpatterns = [
    path('v1/refresh/', RefrashIndexes.as_view()),
    path('v1/price/', PriceDetailView.as_view()),
    path('v1/price/coin/str:<pk1>/', PriceCoinDetailView.as_view()),
    path('v1/price/market/str:<pk1>/', PriceMarketDetailView.as_view()),
    path('v1/price/market/str:<pk1>/coin/str:<pk2>/', PriceMarketCoinDetailView.as_view()),

]