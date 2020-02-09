# Create your views here.
import csv

import pandas as pd
import requests
import urllib
from urllib.request import urlopen

from django.core import serializers
from django.http import QueryDict, JsonResponse
from rest_framework import status, generics
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from contextlib import closing
import codecs
import json
from messageprocess.models import MessageProcessModel, MessageCounter, MessageListModel
from messageprocess.serializer import MessageSerializer, SendingMessageSerializer, BulkMessageSerializer, \
    MessageListSerializer
from whatsappbusiness.settings import Chat_api_sending_message, Chat_api_token, Chat_api_message, SERVER_URL


def SingleMessageSendingView(phone, body):
    global r
    # sending_message_serializer = SendingMessageSerializer(data=message_serializer.data)
    # if sending_message_serializer.is_valid():
    json_data = {'phone': phone, 'body': body}
    # print(json.dumps(json_data))
    # formdata = json.dumps(json_data)
    listtt = dict({'from_whom': dddd["to_who"], 'to_whom': phone,
                   'body': body, 'message_type': 'Text',
                   'file_url': '', 'content_type': '',
                   'sent_status': True})
    query_dict = QueryDict('', mutable=True)
    query_dict.update(listtt)
    message_list_serializer = MessageListSerializer(data=query_dict)
    if (message_list_serializer.is_valid()):
        message_list_serializer.save()

    r = requests.post(Chat_api_sending_message + Chat_api_message + Chat_api_token,
                      json=json_data)
    if r.status_code == 200:
        print(r)
        return Response(r, status=status.HTTP_200_OK)
    else:
        return Response(r, status=status.HTTP_400_BAD_REQUEST)


def BulkMessagesSendingview(mobilenumber, message):
    global r
    # sending_message_serializer = SendingMessageSerializer(data=message_serializer.data)
    # if sending_message_serializer.is_valid():
    json_data = {'phone': mobilenumber, 'body': message}
    print(json.dumps(json_data))
    r = requests.post(Chat_api_sending_message + Chat_api_message + Chat_api_token,
                      data=json_data)
    if r.status_code == 200:
        print(r)
        return Response(r, status=status.HTTP_200_OK)
    else:
        return Response(r, status=status.HTTP_400_BAD_REQUEST)


class BulkMessageProcessView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['vcardfile']
        # file_reader = csv.reader(file_obj, delimiter=',')
        file_serializer = BulkMessageSerializer(data=request.data)
        # message_serializer = MessageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            responsedata = file_serializer.data
            csvfile = responsedata['vcardfile']
            # url = '/Volumes/work/whatsapp/whatsappbusinessdjango/media/excel.csv'
            url = SERVER_URL + csvfile.strip("/")
            print(url)
            with closing(requests.get(url, stream=True, verify=False)) as r:
                reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',')
                for row in reader:
                    # Handle each row here...
                    # if not row ==1:
                    mobile = row[2]
                    BulkMessagesSendingview(mobile, responsedata['body'])
            return Response(responsedata, status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleMessageView(APIView):

    def post(self, request, *args, **kwargs):
        dddd = request.data
        listtt = dict({'from_whom': dddd["to_who"], 'to_whom': 'dsdsda',
                       'body': 'dddd', 'message_type': 'gggg',
                       'file_url': 'gggg', 'content_type': 'ggg',
                       'sent_status': True})
        query_dict = QueryDict('', mutable=True)
        query_dict.update(listtt)
        message_list_serializer = MessageListSerializer(data=query_dict)
        if (message_list_serializer.is_valid()):
            message_list_serializer.save()

        message_serializer = MessageSerializer(data=request.data)
        if message_serializer.is_valid():
            message_serializer.save()
            phone = request.data['phone']
            body = request.data['body']
            # SingleMessageSendingView(phone, body)
            return Response(message_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ListMessagesView(APIView):
#     def get(self, request):
#         queryset = MessageListModel.objects.all()
#         # SomeModel_json = serializers.serialize("json", queryset)
#         serialized = json.dumps(queryset)
#         # message_list_serializer = MessageListSerializer(data=queryset)̥
#         return Response(serialized, status=status.HTTP_200_OK)

class ListMessagesView(generics.ListCreateAPIView):
    queryset = MessageListModel.objects.all()
            # filter(from_whom=request.data['from_whom'])
    serializer_class = MessageListSerializer



class TextMessagesCount(APIView):
    def get(self, request):
        Message_me = MessageListModel.objects.count()
        return Response({"messagecount": Message_me}, status=status.HTTP_200_OK)
