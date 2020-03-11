from rest_framework import serializers

from messageprocess.models import MessageProcessModel, SendingMessageModel, ReadCsvFileModel, MessageListModel


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


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageListModel
        fields = "__all__"
