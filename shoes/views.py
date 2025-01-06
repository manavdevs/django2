from django.shortcuts import render,redirect,get_object_or_404
from .models import Shoes
def shome(request):
    shoes = Shoes.objects.all()
    return render(request, 'shome.html', {'shoes':shoes})


def shoes_add(request):
   if request.method == 'POST':
    name = request.POST.get('name')
    price = request.POST.get('price')
    quants = request.POST.get('quants')
    Shoes.objects.create(
    name=name,
    price=price,
    quants=quants
 )
    return redirect('shoes:shoes_home')
   return render(request, 'shoes_add.html')

def shoes_edit(request, pk):
   shoes = get_object_or_404(Shoes, pk=pk)
   if request.method == 'POST':
     shoes.name = request.POST.get('name')
     shoes.price = request.POST.get('price')
     shoes.quants = request.POST.get('quants')
     shoes.save()
     return redirect('shoes:shoes_home')
   return render(request, 'shoes_add.html', {'shoes': shoes})

def shoes_delete(request, pk):
   shoes = get_object_or_404(Shoes, pk=pk)
   if request.method == 'POST':
     shoes.delete()
     return redirect('shoes:shoes_home')
   return render(request, 'shoes_del.html', {'shoes': shoes})