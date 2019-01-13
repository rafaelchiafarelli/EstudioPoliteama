from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# Create your views here.
def homepage(request):
    if request.method == 'POST':
        if request.POST.get('email') is not None:
            if request.POST.get('name') is not None:
                if request.POST.get('message') is not None:
                    email = EmailMessage(
                                'Mensage de ' + request.POST.get('email') + 'enviado pelo site', 
                                request.POST.get('message'), to=['rafael.chiafarelli@gmail.com']
                    )
                    email.send()

    return render(request, 'homepage/index.html')