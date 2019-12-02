import codecs
import csv
import json
from contextlib import closing

import requests
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from mediamanagement.models import MediaMessageModel
from mediamanagement.serializer import MediaSerializer, MediaFileSerializer
from whatsappbusiness.settings import Chat_api_sending_message, Chat_api_token, Chat_api_message, Chat_api_media, \
    SERVER_URL


def MediaMessageSendingView(mobilenumber, message, filename, caption):
    global r
    # sending_message_serializer = SendingMessageSerializer(data=message_serializer.data)
    # if sending_message_serializer.is_valid():

    json_data = {'phone': mobilenumber, 'body': message, 'filename': filename, 'caption': caption}
    print(json.dumps(json_data))
    r = requests.post(Chat_api_sending_message + Chat_api_media + Chat_api_token,
                      data=json_data)
    if r.status_code == 200:
        print(r)
        return Response(r, status=status.HTTP_200_OK)
    else:
        return Response(r, status=status.HTTP_400_BAD_REQUEST)


# class MediaManageFileUploadView(APIView):
#     parser_class = (FileUploadParser,)
#
#     def post(self, request, *args, **kwargs):
#         file_serializer = MediaSerializer(data=request.data)
#         if file_serializer.is_valid():
#             file_serializer.save()
#             file_obj = request.FILES['file']
#             decoded_file = file_obj.read().decode('utf-8')
#             lines = decoded_file.split("\n")
#             file_reader = csv.DictReader(file_obj, delimiter='\t')
#             for line in lines:
#                 fields = line.split(",")
#                 data_dict = {}
#                 data_dict["sno"] = fields[0]
#                 # do something with row data.
#                 # print(row)
#                 # would print the rows like
#                 # I, like, to, ride, my, bicycle
#                 # I, like, to, ride, my, bike
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MediaFileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = MediaFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            responsedata = file_serializer.data
            return Response(responsedata, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        file_serializer = MediaFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            responsedata = file_serializer.data
            return Response(responsedata, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ReadCsv(APIView):
#     # this is not used
#     parser_classes = (FileUploadParser,)
#
#     def post(self, request, *args, **kwargs):
#         file_obj = request.FILES['file']
#         file_reader = csv.reader(file_obj, delimiter=',')
#         for row in file_reader:
#             # do something with row data.
#             print(row)
#             # would print the rows like
#             # I, like, to, ride, my, bicycle
#             # I, like, to, ride, my, bike


def BulkMediaMessagesSendingview(phone, fileurl, filename, caption):
    global r
    # sending_message_serializer = SendingMessageSerializer(data=message_serializer.data)
    # if sending_message_serializer.is_valid():
    json_data = {'phone': phone, 'body': fileurl, 'filename': filename, 'caption': caption}
    print(json.dumps(json_data))
    r = requests.post(Chat_api_sending_message + Chat_api_media + Chat_api_token,
                      data=json_data)
    if r.status_code == 200:
        print(r)
        return Response(r, status=status.HTTP_200_OK)
    elif r.status_code == 500:
        return Response(r,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(r, status=status.HTTP_400_BAD_REQUEST)


class MultimediaMessagesView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = MediaSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            responsedata = file_serializer.data
            csvfile = responsedata['vcardfile']
            # url = '/Volumes/work/whatsapp/whatsappbusinessdjango/media/excel.csv'
            url = SERVER_URL + csvfile.strip("/")

            with closing(requests.get(url, stream=True)) as r:
                reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',')
                for row in reader:
                    # Handle each row here...
                    # if not row ==1:
                    mobile = row[2]
                    BulkMediaMessagesSendingview(mobile, responsedata['body'], responsedata['filename'],
                                                 responsedata['caption'])

            return Response(responsedata, status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        file_serializer = MediaFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            responsedata = file_serializer.data
            return Response(responsedata, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollageMediaMessagesView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = MediaFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            responsedata = file_serializer.data
            return Response(responsedata, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        file_serializer = MediaFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            responsedata = file_serializer.data
            return Response(responsedata, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MultiMediaMessagesCount(APIView):
    def get(self,request):
        Message_me = MediaMessageModel.objects.count()
        return Response({"messagecount": Message_me}, status=status.HTTP_200_OK)
