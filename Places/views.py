from django.shortcuts import render
from rest_framework.generics import CreateAPIView
# Create your views here.


class CreatePlaceAPIView(CreateAPIView):
    queryset = Places.objects.all()
    serializer_class = CreatePlaceSerializer

    def perform_create(self, serializer):
        serializer.save()