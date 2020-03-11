from django.urls import path

from uploadmedia.views import FileUploadView

urlpatterns = [
    path('', FileUploadView.as_view())
]