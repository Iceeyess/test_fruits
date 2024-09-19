from rest_framework import serializers

from fruits.models import Fruit


class FruitSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Fruit
        fields = ('id', 'name', 'owner', )