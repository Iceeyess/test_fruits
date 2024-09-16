from rest_framework import serializers

from fruits.models import Fruit


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ('name', )