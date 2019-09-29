from library import BaseView
from django.http import JsonResponse
from django.contrib.auth import logout

class Logout(BaseView):
    def get(self, request):
        try:
            logout(request)
            return JsonResponse({'type': 'success', 'data': 'Successfully Logged out'})
        except:
            return JsonResponse({'type': 'error', 'message': 'Problem in our server please try again'})

    def post(self, request):
        try:
            logout(request)
            return JsonResponse({'type': 'success', 'data': 'Successfully Logged out'})
        except:
            return JsonResponse({'type': 'error', 'message': 'Problem in our server please try again'})