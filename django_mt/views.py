from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required


@login_required
def loginView(request):
    return HttpResponse('Hello, World!')
