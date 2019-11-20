import csv

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from mediamanagement.serializer import MediaSerializer, MediaFileSerializer
from whatsappbusiness.settings import Chat_api_sending_message, Chat_api_token, Chat_api_message

class MediaManageFileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = MediaSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            file_obj = request.FILES['file']
            decoded_file = file_obj.read().decode('utf-8')
            lines = decoded_file.split("\n")
            file_reader = csv.DictReader(file_obj, delimiter='\t')
            for line in lines:
                fields = line.split(",")
                data_dict = {}
                data_dict["sno"] = fields[0]
                # do something with row data.
                # print(row)
                # would print the rows like
                # I, like, to, ride, my, bicycle
                # I, like, to, ride, my, bike
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class ReadCsv(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        file_reader = csv.reader(file_obj, delimiter=',')
        for row in file_reader:
            # do something with row data.
            print(row)
            # would print the rows like
            # I, like, to, ride, my, bicycle
            # I, like, to, ride, my, bike


class MultimediaMessagesView(APIView):
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
