from django.http import HttpResponseRedirect as redirect
from django.shortcuts import render
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, UpdateView
from django.views.generic.edit import ModelFormMixin

from profiles.forms import LoginForm, ProfileForm



# Create your views here.
from profiles.models import Profile


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["login"],
                password=form.cleaned_data["password"]
            )
            if user is not None:
                auth_login(request, user)

                if "next" in request.GET:
                    redir = redirect(request.GET["next"])
                else:
                    redir = redirect(reverse("feed"))
                redir.set_cookie("who", user.username, max_age=24 * 60 * 60)
                return redir
            else:
                return render(request, "profiles/login.html", {"form": form,
                                                               "errors": ["User is not found."]})
        else:
            return render(request, "profiles/login.html", {"form": form})
    else:

        form = LoginForm()
        if "who" in request.COOKIES:
            # form = LoginForm(initial={"username": request.COOKIES["who"]})
            # form.fields["login"].initial = request.COOKIES["who"]
            form.fields["login"].initial = request.COOKIES["who"]
        return render(request, "profiles/login.html", {"form": form})


@login_required(login_url="/login")
def logout(request):
    auth_logout(request)
    return redirect("/login")


# @login_required(login_url="/login")
# def settings(request):
#     if request.method == "POST":
#         p = Profile.objects.get(user=request.user)
#         if p is None:
#             p = Profile(user=request.user)
#
#         form = ProfileForm(request.POST, request.FILES, instance=p)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("settings"))
#         else:
#             return render(request, "profiles/settings.html", {"f": form})
#     else:
#         p = Profile.objects.get(user=request.user)
#         if p is None:
#             form = ProfileForm()
#         else:
#             form = ProfileForm(instance=p)
#         return render(request, "profiles/settings.html", {"f": form})

# class SettingsView(FormView):
#     form_class = ProfileForm
#     template_name = "profiles/settings.html"
#
#     def get(self, request, *args, **kwargs):
#         p = Profile.objects.get(user=request.user)
#         if p is None:
#             form = self.form_class()
#         else:
#             form = self.form_class(instance=p)
#         return render(request, self.template_name, {"f": form})
#
#     def post(self, request, *args, **kwargs):
#         p = Profile.objects.get(user=request.user)
#         if p is None:
#             p = Profile(user=request.user)
#         form = self.form_class(request.POST, request.FILES, instance=p)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("settings"))
#         else:
#             return render(request, "profiles/settings.html", {"f": form})


class SettingsView(UpdateView):
    form_class = ProfileForm
    model = Profile
    template_name = "profiles/settings.html"
    success_url = reverse_lazy("settings")

    def get_object(self, queryset=None):
        return Profile.objects.get(user__username=self.request.user)
