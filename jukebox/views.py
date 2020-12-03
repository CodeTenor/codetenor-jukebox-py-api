from django.shortcuts import render
from rest_framework import viewsets
from .models import WebUser, Track
from .serializers import WebUserSerializer, TrackSerializer

class WebUserView(viewsets.ModelViewSet):
    queryset = WebUser.objects.all()
    serializer_class = WebUserSerializer

class TrackView(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    # def get_queryset(self):
    #     req = self.request
    #     qr_code = req.query_params.get('qr_code')

    #     if qr_code:
    #         self.queryset = Track.objects.filter(qr_code=qr_code)

    #     return self.queryset
