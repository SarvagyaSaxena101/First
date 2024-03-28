from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FileUploadForm
import qrcode
from django.core.files.storage import default_storage
from stegano import lsb


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def submit_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        remember_me = request.POST.get('remember_me')

        # Add your logic here to handle the form data (e.g., save to database, send emails, etc.)

        return HttpResponse('Form submitted successfully')  # Adjust this response as needed

    return HttpResponse('Invalid form submission')  # Handle GET requests or other cases

def generate_qr(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            # Read file content
            content = file.read().decode('utf-8')  # Decode bytes to string

            # Generate QR code for the entire content
            qr = qrcode.make(content)

            # Save the QR code image temporarily
            with default_storage.open('temp_qr.png', 'wb') as f:
                qr.save(f)

            # Get the URL of the generated QR code image
            qr_code_url = default_storage.url('temp_qr.png')

            # Render the template with the QR code image URL
            return render(request, 'qr_code_single.html', {'qr_code_url': qr_code_url})
    else:
        form = FileUploadForm()
    return render(request, 'file_upload_form.html', {'form': form})  
