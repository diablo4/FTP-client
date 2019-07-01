import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import ftplib
from django.conf import settings

ftp_address = '127.0.0.1'
ftp_port = 10002

id = 'uxfac'
pwd = '123456'


class download(View):
    def get(self, request, *args, **kwargs):
        ftp = ftplib.FTP()
        ftp.connect(ftp_address, ftp_port)

        path_arr = request.GET['path'].split('/')
        download_file = path_arr.pop()

        cwd_path = ''
        for p in path_arr:
            if p == '':
                cwd_path += '/'
            else:
                cwd_path += p + '/'

        print(cwd_path)
        ftp.login(id, pwd)
        ftp.cwd(cwd_path)
        reader = get_file(ftp, download_file)

        os.remove(download_file)
        # download(request, reader)

        # result = HttpResponse(file.read())
        # result['Content-Disposition'] = 'inline; filename' + os.path.basename('/')
        return downloaded(request, reader)
        # return render(request, 'download.html')

    def post(self, request, *args, **kwargs):
        ftp = ftplib.FTP()
        ftp.connect(ftp_address, ftp_port)
        ftp.login(id, pwd)

        return render(request, 'index.html')


def get_file(ftp, filename):
    try:
        m_get_file = open(filename, 'wb')
        ftp.retrbinary("RETR " + filename, m_get_file.write)
        m_read_file = open(filename, 'rb')
        m_get_file.close()

        return m_read_file

    except:
        print("File Download Error")


def downloaded(request, reader):
    response = HttpResponse(reader.read(), content_type="multipart/form-data")
    response['Content-Disposition'] = 'inline; filename=' + reader.name
    return response