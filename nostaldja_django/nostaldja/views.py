from django.shortcuts import render, redirect
from .models import Decade, Fad

# Create your views here.

# ***************************** DECADE **************************************
def decade_list(request):
  decades = Decade.objects.all()
  return render(request, 'nostaldja/decade_list.html', {'decades': decades})

def decade_detail(request, pk):
  decade = Decade.objects.get(pk=pk)
  return render(request, 'nostaldja/decade_detail.html', {'decade': decade})

# CREATE
def decade_create(request):
  if request.method == 'POST':
    form = DecadeForm(request.POST)
    if form.is_valid():
      decade = form.save
      return redirect('decade_detail', pk=decade.pk)
    else:
      form = DecadeForm()
    return render(request, 'nostaldja/decade_form.html', {'decade': decade})

# UPDATE
def decade_edit(request, pk):
  decade = Decade.objects.get(pk=pk)
  if request.method == 'POST':
    form = DecadeForm(request.POST, instance=decade)
    if form.is_valid():
      decade = form.save()
      return redirect('decade_detail', pk=decade.pk)
  else:
    form = DecadeForm(instance=decade)
  return render(request, 'nostaldja/decade_form.html', {'decade': decade})

# DELETE
def decade_delete(request, pk):
  Decade.objects.get(pk=pk).delete()
  return redirect('decade_list')

# ***************************** FAD *****************************************
def fad_list(request):
  fads = Fad.objects.all()
  return render(request, 'nostaldja/fad_list.html', {'fads':fads})

def fad_detail(request):
  fad = Fad.objects.get(id=id)
  return render(request, 'nostaldja/fad_detail.html', {'fad': fad})

# CREATE
def fad_create(request):
  if request.method == 'POST':
    fad = FadForm(request.POST)
    if form.is_valid():
      fad = form.save
      return redirect('fad_detail', id=fad.id)
    else:
      form = FadForm()
    return render(request, 'nostaldja/fad_form.html', {'fad': fad})

# UPDATE
def fad_edit(request, id):
  fad = Fads.objects.get(pk=id)
  if request.method == 'POST':
    form = FadForm(request.POST, instance=fad)
    if form.is_valid():
      fad = form.save()
      return redirect('fad_detail', id=fad.id)
  else:
    form = FadForm(instance=fad)
  return render(request, 'nostaldja/fad_form.html', {'fad': fad})


# DELETE
def fad_delete(request, id):
  Fad.objects.get(pk=id).delete()
  return redirect('fad_list')
