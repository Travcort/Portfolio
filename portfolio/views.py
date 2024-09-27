from django.shortcuts import render, redirect
from django.core.mail import send_mail

def home(request):
    return render(request, 'portfolio/index.html')

# Still to be completed
def send_email(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f'Full Name: {fullname}\nEmail: {email}\nSubject: \n{subject}\nMessage: \n{message}'

        send_mail(
            subject = subject,
            message = full_message,
            from_email = 'no-reply@mywebsite.com',
            recipient_list = ['myemail@gmail.com']
        )

        return redirect('success-page')
    
    return render(request, 'portfolio/index.html')
