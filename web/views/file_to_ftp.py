from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
import ftplib
from ..form import UploadFileForm

import os
from django_ftpserver.utils import make_server

ftp_server_ip = '127.0.0.1'
ftp_server_port = 10002

user = 'uxfac'
pw = '123456'


class FTP(View):
    def get(self, request, *args, **kwargs):
        ftp = ftplib.FTP()
        ftp.connect(ftp_server_ip, ftp_server_port)
        ftp.login(user, pw)

        ftp = ftplib.FTP()
        data = []
        path = ftp.pwd()
        ftp.dir(data.append)
        print('what?')
        print(path)
        ftp.quit()

        for line in data:
            print(line)

        form = UploadFileForm()
        return render(request, 'index.html', {'data': data, 'path1': path, 'form': form})

    def post(self, request, *args, **kwargs):
        return render(request, 'index.html')
