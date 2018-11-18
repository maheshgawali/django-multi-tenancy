from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required


# @login_required
def loginView(request):
    # print('loginView request: %s' % request.__dict__)
    # return HttpResponse('Hello, World!')
    return HttpResponse('%s' % request.__dict__)
