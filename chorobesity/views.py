from django.shortcuts import render
from .models import County, State
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CountySerializer, StateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class StateListViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    @action(detail=False)
    def flush(self, request):
        State.objects.all().delete()
        County.objects.all().delete()
        return Response("ok")

    def list(self, request):
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def retrieve(self, request, pk):
        counties = County.objects.filter(state=pk)
        serializer = CountySerializer(counties, many=True)
        return Response(serializer.data)

    def create(self, request):
        if len(request.query_params) > 0:
            serializer = CountySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            serializer = StateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response("ok")
