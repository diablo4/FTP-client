from django.urls import path, re_path

from .views import file_to_ftp, main, login, cwd, download, upload
urlpatterns = [
    path('', main.Main.as_view(), name='index'),
    re_path(r'^ftp/', file_to_ftp.FTP.as_view(), name='ftp'),
    re_path(r'^login/', login.Login.as_view(), name='login'),
    re_path(r'^path/', cwd.cwd.as_view(), name='cwd'),
    re_path(r'^download/', download.download.as_view(), name='download'),
    re_path(r'^upload/', upload.Upload.as_view(), name='upload')
]