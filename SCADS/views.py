from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return HttpResponse("<h1>The HomePage</h1>")