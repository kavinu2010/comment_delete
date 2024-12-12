from django.shortcuts import render, redirect,get_object_or_404
from .models import Poster
from .forms import PosterForm

# Create your views here.
def home(request):
  posts=Poster.objects.all()
  return render(request,'home.html',{'posts':posts})

def post(request):
  if request.method=='POST':
    postes=PosterForm(request.POST)
    if postes.is_valid():
      postes.save()
      return redirect(home)
    
  else:
    postes=PosterForm()
  return render(request, 'post.html',{'postes':postes})


def delete(request, post_id):
  if request.method=='POST':
    postii = get_object_or_404(Poster, id=post_id)
    postii.delete()
    return redirect(home)
  
  else:
    return redirect(home)


  


