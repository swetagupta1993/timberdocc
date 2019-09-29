from library import BaseView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


class HomePage(BaseView):
    def get(self, request):
        return render(request, 'homepage/index.html')

    def post(self, request):
        return JsonResponse("ksydufguydshfbsdufgsdfyhsgdfuy7sdgvfhjgvf")
