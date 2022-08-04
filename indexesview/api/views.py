# -*- coding: utf-8 -*-
from django.http import JsonResponse
from rest_framework import generics

from rest_framework.views import APIView

from .models import Price
from .serialezers import PriceListSerializer
from .services import GetIndexes, ParsePrice



class RefrashIndexes(APIView):
    def get(self, request):
        url = 'https://api.coingecko.com/api/v3/indexes?per_page=250'
        get_indexes = GetIndexes()
        get_indexes.get_max_number_page(url)
        get_indexes.parse_index(url, False)
        parse_price = ParsePrice(get_indexes.get_ptice())
        parse_price.parse_price_and_write_to_db()
        response_json = JsonResponse({
            'success': True,
        })
        response_json.status_code = 400
        return response_json


class PriceDetailView(generics.ListAPIView):

    queryset = Price.objects.all().order_by('name_coin')
    serializer_class = PriceListSerializer


class PriceCoinDetailView(generics.ListAPIView):

    queryset = Price.objects.all().order_by('name_coin')
    serializer_class = PriceListSerializer

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Price.objects.none()
        queryset = self.queryset.filter(
            name_coin=self.kwargs['pk']
        )
        return queryset


class PriceMarketDetailView(generics.ListAPIView):

    queryset = Price.objects.all().order_by('name_coin')
    serializer_class = PriceListSerializer

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Price.objects.none()
        queryset = self.queryset.filter(
            market=self.kwargs['pk']
        )
        return queryset


class PriceMarketCoinDetailView(generics.ListAPIView):

    queryset = Price.objects.all().order_by('name_coin')
    serializer_class = PriceListSerializer

    def get_queryset(self):
        """Запрос деталей документа по номеру документа"""
        if getattr(self, "swagger_fake_view", False):
            return Price.objects.none()
        queryset = self.queryset.filter(
            market=self.kwargs['pk1'],
            name_coin=self.kwargs['pk2']
        )
        return queryset
