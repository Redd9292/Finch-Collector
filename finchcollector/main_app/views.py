from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Finch

# finches = [
#   {'name': 'Lolo', 'breed': 'Society Finch', 'description': 'skittish', 'age': 1},
#   {'name': 'Sachi', 'breed': 'Purple Finch', 'description': 'gentle and loving', 'age': 2},
#   {'name': 'Penny', 'breed': 'Zebra finch', 'description': 'always curious', 'age': 2},
# ]


# Create your views here.

def home(request):
    #include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



def finches_index(request):
    finches = Finch.objects.all() # Retrieve all cats
    return render(request, 'finches/index.html', 
    { 
        'finches': finches
    }
    )

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'