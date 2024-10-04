from django.shortcuts import render

def homepage(request):
    data = {
        "name" : "Nick",
        "age" : 25
    }
    return render(request, 'index.html',data)
