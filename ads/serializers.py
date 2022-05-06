from rest_framework import serializers

from ads.models import Ad, Selection


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id"]


class AdDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id"]


class SelectionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = '__all__'


# class SelectionDetailSerializer(serializers.ModelSerializer):


class SelectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = '__all__'





