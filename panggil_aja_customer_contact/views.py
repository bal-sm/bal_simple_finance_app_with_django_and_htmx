from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

# Create your views here.


def create_contact_form(request):
    context = {}

    if request.method == "POST":
        form = ContactForm(request.POST or None)

        if form.is_valid():
            contact = form.save()
            context["contact"] = contact
            return render(request, "prefilled_partials/contact.html", context)

    else:
        form = ContactForm()
        context["form"] = form
        context["contacts"] = Contact.objects.all()

        if request.method == "GET" and request.GET.get("add-contact"):
            return render(request, "prefilled_partials/form.html", context)
        else:
            return render(request, "index.html", context)
