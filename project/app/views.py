from django.shortcuts import render
from.models import Students
from.models import myQuery
from django.http import HttpResponse

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
            return render(request,"dashboad.html",{'msg':msg})
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
                query_data = myQuery.objects.filter(stu_email=email)
                return render(request,'dashboad.html',{'data':data,'query_data':query_data})
            else:
                msg="email and password not matched"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="email not registed"
            return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'login.html')
    
# def all_details(request):
#         data=Students.objects.all().values_list('stu_name','stu_email','stu_contact','stu_password')
#         print(data)
#         print(data.values_list())
        
#         return HttpResponse(data)
    
# def filter(request):
#     data=Students.objects.filter(stu_name="deepa")
#     print(data)
#     return HttpResponse(data)
# def exclude(request):
#     data=Students.objects.exclude(stu_name="deepa")
#     print(data)
#     return HttpResponse(data)
# def order(request):
#     data=Students.objects.order_by('stu_name')
#     return HttpResponse(data)
# def dis_order(request):
#     #data=Students.objects.order_by('-stu_name')
#     data=Students.objects.order_by('stu_name').reverse()
#     return HttpResponse(data)
# def slice(request):
#     data=Students.objects.all()
#     return HttpResponse(data)  



def query(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('query')
        print(name,email,query)
        myQuery.objects.create(
        stu_email=email,
        stu_name=name,
        stu_query=query)
        data=Students.objects.get(stu_email=email)
        data={
        'name':data.stu_name,
        'email':data.stu_email,
        'contact':data.stu_contact,
        'password':data.stu_password
        }
        
        query_data=myQuery.objects.filter(stu_email=email)
        print(data,query_data)
        return render(request,'dashboad.html',{'data':data,'query_data':query_data})
    msg="succusfull....."
    return render(request,'dashboad.html',{'msg':msg})

def edit(request,x):
    data1=myQuery.objects.get(id=x)
    id1=data1.id
    email=data1.stu_email
    name=data1.stu_name
    query=data1.stu_query
    data=Students.objects.get(stu_email=email)
    data={
        'name':data.stu_name,
        'email':data.stu_email,
        'contact':data.stu_contact,
        'password':data.stu_password
        }
    query_data=myQuery.objects.filter(stu_email=email)
    edit_data={
        'id':id1,
        'email':email,
        'name':name,
        'query':query,
    }
    return render(request,'dashboad.html',{'key2':edit_data, 'data':data, 'query_data':query_data})
def update(request,x):
    if request.method=="POST":
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        query1=request.POST.get('query')
        print(name1,email1,query1)
        oldData=myQuery.objects.get(id=x)

        oldData.stu_name=name1
        oldData.stu_email=email1
        oldData.stu_query=query1
        oldData.save()
    
        data=Students.objects.get(stu_email=email1)
        
        data={
           'name':data.stu_name,
           'email':data.stu_email,
           'contact':data.stu_contact,
           'password':data.stu_password
        }  
        query_data=myQuery.objects.filter(stu_email=email1)
    return render(request,'dashboad.html',{'data':data, 'query_data':query_data}) 

def delete(request,x,y):
    queryData=myQuery.objects.filter(id=x)
    if queryData:
        queryData=myQuery.objects.get(id=x)
        name1=queryData.stu_name
        email1=queryData.stu_email
        query1=queryData.stu_query

        queryData.delete()
        data=Students.objects.get(stu_email=email1)
        
        data={
           'name':data.stu_name,
           'email':data.stu_email,
           'contact':data.stu_contact,
           'password':data.stu_password
        } 
        query_data=myQuery.objects.filter(stu_email=email1)
        return render(request,'dashboad.html',{'data':data,'query_data':query_data})
    else:
        data=Students.objects.get(stu_email=y)
        data={
           'name':data.stu_name,
           'email':data.stu_email,
           'contact':data.stu_contact,
           'password':data.stu_password
        }  
        query_data=myQuery.objects.filter(stu_email=y)
        return render(request,'dashboad.html',{'query_data':query_data,'data':data})
def logout(request):
    return render(request,'home.html')
        
        
        
   
   



    
# def first(request):
#     data=Students.objects.first()
#     print(data)
#     print(data.stu_name,data.stu_contact,data.stu_email,data.stu_password)
#     return  HttpResponse(data)
# def last(request):
#     data=Students.objects.last()
#     print(data)
#     print(data.stu_name,data.stu_contact,data.stu_email,data.stu_password)

#     return HttpResponse(data)
# def lastest(request):
#     data=Students.objects.latest("id")
#     print(data)
#     return HttpResponse(data)

