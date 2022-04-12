import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from ads.models import Ad, Category


# class AdDetailView_N(DetailView):
#
#     def get(self, request, *args, **kwargs):
#         ad = self.get_object()
#
#         return JsonResponse(200, {"status": "ok"})


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