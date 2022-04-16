import json

import pandas as pd
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from ads.models import Ad, Category

@method_decorator(csrf_exempt, name='dispatch')
class HelloView(DetailView):
    model = Ad
    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except Ad.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse(200, {"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        ads = Ad.objects.all()
        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
            })
        return JsonResponse(response, safe=False)


    def post(self, request):
        ad_data = json.loads(request.body)

        ad = Ad.objects.create(
            name=ad_data["name"],
            author=ad_data["author"],
            price=ad_data["price"],
            description=ad_data["description"],
            address=ad_data["address"],
            is_published=ad_data["is_published"],
        )
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "address": ad.address,
            "description": ad.description,
            "is_published": ad.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "address": ad.address,
            "is_published": ad.is_published,
        })

# перенос базы ads
class Ads_base(View):
    def get(self, request):
        data_ads = pd.read_csv('ads/db/ads.csv', sep=",").to_dict()

        i = 0

        while max(data_ads['Id'].keys()) >= i:
            print(data_ads['name'][i])
            ad = Ad.objects.create(
                name=data_ads["name"][i],
                author=data_ads["author"][i],
                price=data_ads["price"][i],
                description=data_ads["description"][i],
                address=data_ads["address"][i],
                is_published=data_ads["is_published"][i],
            )
            i += 1
        return JsonResponse("База есть", safe=False, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = []
        for categorie in categories:
            response.append({
                "id": categorie.id,
                "name": categorie.name,
            })
        return JsonResponse(response, safe=False)
#
    def post(self, request):
        categorie_data = json.loads(request.body)

        categorie = Category.objects.create(
            name=categorie_data["name"],
        )
        return JsonResponse({
            "id": categorie.id,
            "name": categorie.name,
        })

@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        categorie = self.get_object()

        return JsonResponse({
            "id": categorie.id,
            "name": categorie.name,
        })

# перенос базы Сategories
class Category_base(View):
    def get(self, request):
        data_categories = pd.read_csv('ads/db/categories.csv', sep=",").to_dict()

        i = 0

        while max(data_categories['id'].keys()) >= i:
            Category.objects.create(
                name=data_categories["name"][i],
            )
            i += 1
        return JsonResponse("База категории есть", safe=False, status=200)