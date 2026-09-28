from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    students= Student.objects.all()
    return render (
        request,
        'student_list.html',
        {'students': students}
    )

def student_add(request):
    if request.method == "POST" :
        form= StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(
        request,
        'student_add.html',
        { 'form' : form}
    )


def student_edit(request,id):
    student= Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'student_edit.html',
        {'form': form}
    )
def student_delete(request,id):
    student= Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')


    return render(
        request,
        'student_delete.html',
        {'student': student}
    )