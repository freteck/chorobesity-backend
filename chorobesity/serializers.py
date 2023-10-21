from .models import County
from rest_framework import serializers

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = "__all__"