from django.shortcuts import render, HttpResponse
from django.views.generic import View

class Sabado(View):
	def get(self,request):
		return HttpResponse('Bienvenido humano');

class ThugLife(View):
	def get(self,request):
		return HttpResponse('B) Thug Life');

class PagWeb(View):
	def get(self,request):
		return render(request,'hola.html');


		