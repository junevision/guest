from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def event_manage(request):
    # username = request.COOKIES.get('user', '')  # get cookie
    username = request.session.get('user', '')  # get session from browser
    return render(request, "event_manage.html", {"user": username})


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600)  # add browser cookie
            request.session['user'] = username  # add session to browser
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})