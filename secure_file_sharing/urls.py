from django.urls import path, include
from django.shortcuts import redirect
from files.views import (
    UploadFileView, SignUpView, LoginView, ListFilesView, DownloadFileView, home
)


def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('', home, name='home'),  
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('upload/', UploadFileView.as_view(), name='upload'),
    path('files/', ListFilesView.as_view(), name='list_files'),
    path('files/<int:file_id>/download/', DownloadFileView.as_view(), name='download_file'),
]
