
from django.shortcuts import render, HttpResponse
from app.models import Musician

# Create your views here.

def index(request):
	x = Musician.objects.all()
	print x
	o = []
	for each in x:
		o.append(each.first_name)
	return render(request,'app/prof.html',{'data':o})
    #return HttpResponse('Hello World!')

def test(request):
	x = request.GET.get('mus', '')
	b = Musician(first_name=x)
	b.save()
	return HttpResponse('Added !')