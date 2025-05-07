from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Send email and redirect
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "6df4342fcc-6a3e78@inbox.mailtrap.io",
                ["puetaso@hotmail.com"],
                reply_to=[email],
            )
            try:
                # All fine, redirect to OK
                email.send()
                return redirect(reverse('contact') + '?ok')
            except Exception as e:
                print("ERROR CON EL EMAIL: ", e)
                # Something went wrong, redirect to FAIL
                return redirect(reverse('contact') + '?fail')

    return render(request, 'contact/contact.html', {'contact_form': contact_form})
