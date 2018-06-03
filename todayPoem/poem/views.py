from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Poetry

def index(request):
	poem_list = Poetry.objects.order_by('poem_title')
	return render(request, 'poem/index.html',{'poem_list':poem_list})

def view(request, poem_id):
	poem_object = get_object_or_404(Poetry,id=poem_id)
	return render(request, 'poem/detail.html', {'poem_object':poem_object})