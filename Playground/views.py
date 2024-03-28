from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FileUploadForm
import qrcode
from django.core.files.storage import default_storage
from stegano import lsb
from django.conf import settings
import os


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service1(request):
    return render(request, 'service1.html')

def service2(request):
    return render(request, 'service2.html')

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
            # Get the uploaded image file
            uploaded_image = request.FILES['image']

            # Generate QR code for the entire content
            qr_content = "Your QR code content here"  # Replace with your actual content
            qr = qrcode.make(qr_content)

            # Define the file path to save the QR code image
            qr_file_path = os.path.join(settings.BASE_DIR, 'static/Assets', 'temp_qr.png')

            # Save the QR code image
            with open(qr_file_path, 'wb') as f:
                qr.save(f)

            # Get the uploaded image file path
            uploaded_image_path = os.path.join(settings.BASE_DIR, 'static/Assets', uploaded_image.name)

            # Save the uploaded image file
            with open(uploaded_image_path, 'wb') as f:
                for chunk in uploaded_image.chunks():
                    f.write(chunk)

            # Embed the QR code image into the uploaded image
            secret_image = lsb.hide(uploaded_image_path, qr_file_path)

            # Define the file path to save the combined image
            combined_image_path = os.path.join(settings.BASE_DIR, 'static/Assets', 'combined_image.png')

            # Save the combined image
            secret_image.save(combined_image_path)

            # Get the URL of the combined image and QR code
            combined_image_url = '/static/Assets/combined_image.png'  # Adjust as needed based on your URL configuration
            qr_code_url = '/static/Assets/temp_qr.png'

            # Render the template with the combined image and QR code URLs
            return render(request, 'qr_code_single.html', {'combined_image_url': combined_image_url, 'qr_code_url': qr_code_url})
    else:
        form = FileUploadForm()
    return render(request, 'file_upload_form.html', {'form': form})


def try_decode(file, encodings=['utf-8', 'latin-1', 'iso-8859-1']):
    for encoding in encodings:
        try:
            return file.read().decode(encoding)
        except UnicodeDecodeError:
            pass
    # If no encoding works, return empty string
    return ''
