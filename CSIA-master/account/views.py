from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import JsonResponse


def login(request):
    if request.method== "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("user_home")
        else:
            respone = {"result": "permission denied"}

        return JsonResponse(respone)


def logout(request):
    auth.logout(request)
    return redirect("home")



