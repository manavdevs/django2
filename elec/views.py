from django.shortcuts import render,redirect,get_object_or_404
from .models import Elec
def ehome(request):
    elec = Elec.objects.all()
    return render(request, 'ehome.html', {'elec':elec})


def elec_add(request):
   if request.method == 'POST':
    name = request.POST.get('name')
    price = request.POST.get('price')
    quants = request.POST.get('quants')
    Elec.objects.create(
    name=name,
    price=price,
    quants=quants
 )
    return redirect('elec:elec_home')
   return render(request, 'elec_add.html')

def elec_edit(request, pk):
   elec = get_object_or_404(Elec, pk=pk)
   if request.method == 'POST':
     elec.name = request.POST.get('name')
     elec.price = request.POST.get('price')
     elec.quants = request.POST.get('quants')
     elec.save()
     return redirect('elec:elec_home')
   return render(request, 'elec_add.html', {'elec': elec})

def elec_delete(request, pk):
   elec = get_object_or_404(Elec, pk=pk)
   if request.method == 'POST':
     elec.delete()
     return redirect('elec:elec_home')
   return render(request, 'elec_del.html', {'elec': elec})