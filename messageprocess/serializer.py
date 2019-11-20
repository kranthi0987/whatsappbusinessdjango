from rest_framework import serializers

from messageprocess.models import MessageProcessModel, SendingMessageModel, ReadCsvFileModel


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageProcessModel
        fields = "__all__"


class SendingMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendingMessageModel
        fields = "__all__"


class BulkMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadCsvFileModel
        fields = "__all__"
