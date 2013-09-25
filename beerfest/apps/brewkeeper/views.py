from django.contrib.auth.decorators import login_required

from annoying.decorators import render_to, ajax_request


@render_to('brewkeeper/home.html')
def home(request):
    return locals()
