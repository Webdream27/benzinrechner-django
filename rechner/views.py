from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms.forms import BenzinForm

def home_page_view(request):
    if request.method == "POST":
        form = BenzinForm(request.POST)
        if form.is_valid():
            template = loader.get_template("rechner/ergebnis.html")
            kilometer = form.cleaned_data["kilometer"]
            verbrauch = form.cleaned_data["verbrauch"]
            preis = form.cleaned_data["preis"]
            kosten = (kilometer / 100) * verbrauch * preis
            context = {"ergebnis": f"{kosten:.2f} €"}
            return HttpResponse(template.render(context, request))
    else:
        form = BenzinForm()
    return HttpResponse(render(request, "rechner/formular.html", {"form": form}))


