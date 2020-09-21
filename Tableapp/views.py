from django.shortcuts import render
from .models import Student
from Tableapp.forms import StudentForm
from django.shortcuts import redirect

# Create your views here.
def views1(request):
    students = Student.objects.all()
    return render(request,'star/information.html',{'students':students})


def views2(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'star/insert.html',{'form':form})
        