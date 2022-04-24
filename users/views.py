import json

from django.conf import settings

from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from users.models import User, Location
from users.serializers import LocationSerializer, UserSerializer, UserCreateSerializer, UserUpdateSerializer, \
    UserDeleteSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserView(ListView):
    models = User
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.annotate(total_ads=Count('ad'))

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        users = []
        for user in page_obj:
            users.append({
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "second_name": user.second_name,
                "role": user.role,
                "age": user.age,
                "total_ads": user.total_ads,
                "locations": user.locations,
            })

        response = {
            "items": users,
            "nume_pages": page_obj.paginator.num_pages,
            "total": page_obj.paginator.count,
        }
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()

        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "second_name": user.second_name,
            "role": user.role,
            "age": user.age,
            "locations": list(map(str, user.locations.all())),
            })

@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ["username", "first_name", "second_name", "password", "role", "age", "locations"]


    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        user = User.objects.create(
            username=user_data["username"],
            password=user_data["password"],
            first_name=user_data["first_name"],
            second_name=user_data["second_name"],
            role=user_data["role"],
            age=user_data["age"],
        )

        for location_name in user_data["locations"]:
            location, _ = Location.objects.get_or_create(name=location_name)
            user.locations.add(location)

        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "second_name": user.second_name,
            "role": user.role,
            "age": user.age,
            "locations": list(map(str, user.locations.all())),
        })



@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ["username", "first_name", "second_name", "password", "role", "age", "locations"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)
        self.object.username = user_data["username"]
        self.object.first_name = user_data["first_name"]
        self.object.second_name = user_data["second_name"]
        self.object.password = user_data["password"]
        self.object.age = user_data["age"]

        for location_name in user_data["locations"]:
            location, _ = Location.objects.get_or_create(name=location_name)
            self.object.locations.add(location)

        self.object.save()
        return JsonResponse({
            "id": self.object.id,
            "username": self.object.username,
            "first_name": self.object.first_name,
            "second_name": self.object.second_name,
            "role": self.object.role,
            "age": self.object.age,
            "locations": list(map(str, self.object.locations.all())),
        })



@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


########################################

class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class UserViewSet(ListApiView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveApiView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(CreateApiView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserUpdateView(UpdateApiView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

class UserDeleteView(DestroyApiView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer



