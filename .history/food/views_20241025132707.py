from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
  item_list = Item.objects.all()
  loader.get_template('food/index.html')
  return HttpResponse(item_list)

def item(request):
  return HttpResponse("This is an item view")
