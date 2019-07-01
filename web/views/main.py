from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class Main(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')
        # return HttpResponse("Hello, world. You're at the polls index.")

    def post(self, request, *args, **kwargs):
        return render(request, 'main.html')
