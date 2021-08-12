# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from cis_app.tasks import create_users, send_mail_to_all_users
from cis_app.forms import UserForm, EmailForm

def create_users_view(request):
    '''Create Users View'''
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            number_of_users = request.POST.get('number_of_users')
            create_users.delay(number_of_users)
            return HttpResponse("Request for creating users has been accepted")
        else:
            return HttpResponse("Please enter a valid integer")
    else:
         user_form = UserForm()
         return render(request, 'userform.html', {'user_form': user_form })
            
def send_email_view(request):
    '''Send Emails View'''
    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            email_data = {
                "mail_subject":  request.POST.get("mail_subject"),
                "message": request.POST.get('message')
            }
            send_mail_to_all_users.delay(email_data)
            return HttpResponse("Request for sending mail has been accepted")
        else:
            return HttpResponse("Please enter valid input")
    else:
         email_form = EmailForm()
         return render(request, 'sendmail.html', {'email_form': email_form })

def home(request):
    '''Home page view'''
    return render(request, 'home.html')

