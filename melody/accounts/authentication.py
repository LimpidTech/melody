from django.contrib.auth import authenticate
from django.contrib.auth import login


def authenticate_and_login(request, username, password):
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)

    return user
