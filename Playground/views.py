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

import qrcode
from django.core.files.storage import default_storage
from django.shortcuts import render
from .forms import FileUploadForm

def generate_qr(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            # Read file content
            content = file.read()

            # Define the maximum capacity of a single QR code (adjust as needed)
            max_capacity = 2000

            # Check if content exceeds the maximum capacity
            if len(content) > max_capacity:
                # Split the content into chunks
                chunks = [content[i:i+max_capacity] for i in range(0, len(content), max_capacity)]
                qr_code_urls = []

                # Generate QR codes for each chunk
                for idx, chunk in enumerate(chunks):
                    qr = qrcode.make(chunk, version=10)  # Adjust the version as needed
                    # Save the QR code image temporarily
                    with default_storage.open(f'temp_qr_{idx}.png', 'wb') as f:
                        qr.save(f)
                    qr_code_urls.append(default_storage.url(f'temp_qr_{idx}.png'))

                # Render the template with QR code image URLs
                return render(request, 'qr_code_multi.html', {'qr_code_urls': qr_code_urls})
            else:
                # Generate QR code for the entire content
                qr = qrcode.make(content, version=10)  # Adjust the version as needed
                # Save the QR code image temporarily
                with default_storage.open('temp_qr.png', 'wb') as f:
                    qr.save(f)
                # Render the template with QR code image URL
                qr_code_url = default_storage.url('temp_qr.png')
                return render(request, 'qr_code.html', {'qr_code_url': qr_code_url})
    else:
        form = FileUploadForm()
    return render(request, 'file_upload_form.html', {'form': form})

