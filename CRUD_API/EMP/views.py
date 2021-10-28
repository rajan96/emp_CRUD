from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import employee
# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'myapp/index.html',{'form':form})
def show(request):
    employees = employee.objects.all()
    return render(request,"myapp/show.html",{'employees':employees})
def edit(request, id):
    employee = employee.objects.get(id=id)
    return render(request,'myapp/edit.html', {'employee':employee})
def update(request, id):
    employee = employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'myapp/edit.html', {'employee': employee})
def destroy(request, id):
    employee = employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")