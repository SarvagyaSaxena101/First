from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# a function that take request and retruns a response mainly a Reequest handler

# def say_hello(request):
#     # pull data , tranform, etc
#     # return HttpResponse('Hello World')
#     # now we have to map this function to a url 
#     return render(request,'hello.html', { 'name': 'Sarvagya'})
#     # first parameter is the request and then the file and then the context

def index(request):
    Variables = {
        'Name':'Sarvagya'                   #input('Enter a name:')
    }
    return render(request,'index.html')
    # if u want to send a variable to the front then add it after the template file name
# def hi(request):
#     return HttpResponse('Hi from Sneha')


def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')

def submit_contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        # Add your logic here to handle the form data (e.g., save to database, send emails, etc.)

        return HttpResponse('Form submitted successfully')  # Adjust this response as needed

    return HttpResponse('Invalid form submission')  # Handle GET requests or other cases