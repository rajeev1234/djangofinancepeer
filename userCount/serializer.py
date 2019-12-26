from .models import Count
from rest_framework import serializers



class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields = ['people', 'gender']