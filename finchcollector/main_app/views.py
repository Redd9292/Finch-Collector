from django.shortcuts import render

finches = [
  {'name': 'Lolo', 'breed': 'Society Finch', 'description': 'skittish', 'age': 1},
  {'name': 'Sachi', 'breed': 'Purple Finch', 'description': 'gentle and loving', 'age': 2},
]


# Create your views here.

def home(request):
    #include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })