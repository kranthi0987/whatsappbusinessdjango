from django.urls import path

from mediamanagement.views import MediaFileUploadView, CollageMediaMessagesView, \
    MultimediaMessagesView, MultiMediaMessagesCount

urlpatterns = [
    # path('', MediaManageFileUploadView.as_view()),
    path('fileupload/', MediaFileUploadView.as_view()),
    path('multimediamessages/', MultimediaMessagesView.as_view()),
    path('collagemediamessages/', CollageMediaMessagesView.as_view()),
    path('messagecount/',MultiMediaMessagesCount.as_view()),
    # path('csv/', ReadCsv.as_view())
]
