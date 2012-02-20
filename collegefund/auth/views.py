from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf

def login_user(request):
    state = 'Please log in below...'
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active."
        else:
            state = 'Your username and/or password were incorrect'

    data = {'state': state,
            'username': username}
    data.update(csrf(request))
    return render_to_response('login.html', 
            data,
            context_instance = RequestContext(request))
