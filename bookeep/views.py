from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import PersonForm
from .models import Person
from django.shortcuts import redirect
from django.urls import reverse




# Create your views here.
def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")


def get_name(request):
    all = Person.objects.all()
    # all.delete()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PersonForm()

    return render(request, 'bookeep/index.html', {'form': form, "all": all})

def update(request, id):
    all = Person.objects.all()
    if request.method == 'POST':
        instance = Person.objects.get(id=id)
        form = PersonForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')

    else:
        instance = Person.objects.get(id=id)
        form = PersonForm(instance=instance)
        return render(request, 'bookeep/index.html', {'form': form, "all": all})


def post_data(request):

    if request.method == 'POST':
        if request.POST["operation"] == "Delete" and request.POST.get("item") != None:
            obj = Person.objects.get(id=request.POST["item"])
            obj.delete()
            return HttpResponseRedirect('/')
        elif request.POST["operation"] == "Update" and request.POST.get("item") != None:
            return redirect(reverse('update', kwargs={'id': request.POST["item"]}))

        else:
            return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/')
