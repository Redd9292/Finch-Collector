from django.shortcuts import render

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

# def finches_index(request):
#     finches = Finch.objects.all()
#     return render(request, 'finches/index.html', {
#         'finches': finches
#     })

def finches_index(request):
    finches = Finch.objects.all() # Retrieve all cats
    return render(request, 'finches/index.html', 
    { 
        'finches': finches
    }
    )
# def finches_detail(request, finch_id):
#     finch = Finch.objects.get(id=finch_id)
#     return render(request 'finches/detail.html', { 'finch': finch})

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })