from django.shortcuts import render
from .models import County
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CountySerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CountyViewSet(viewsets.ModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer

    @action(detail=False)
    def delete(self, request):
        County.objects.all().delete()
        return Response("ok")