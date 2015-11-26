from django.http import HttpResponseRedirect as redirect
from django.shortcuts import render
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.core.urlresolvers import reverse
from profiles.forms import LoginForm, ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from profiles.models import Profile


def login(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                    username=form.cleaned_data["login"],
                    password=form.cleaned_data["password"]
            )
            if user is not None:
                auth_login(request, user)
                if "next" in request.GET:
                    return redirect(request.GET["next"])
                else:
                    return redirect(reverse("feed"))
            else:
                return render(request, "profiles/login.html", {"form": form,
                    "errors": ["User is not found."]})
        else:
            return render(request, "profiles/login.html", {"form": form})
    else:
        form = LoginForm()
        return render(request, "profiles/login.html", {"form": form})


@login_required(login_url="/login")
def logout(request):
    auth_logout(request)
    return redirect("/login")

@login_required(login_url="/login")
def settings(request):
    if request.method == "POST":
        p = Profile.objects.get(user=request.user)
        if p is None:
            p = Profile(user=request.user)

        form = ProfileForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect(reverse("settings"))
        else:
            return render(request, "profiles/settings.html", {"f": form})
    else:
        p = Profile.objects.get(user=request.user)
        if p is None:
            form = ProfileForm()
        else:
            form = ProfileForm(instance=p)
        return render(request, "profiles/settings.html", {"f": form})