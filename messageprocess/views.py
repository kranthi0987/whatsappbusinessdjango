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
from whatsappbusiness.settings import Chat_api_sending_message, Chat_api_token, Chat_api_message


def my_django_view(message_serializer):
    global r
    sending_message_serializer = SendingMessageSerializer(data=message_serializer.data)
    if sending_message_serializer.is_valid():
        r = requests.post(Chat_api_sending_message + Chat_api_message + Chat_api_token,
                          data=sending_message_serializer.data)
        if r.status_code == 200:
            return Response(r, status=status.HTTP_200_OK)
    return Response(r, status=status.HTTP_400_BAD_REQUEST)


def BulkMessagesSendingview(mobilenumber, message):
    global r
    # sending_message_serializer = SendingMessageSerializer(data=message_serializer.data)
    # if sending_message_serializer.is_valid():
    json_data = {'phone': mobilenumber, 'body': message}
    print(json.dumps(json_data))
    r = requests.post(Chat_api_sending_message + Chat_api_message + Chat_api_token,
                      data=json.dumps(json_data))
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
            url = 'http://localhost:8000' + csvfile

            with closing(requests.get(url, stream=True)) as r:
                reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',')
                for row in reader:
                    # Handle each row here...
                    # if not row ==1:
                    mobile = row[2]
                    BulkMessagesSendingview(mobile,responsedata['body'])
                    # csv1 = pd.read_csv(url)
            # print(csv1.rows)
            # response = urlopen(url)
            # cr = csv.reader(csv1)
            #
            # for row in cr:
            #     print(row)

            # reader=csv.reader(open(url,'r'),delimiter=',')
            # for i,item in enumerate(reader,start=1):
            #     if not i == 1:
            #         print(item[2])

            # reader = csv.reader(open(url, 'rb'), delimiter=',')
            # fields = reader.next()
            # for item in reader:
            #     items = zip(fields, item)
            #     items_dict = {}
            #     items_dict = dict(items)
            #     mob = items_dict['mobile_number']
            #     print(mob)

            return Response(responsedata, status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleMessageView(APIView):

    def post(self, request, *args, **kwargs):
        message_serializer = MessageSerializer(data=request.data)
        if message_serializer.is_valid():
            message_serializer.save()
            my_django_view(message_serializer)
            return Response(message_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListMessagesView(generics.ListCreateAPIView):
    queryset = MessageProcessModel.objects.all()
    serializer_class = MessageSerializer
