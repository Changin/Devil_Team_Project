from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Poetry

import datetime

def index(request):
	#poem_list = Poetry.objects.order_by('poem_title')
	return render(request, 'poem/pro.html')

def view(request):
	#poem_object = get_object_or_404(Poetry,id=1)
	poem_count = len(Poetry.objects.all())
	dt = datetime.datetime.now()
	poem_num = poem_count % dt.day
	print("count of poem : "+str(poem_count))
	return render(request, 'poem/pro1.html', {'poem_num':poem_num})