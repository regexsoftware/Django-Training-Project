from rest_framework import serializers
from .models import Zomato

class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class filters(serializers.ModelSerializer):
    Cuisines = StringSerializer(many=False)

    class Meta:
        model = Zomato
        fields = ('__all__')