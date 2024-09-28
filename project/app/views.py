from django.shortcuts import render
from.models import Students

# Create your views here.
def home(request):
    return render(request,"home.html")

def register(request):
    if request.method=='POST':
        print(request.POST)
        name=request.POST.get('name')
        contact=request.POST.get('con')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        print(name,contact,email,password)

        Students.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
    msg="registration succussfully..."
    return render(request,'register.html',{'msg':msg})
