from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Shorting
from .forms import URLForm

# from .forms import ValidateURLForm


# def index(request):
    # form = ValidateURLForm(request.POST)
    # context = {
    #     "form" : form
    # }
    # if form.is_valid():
    #     print(form.cleaned_data.get("url"))
    # return render(request, "urlshort/index.html", {})

def index(request):
    template = "urlshort/index.html"
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get("url_in"))
            new_url = form.cleaned_data.get("url_in")
            obj, created = Shorting.objects.get_or_create(url_in=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "urlshort/done.html"
            else:
                template = "urlshort/exists.html"
    else:
        form = URLForm()
        context = {'form': form, }
    return render(request, template, context)


def shorting_view(request, code=None):
    url = get_object_or_404(Shorting, code=code)
    return HttpResponseRedirect(url.url_in)


