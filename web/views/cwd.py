from django.shortcuts import render
from django.views import View
import ftplib

ftp = ftplib.FTP()
ftp_address= '127.0.0.1'
ftp_port = 10002
id = 'uxfac'
pwd = '123456'


class cwd(View):

    def get(self, request, *args, **kwargs):
        path = request.GET['path']
        ftp.connect(ftp_address, ftp_port)
        ftp.login(id, pwd)

        current_path = ftp.cwd(path)
        data = []

        if current_path.split(" ")[0] == "250":
            ftp.dir(data.append)
            return render(request, 'index.html', {'data': data, 'path1': path})
        else:
            return render(request, 'main.html')

    def post(self, request, *args, **kwargs):

        return render(request, 'main.html')
