from library import BaseView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

class Product(BaseView):
    def get(self, request):
        return render(request, 'product_upload.html')

    def post(self, request):
        file_name = "";
        i = 0;
        for file in request.FILES:
            i = i +1
            fileimg = request.FILES[file]
            fls = FileSystemStorage()
            ff = fls.save("UploadedFiles/"+fileimg.name, fileimg)
            file_name = file_name + "<br>" + str(i) + ") File Name :- " + fls.url(ff)
        return JsonResponse({'type':'success', 'data': file_name})