from django.urls import path

from messageprocess.views import BulkMessageProcessView, ListMessagesView, SingleMessageView, TextMessagesCount

urlpatterns = [
    path('bulkmessages/', BulkMessageProcessView.as_view()),
    path('singlemessage/',SingleMessageView.as_view()),
    path('listallmessages/',ListMessagesView.as_view()),
    path('messagecount/',TextMessagesCount.as_view())
]