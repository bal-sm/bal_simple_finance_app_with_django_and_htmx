from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

# Create your views here.


def index(request):
    context = {"form": ContactForm()}
    return render(request, "index.html", context)


def create_contact_form(request):
    context = {}

    if request.method == "POST":
        pass

    return render(request, "partials/form.html", context)
