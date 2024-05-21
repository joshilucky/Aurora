from django.shortcuts import render
from .models import OriginPost
# Create your views here.
 
def index(request):
    originpost = OriginPost.objects.all()
    return render(request, 'index.html', {'originpost': originpost})