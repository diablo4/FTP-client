from django.shortcuts import render
from django.views import View
import ftplib

from ..form import UploadFileForm

ftp_address = '127.0.0.1'
ftp_port = 10002
ftp = ftplib.FTP()


class Login(View):

    def get(self, request, *args, **kwargs):

        print('login')
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):

        id = request.POST.get('id')
        pw = request.POST.get('pw')

        ftp.connect(ftp_address, ftp_port)
        login_check = ftp.login(id, pw)
        print(ftp.pwd())
        data = []
        if login_check == '230 welcome.':
            data = []
            ftp.dir(data.append)
            form = UploadFileForm()
            return render(request, 'index.html', {'data': data}, {'form', form})
        else:
            return render(request, 'login.html')
