from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

# Create your views here.


def index(request):
    context = {
        "form": ContactForm(),
        "contacts": Contact.objects.all(),
    }
    return render(request, "index.html", context)


def create_contact_form(request):
    context = {}

    if request.method == "POST":
        form = ContactForm(request.POST or None)

        if form.is_valid():
            contact = form.save()
            context["contact"] = contact
            return render(request, "prefilled_partials/contact.html", context)

    elif request.method == "GET" and request.GET.get("add-contact"):
        form = ContactForm()
        context["form"] = form
        return render(request, "prefilled_partials/form.html", context)

    else:
        raise (ValueError("Invalid request method"))
