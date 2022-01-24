from sys import intern
from django.shortcuts import redirect, render, HttpResponse
from .models import EmployeeDetails

# Create your views here.

# fetch all data on main admin page....
def index(request,id=0):
    data = EmployeeDetails.objects.all()
    employee_data = {
        "employee": data
    }
    
    return render(request,'admin.html',employee_data)

# insert data....................................
def add(request):
    
    if request.method=="POST":

        name = request.POST.get("name")
        email_id = request.POST.get("email")
        salary = request.POST.get("salary")
        status = request.POST.get("status")     
        image = request.FILES.get("image")
        intern_status = False
        if status:
            intern_status = True
        
        EmployeeDetails.objects.create(name=name,email_id=email_id,salary=salary,img=image,intern_status=intern_status)
        
        return redirect('/')
    
    return render(request,'addEmployee.html')
    
# update employee data.........................
def update(request,*args,**kwargs):
  
    data = EmployeeDetails.objects.get(pk=kwargs['id'])
    old_image = data.img
    context = {
        "emp_data":data
    }
    
    if request.method == "POST":
        data.name = request.POST.get("name")
        data.email_id = request.POST.get("email")
        data.salary = request.POST.get("salary")
        status = request.POST.get("status")     
        data.img = request.FILES.get("image")
        if data.img == None:
            data.img = old_image
        data.intern_status = False
        if status:
            data.intern_status = True
        data.save()
        return redirect('/')
    return render(request,'editEmployee.html',context)

# delete record........

def delete(request,id):
    data = EmployeeDetails.objects.get(pk=id)
    data.delete()
    return redirect("/")
