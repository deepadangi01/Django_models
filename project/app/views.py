from django.shortcuts import render
from.models import Students

# Create your views here.
def home(request):
    return render(request,"home.html")

def register(request):
    if request.method=='POST':
        # print(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('con')
        password=request.POST.get('pass')
        cpassword=request.POST.get('cpass')

        if password==cpassword:
            user=Students.objects.filter(stu_email=email)
            if user:
                msg="Email already exist"
                return render (request,'login.html',{'msg':msg})
            else:
                Students.objects.create(
                stu_name=name,
                stu_email=email,            
                stu_contact=contact,
                stu_password=password,
                )
            msg="Registration successfull"
            return render(request,"home.html",{'msg':msg})
        else:
            msg="Password is not matching"
            return render(request,'register.html',{'msg':msg})    
    else:
        return render(request,"register.html") 


def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('pass')
        user=Students.objects.filter(stu_email=email)
        if user:
            userdata=Students.objects.get(stu_email=email)
            print(userdata)
            email1=userdata.stu_email
            password1=userdata.stu_password
            name1=userdata.stu_name
            contact1=userdata.stu_contact
            print(email1,password1,name1,contact1)
            if password==password1:
                data={
                    'name':name1,
                    'email':email1,
                    'password':password1,
                    'contact':contact1,
                }
                return render(request,'dashboad.html',{'data':data})
            else:
                msg="email and password not matched"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="email not registed"
            return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'login.html')