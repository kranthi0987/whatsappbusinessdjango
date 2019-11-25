# Create your views here.
import csv

import pandas as pd
import requests
import urllib
from urllib.request import urlopen
from rest_framework import status, generics
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from contextlib import closing
import codecs
import json
from messageprocess.models import MessageProcessModel
from messageprocess.serializer import MessageSerializer, SendingMessageSerializer, BulkMessageSerializer
from whatsappbusiness.settings import Chat_api_sending_message, Chat_api_token, Chat_api_message, SERVER_URL


def SingleMessageSendingView(phone, body):
    global r
    # sending_message_serializer = SendingMessageSerializer(data=message_serializer.data)
    # if sending_message_serializer.is_valid():
    json_data = {'phone': phone, 'body': body}
    # print(json.dumps(json_data))
    # formdata = json.dumps(json_data)
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
            url = SERVER_URL + csvfile

            with closing(requests.get(url, stream=True)) as r:
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
        message_serializer = MessageSerializer(data=request.data)
        if message_serializer.is_valid():
            message_serializer.save()
            phone = request.data['phone']
            body = request.data['body']
            SingleMessageSendingView(phone, body)
            return Response(message_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListMessagesView(generics.ListCreateAPIView):
    queryset = MessageProcessModel.objects.all()
    serializer_class = MessageSerializer
