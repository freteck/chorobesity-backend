from .models import County, State
from rest_framework import serializers

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"
    
class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = "__all__"