from django.shortcuts import render
from .forms import Imageforms
from .models import Image

# Create your views here.
def home(request):
    if request.method=="POST":
        fm=Imageforms(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()       
    
    fm=Imageforms()
    img=Image.objects.all()
    return render(request,'myapp/home.html',{'fm':fm,'img':img})
