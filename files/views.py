from django.urls import path
from .import views  

from django.views.generic import View

from django.http import HttpResponse
from django.shortcuts import render

class SignUpView(View):
    def get(self, request):
        return render(request, 'signup.html')

class UploadFileView(View):
    def get(self, request):
        return render(request, 'upload.html')
    

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class ListFilesView(View):
    def get(self, request):
        return render(request, 'listfiles.html')
    

class DownloadFileView(View):
    def get(self, request):
        return render(request, 'download_file.html')
    


def home(request):
    return HttpResponse("<h1>Welcome to Secure File Sharing!</h1>")
 
urlpatterns = [
    path('', views.home, name='home'),  
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('upload/', views.UploadFileView.as_view(), name='upload'),
    path('files/', views.ListFilesView.as_view(), name='list_files'),
    path('files/<int:file_id>/download/', views.DownloadFileView.as_view(), name='download_file'),
]
