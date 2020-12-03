from rest_framework import serializers
from .models import WebUser, Track

class WebUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebUser
        fields = ('id', 'qr_code')

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'track_id', 'title', 'artist', 'picture_big', 'played', 'web_user_id')