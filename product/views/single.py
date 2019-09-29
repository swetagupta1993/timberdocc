from library import BaseView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


class Single(BaseView):
    def get(self, request):
        return render(request, 'single.html')

    def post(self, request):
        return JsonResponse("ksydufguydshfbsdufgsdfyhsgdfuy7sdgvfhjgvf")
