import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from ftplib import FTP
from ..form import UploadFileForm

ftp_address = '127.0.0.1'
ftp_port = 10002

id = 'uxfac'
pwd = '123456'


class Upload(View):
    def get(self, request, *args, **kwagrs):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/success/url/')
        else:
            form = UploadFileForm()
        render(request, 'index.html', {'form': form})

    def post(self, request, *args, **kwargs):

        cwd_path = ''

        ftp = FTP()
        ftp.connect(ftp_address, ftp_port)
        ftp.login(id, pwd)

        if request.is_ajax():
            getPath = request.POST.get('getCurrentPath', '')
            # getPath = request.POST['getCurrentPath']
            print(getPath)

            path_arr = getPath.split(" ")

            for p in path_arr:
                if p == '':
                    cwd_path += '/'
                else:
                    cwd_path += p + '/'
            ftp.cwd(cwd_path)

            handle_uploaded_file(ftp, request.FILES['file'])

            print(cwd_path)
            return HttpResponse('202')
        else:
            print('fail')
            return HttpResponse('400')


def handle_uploaded_file(ftp, f):
    m_get_file = open(f.name, 'wb')
    for chunk in f.chunks():
        m_get_file.write(chunk)
        m_get_file.close()

    r_get_file = open(f.name, 'rb')
    ftp.storbinary("STOR " + r_get_file.name, r_get_file)

