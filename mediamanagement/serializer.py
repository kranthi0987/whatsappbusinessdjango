from rest_framework import serializers

from mediamanagement.models import MediaMessageModel, MediaFileModel


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaMessageModel
        fields = "__all__"


class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFileModel
        fields = "__all__"
