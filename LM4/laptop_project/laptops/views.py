from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopForm

def laptop_list(request):
    laptops= Laptop.objects.all()
    return render(request,'laptop_list.html',{'laptops': laptops})

def laptop_add(request):
    if request.method == "POST":
        form= LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('laptop_list')

    else:
        form = LaptopForm()

    return render(request,
                  'laptop_add.html',
                  {'form': form})


def laptop_edit(request,id):
    laptop=Laptop.objects.get(id=id)
    if request.method == "POST":
        form= LaptopForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect ('laptop_list')

    else:
        form = LaptopForm(instance=laptop)

    return render(request,
                  'laptop_edit.html',
                  {'form': form})


def laptop_delete(request,id):
    laptop=Laptop.objects.get(id=id)
    if request.method == "POST":
        laptop.delete()
        return redirect('laptop_list')



    return render(request,
                  'laptop_delete.html',
                  {'laptop': laptop})
