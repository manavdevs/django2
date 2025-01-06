from django.shortcuts import render,redirect,get_object_or_404
from .models import Clothes


def chome(request):
    clothes = Clothes.objects.all()
    return render(request, 'chome.html', {'clothes':clothes})


def chome_add(request):
   if request.method == 'POST':
    name = request.POST.get('name')
    price = request.POST.get('price')
    quants = request.POST.get('quants')
    Clothes.objects.create(
    name=name,
    price=price,
    quants=quants
 )
    return redirect('clothes:clothes_home')
   return render(request, 'clothes_add.html')


def clothes_edit(request, pk):
   clothes = get_object_or_404(Clothes, pk=pk)
   if request.method == 'POST':
     clothes.name = request.POST.get('name')
     clothes.price = request.POST.get('price')
     clothes.quants = request.POST.get('quants')
     clothes.save()
     return redirect('clothes:clothes_home')
   return render(request, 'clothes_add.html', {'clothes': clothes})


def clothes_delete(request, pk):
   clothes = get_object_or_404(Clothes, pk=pk)
   if request.method == 'POST':
     clothes.delete()
     return redirect('clothes:clothes_home')
   return render(request, 'clothes_del.html', {'clothes': clothes})