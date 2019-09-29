from library import BaseView
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

class Login(BaseView):
    def get(self, request):
        if(request.user.is_authenticated):
            return redirect('homepage')
        else:
            return render(request, 'login.html')

    def post(self, request):
        try:
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if (user):
                login(request, user)
                return JsonResponse({'type': 'success', 'data': 'Successfully received', 'user': user})
            else:
                return JsonResponse({'type': 'error', 'message': 'Username or password is wrong'})
        except:
            return JsonResponse({'type': 'error', 'message': 'Problem in our server please try again'})


