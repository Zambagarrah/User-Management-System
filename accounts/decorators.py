from django.shortcuts import redirect
from functools import wraps

def verified_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.profile.is_verified:
            return view_func(request, *args, **kwargs)
        return redirect('verify_code')
    return wrapper
