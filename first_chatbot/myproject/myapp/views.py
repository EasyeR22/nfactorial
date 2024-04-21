from django.shortcuts import render
from .models import Dog
from . import dog_api as dog

def mainpage(request):
    return render(request,'templates\mainpage.html')

def catalog(request):
    

    breeds = dog.all_breeds()
    breed_list = breeds.keys()
    for i in breed_list:
        breeds[i] = dog.random_image(i)

  

    context = {'breeds' : breeds}
    return render(request,'templates\catalog.html',context)
def info(request):
    return render(request,'templates\info.html')