from library import BaseView
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login


class SocialLogin(BaseView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return render(request, 'social.html')

    def post(self, request):
        try:
            return JsonResponse({'type': 'success', 'data': 'Successfully received'})
        except:
            return JsonResponse({'type': 'error', 'message': 'Problem in our server please try again'})
