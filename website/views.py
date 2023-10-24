from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from . import models
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.utils import translation

# Create your views here.

def index(request):
    projects = models.Project.objects.all()
    categories = models.Category.objects.all()
    myskills = models.MySkill.objects.all()
    personal = models.Personal.objects.all()
    
    form = ContactForm()
   
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            EmailMessage(
                'Contact Name:'.format(name),
                message,
                'form-response@example.com',
                ['lostris84@hotmail.com'],
                reply_to=[email]
            ).send()
            
            return redirect('index')
    
    return render(request,'index.html',{'projects':projects, 'categories':categories,'myskills':myskills,'personal':personal,'form':form})

def project(request,course_id):
    project = get_object_or_404(models.Project,pk=course_id)
    languages_used = project.programming_languages.split(',')
    return render(request,'project.html',{'project':project,'languages_used':languages_used})

def thankyou(request):
    
    return render(request,'thank_you.html')

def test(request):
    return render(request,'test.html')