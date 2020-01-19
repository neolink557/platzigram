from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not request.user.is_staff:
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('logout'), reverse('update_profile')]:
                        return redirect('update_profile')

        response = self.get_response(request)
        return response
