from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.


def home(request):
  info = CompanyInformation.objects.first()

   
  data ={
      
      'info':info,
      
   }
   
  return render(request, 'home.html',data)

def about(request):
    # Retrieve company information from the database or define it here
    CompanyInformation = {
        'name': 'Your Company Name',
        'description': 'A brief description of your company.',
        'founded_year': 2020,
        'location': 'Your Company Location',
        # Add more fields as needed
    }
    context = {
        'company_info': CompanyInformation
    }
    return render(request, 'about.html', context)

def contact_us(request):
   
   if request.method =='POST':
      user_name  = request.POST.get('name')
      user_email  = request.POST.get('email')
      user_text  = request.POST.get('text')
   
      obj = ContactInfo()
      
      obj.name = user_name
      obj.email =user_email
      obj.text = user_text
      obj.save()
   return render(request, 'contact.html')


def product(request):
  info = CompanyInformation.objects.first()
  products = Product.objects.all()
   
  data ={
      
      'info':info,
      'products':products
   }
   
  return render(request, 'product.html',data)