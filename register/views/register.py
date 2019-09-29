from library import BaseView
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from ..models import UserDetail


class Register(BaseView):
    def get(self, request):
            return render(request, 'register.html')

    def post(self, request):
        try:
            user=User.objects.create_user(username=request.POST.get('username'),email=request.POST.get('email'),password=request.POST.get('password'))
            user.first_name=request.POST.get('first_name')
            user.last_name=request.POST.get('last_name')
            user.save()
            detail=UserDetail.objects.create(mobile_number=request.POST.get('mobile_number'), user_id=user.id)
            detail.save()
            arr = {'type': 'success', 'data': "saved", 'user': user}
            return JsonResponse(arr)

        except Exception as e:
            arr = {'type': 'error', 'message': request.POST.get('email')}
            return JsonResponse(arr)

