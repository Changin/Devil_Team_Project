from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Poetry

def index(request):
	#poem_list = Poetry.objects.order_by('poem_title')
	return render(request, 'poem/pro.html')

def view(request):
	#poem_object = get_object_or_404(Poetry,id=1)
	#{'poem_object':poem_object}
	return render(request, 'poem/pro1.html')