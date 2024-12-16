from django.shortcuts import redirect

class RedirectUnauthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/classes/') and not request.user.is_authenticated:
            return redirect('/')  # Redirect to home if unauthenticated
        return self.get_response(request)
